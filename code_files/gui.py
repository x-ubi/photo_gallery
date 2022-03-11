from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from PySide6.QtGui import QPixmap
import sys
from pathlib import Path
from ui.ui_MainMenu import Ui_MainMenu
from ui.ui_NewGallery import Ui_NewGallery
from ui.ui_NewCollage import Ui_NewCollage
from ui.ui_EditPhoto import Ui_editDialog
from fetching_topic import get_topics
from fetching_photos import fetch_photos_of_topic
from collage_maker import collage
from edit_photo import crop, rotate, black_and_white, gaussian_blur
from PIL import Image
import numpy as np
import json
import requests
from io import BytesIO
from random import randint
from math import ceil


class GalleryWindow(QMainWindow):
    """Main window of the GUI.
    Responsible for opening dialogs by clicking on an action."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.ui.action_New_Gallery.triggered.connect(self.new_gallery)
        self.ui.action_Collage.triggered.connect(self.collage)
        self.ui.action_Edit_photos.triggered.connect(self.edit_a_photo)

    def new_gallery(self):
        """Create a new gallery of photos.
        Open a dialog for gallery creation.
        Wait for user to choose topic and number of photos
        from that topic to save in a gallery.
        Open a dialog for the user to choose a directory.
        Download and save photos to the chosen directory.
        """
        creation_dialog = GalleryDialog(self)
        creation_dialog.exec()
        if creation_dialog.result():
            topics = creation_dialog.get_list_of_topics()
            chosen_topic_index = creation_dialog.ui.topicsList.currentIndex()
            chosen_topic_id = topics[chosen_topic_index].id()
            number_of_photos = creation_dialog.ui.spinBox.value()
            list_of_photos = photos_list(chosen_topic_id,
                                         number_of_photos, randint(1, 5))
            save_dialog = SaveGallery(self)
            save_dialog.exec()
            if save_dialog.result():
                selected_folder = save_dialog.selected_folder()
                download_photos(selected_folder, list_of_photos)


    def collage(self):
        """Create a collage.
        Open a dialog and wait for the user to choose a directory where
        the photos will be fetched from.
        Open a dialog for collage creation.
        Wait for user to choose how many photos, specify the number of rows,
        and how many pictures there should be in each row.
        Create a collage using the information provided by the user.
        Open a dialog and wait for the user to name the collage.
        Save the collage under the chosen name.
        """
        creation = CollageDialog(self)
        gallery_exists = False
        while not gallery_exists:
            creation.exec()
            if creation.result() and creation.chosen_gallery is not None:
                gallery_exists = True
                chosen_gallery = creation.chosen_gallery
                save_dialog = SaveCollage(self)
                if save_dialog.result():
                    collage(chosen_gallery,
                            save_dialog.get_filename(),
                            creation.ui.photosNumber.value(),
                            creation.ui.picsinRow.value())
            elif not creation.result():
                break

    def edit_a_photo(self):
        """Edit a chosen photo.
        Open a dialog and wait for the user to choose photo to be edited.
        Open a dialog where the photo will be displayed,
        along with effects for the user to choose from.
        Save the edited file under the same name
        to overwrite the original file.
        """
        edit_dialog = EditDialog(self)
        edit_dialog.exec()
        if edit_dialog.result():
            edit_dialog.photo.save(edit_dialog.filename)


class EditDialog(QDialog):
    """A dialog responsible for editing photos.
    Displays possible effects and a photo chosen by the user that changes
    every time the user adds an effect to reflect it.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_editDialog()
        self.ui.setupUi(self)
        self.filename = ""
        self.get_photo()
        self.photo = Image.open(self.filename)
        while self.photo.height > 900:
            width, height = self.photo.size
            self.photo = self.photo.resize((width // 2, height // 2))
        self.photo_buffer = self.photo
        for item in ['90', '180', '270', '360']:
            self.ui.comboBoxDegrees.addItem(item)
        for item in ['left', 'right']:
            self.ui.comboBoxDir.addItem(item)
        self.ui.newWidth.setMaximum(self.photo.width)
        self.ui.newHeight.setMaximum(self.photo.height)
        self.photo_to_label()
        self.ui.blurChange.clicked.connect(self.blur_photo)
        self.ui.cropChange.clicked.connect(self.crop_photo)
        self.ui.rotateChange.clicked.connect(self.rotate_photo)
        self.ui.blackWhite.stateChanged.connect(self.bw_photo)
        self.ui.newWidth.valueChanged.connect(self.set_max_startingx)
        self.ui.newHeight.valueChanged.connect(self.set_max_startingy)

    def set_max_startingx(self):
        """Set maximum value of starting x coordinate."""
        self.ui.startingX.setMaximum(self.photo.width
                                     - self.ui.newWidth.value())

    def set_max_startingy(self):
        """Set maximum value of starting y coordinate."""
        self.ui.startingY.setMaximum(self.photo.height
                                     - self.ui.newHeight.value())

    def get_photo(self):
        """Get the name of the photo from user."""
        open_photo = OpenPhoto()
        self.filename = open_photo.get_filename()
        return self.filename

    def photo_to_label(self):
        """Display the photo on a QLabel object inside the dialog."""
        photo_buffer = generate_photo(self.photo)
        pixmap = QPixmap()
        pixmap.loadFromData(photo_buffer)
        self.ui.photoDisplay.setPixmap(pixmap)

    def crop_photo(self):
        """Crop the photo, then display it on screen."""
        photo_data = photo_to_numpy(self.photo)
        self.photo = crop(photo_data,
                          self.ui.newWidth.value(),
                          self.ui.newHeight.value(),
                          self.ui.startingX.value(),
                          self.ui.startingY.value())
        self.photo_to_label()

    def rotate_photo(self):
        """Rotate the photo, then display it on screen."""
        photo_data = photo_to_numpy(self.photo)
        self.photo = rotate(photo_data,
                            ((self.ui.comboBoxDegrees.currentIndex() + 1)
                             * ((-1) ** self.ui.comboBoxDir.currentIndex())
                             )
                            )
        self.photo_to_label()

    def blur_photo(self):
        """Blur the photo, then display it on screen."""
        self.photo = gaussian_blur(self.photo, self.ui.blurRadius.value())
        self.photo_to_label()

    def bw_photo(self):
        """Make the photo black and white, then display it on screen."""
        if self.ui.blackWhite.isChecked():
            self.photo_buffer = self.photo
            self.photo = black_and_white(self.photo)
        else:
            self.photo = self.photo_buffer
        self.photo_to_label()


class GalleryDialog(QDialog):
    """Dialog responsible for creating a new gallery.
    Displays possible topics to choose from."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NewGallery()
        self.ui.setupUi(self)
        self.list_of_topics = topics_list()
        for topic in self.list_of_topics:
            self.ui.topicsList.addItem(str(topic))

    def get_list_of_topics(self):
        """Return list of topics provided by the API."""
        return self.list_of_topics


class CollageDialog(QDialog):
    """Dialog responsible for creating a collage out of photos.
    Displays options for specifying which photos to use
    along with the number of them,
    how many rows the collage should have,
    and how many pictures does every row include."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NewCollage()
        self.ui.setupUi(self)
        self.chosen_gallery = None
        self.ui.chooseDir.clicked.connect(self.choose_gallery)
        self.ui.photosNumber.valueChanged.connect(self.change_pics_value)

    def choose_gallery(self):
        """Wait for the user to choose a directory to fetch photos from
        and return the directory."""
        choose_dir = OpenGallery(self)
        choose_dir.exec()
        if choose_dir.result():
            self.chosen_gallery = choose_dir.selected_folder()
            self.ui.Directory.setPlainText(self.chosen_gallery)
            return self.chosen_gallery

    def change_pics_value(self):
        """Change maximum amount of photos in a singular row of collage."""
        self.ui.picsinRow.setMaximum(ceil(self.ui.photosNumber.value() / 2))


class SaveGallery(QFileDialog):
    """FileDialog responsible for saving a gallery to an existing directory."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFileMode(QFileDialog.Directory)
        self.setAcceptMode(QFileDialog.AcceptSave)
        self.setOption(QFileDialog.ShowDirsOnly, True)

    def selected_folder(self):
        """Return selected directory."""
        return self.selectedFiles()[0]


class OpenGallery(QFileDialog):
    """FileDialog responsible for opening a folder
    that contains a gallery of photos."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFileMode(QFileDialog.Directory)
        self.setAcceptMode(QFileDialog.AcceptOpen)
        self.setOption(QFileDialog.ShowDirsOnly, True)

    def selected_folder(self):
        """Return selected directory."""
        return self.selectedFiles()[0]


class OpenPhoto(QFileDialog):
    """FileDialog responsible for selecting a photo to use for editing."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fileName = self.getOpenFileName(self,
                                             self.tr("Open File"), "",
                                             self.tr("Images (*.jpg)"))

    def get_filename(self):
        """Return selected photo."""
        return self.fileName[0] if self.fileName[0] else None


class SaveCollage(QFileDialog):
    """FileDialog responsible for letting the user
    provide a name for a collage."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fileName = self.getSaveFileName(self,
                                             self.tr("Save As"), "",
                                             self.tr("Images (*.jpg)"))
        if self.fileName:
            self.setResult(1)

    def get_filename(self):
        """Return selected file."""
        return self.fileName[0]


def get_data_from_json_file():
    """Get data from a .json file, then return it."""
    with open(f"{Path(__file__).parent}/api.json") as file:
        data = json.load(file)
        return data


def topics_list():
    """Get the topics list from the server, then return it."""
    data = get_data_from_json_file()
    url_topics = data["topic-fetching-url"]
    list_of_topics = get_topics(url_topics)
    return list_of_topics


def photos_list(given_id, given_number, given_page):
    """Get the list of photos from the server, then return it.
    Keyword arguments:
    given_id -- topic id
    given_number -- number of photos to fetch
    given_page -- the page number to fetch the photos from
    """
    data = get_data_from_json_file()
    url_photos = data["photo-fetching-url"]
    list_of_photos = fetch_photos_of_topic(url_photos,
                                           given_id,
                                           given_number,
                                           given_page)
    return list_of_photos


def download_photos(selected_folder, list_of_photos):
    """Download photos of the selected list to a folder.
    Keyword arguments:
    selected_folder - directory where the photos will be saved
    list_of_photos - list of photos to download
    """
    for photo in list_of_photos:
        photo_download_url = photo['urls']['regular']
        downloaded_photo = requests.get(photo_download_url,
                                        allow_redirects=True)
        open(f"{selected_folder}/photo{list_of_photos.index(photo)}.jpg",
             "wb").write(downloaded_photo.content)


def photo_to_numpy(photo):
    """Make a numpy array out of a given photo.
    Keyword arguments:
    photo -- a given photo to make into an array
    """
    photo_data = np.array(photo)
    return photo_data


def generate_photo(photo):
    """Save a photo to a buffer.
    Keyword arguments:
    photo -- a given photo to save into buffer
    """
    buffer = BytesIO()
    photo.save(buffer, "JPEG")
    return buffer.getvalue()


def guiMain(args):
    """Main function"""
    app = QApplication(args)
    window = GalleryWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    guiMain(sys.argv)
