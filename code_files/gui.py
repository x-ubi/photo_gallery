from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from PySide2.QtGui import QPixmap
import sys
from ui_MainMenu import Ui_MainMenu
from ui_NewGallery import Ui_NewGallery
from ui_NewCollage import Ui_NewCollage
from ui_EditPhoto import Ui_editDialog
from fetching_topic import get_topics
from fetching_photos import fetch_photos_of_topic
from collage_maker import collage
from edit_photo import crop, rotate, black_and_white, gaussianblur
from PIL import Image
import numpy as np
import json
import requests
from io import BytesIO


class GalleryWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.ui.action_New_Gallery.triggered.connect(self.new_gallery)
        self.ui.action_Collage.triggered.connect(self.collage)
        self.ui.action_Edit_photos.triggered.connect(self.edit_a_photo)

    def new_gallery(self):
        creation_dialog = GalleryDialog(self)
        creation_dialog.exec()
        if creation_dialog.accepted:
            topics = creation_dialog.get_list_of_topics()
            chosen_topic_index = creation_dialog.ui.topicsList.currentIndex()
            chosen_topic_id = topics[chosen_topic_index].id()
            number_of_photos = creation_dialog.ui.spinBox.value()
            list_of_photos = photos_list(chosen_topic_id, number_of_photos, 1)
            save_dialog = SaveGallery(self)
            save_dialog.exec()
            if save_dialog.accepted:
                selected_folder = save_dialog.selected_folder()
                download_photos(selected_folder, list_of_photos)

    def collage(self):
        creation_dialog = CollageDialog(self)
        creation_dialog.exec()
        if creation_dialog.accepted:
            chosen_gallery = creation_dialog.chosen_gallery
            save_dialog = SaveCollage(self)
            if save_dialog.accepted:
                collage(chosen_gallery,
                        save_dialog.get_filename(),
                        creation_dialog.ui.NoOfRows.value(),
                        creation_dialog.list_of_pics_per_row())

    def edit_a_photo(self):
        edit_dialog = EditDialog(self)
        edit_dialog.exec()
        if edit_dialog.accepted:
            edit_dialog.photo.save(edit_dialog.filename)


class EditDialog(QDialog):
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
        self.photo_to_label()
        self.ui.blurChange.clicked.connect(self.blur_photo)
        self.ui.cropChange.clicked.connect(self.crop_photo)
        self.ui.rotateChange.clicked.connect(self.rotate_photo)
        self.ui.blackWhite.pressed.connect(self.bw_photo)

    def get_photo(self):
        while not self.filename:
            open_photo = OpenPhoto()
            self.filename = open_photo.get_filename()
        return self.filename

    def photo_to_label(self):
        photo_buffer = generate_photo(self.photo)
        pixmap = QPixmap()
        pixmap.loadFromData(photo_buffer)
        self.ui.photoDisplay.setPixmap(pixmap)

    def crop_photo(self):
        photo_data = photo_to_numpy(self.photo)
        self.photo = crop(photo_data,
                          self.ui.newWidth.value(),
                          self.ui.newHeight.value(),
                          self.ui.startingX.value(),
                          self.ui.startingY.value())
        self.photo_to_label()

    def rotate_photo(self):
        photo_data = photo_to_numpy(self.photo)
        self.photo = rotate(photo_data,
                            (self.ui.comboBoxDegrees.currentIndex() + 1))
        self.photo_to_label()

    def blur_photo(self):
        self.photo = gaussianblur(self.photo, self.ui.blurRadius.value())
        self.photo_to_label()

    def bw_photo(self):
        self.photo = black_and_white(self.photo)
        self.photo_to_label()


class GalleryDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NewGallery()
        self.ui.setupUi(self)
        self.list_of_topics = topics_list()
        for topic in self.list_of_topics:
            self.ui.topicsList.addItem(str(topic))

    def get_list_of_topics(self):
        return self.list_of_topics


class CollageDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NewCollage()
        self.ui.setupUi(self)
        self.ui.chooseDir.clicked.connect(self.choose_gallery)
        self.ui.photosNumber.valueChanged.connect(self.change_noofrows_value)

    def choose_gallery(self):
        choose_dir = OpenGallery(self)
        choose_dir.exec()
        if choose_dir.accepted:
            self.chosen_gallery = choose_dir.selected_folder()
            self.ui.Directory.setPlainText(self.chosen_gallery)
            return self.chosen_gallery

    def change_noofrows_value(self):
        self.ui.NoOfRows.setMaximum(self.ui.photosNumber.value())

    def list_of_pics_per_row(self):
        self.list_pics_per_row = [int(number)
                                  for number
                                  in self.ui.NoOfPics.toPlainText().split(", ")
                                  ]
        return self.list_pics_per_row


class SaveGallery(QFileDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFileMode(QFileDialog.Directory)
        self.setAcceptMode(QFileDialog.AcceptSave)
        self.setOption(QFileDialog.ShowDirsOnly, True)

    def selected_folder(self):
        return self.selectedFiles()[0]


class OpenGallery(QFileDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFileMode(QFileDialog.Directory)
        self.setAcceptMode(QFileDialog.AcceptOpen)
        self.setOption(QFileDialog.ShowDirsOnly, True)

    def selected_folder(self):
        return self.selectedFiles()[0]


class OpenPhoto(QFileDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fileName = QFileDialog.getOpenFileName(self,
                                                    self.tr("Open File"), "",
                                                    self.tr("Images (*.jpg)"))

    def get_filename(self):
        return self.fileName[0]


class SaveCollage(QFileDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fileName = QFileDialog.getSaveFileName(self,
                                                    self.tr("Save As"), "",
                                                    self.tr("Images (*.jpg)"))

    def get_filename(self):
        return self.fileName[0]


def get_data_from_json_file():
    with open("api.json") as file:
        data = json.load(file)
        return data


def topics_list():
    data = get_data_from_json_file()
    url_topics = data["topic-fetching-url"]
    list_of_topics = get_topics(url_topics)
    return list_of_topics


def photos_list(given_id, given_number, given_page):
    data = get_data_from_json_file()
    url_photos = data["photo-fetching-url"]
    list_of_photos = fetch_photos_of_topic(url_photos,
                                           given_id,
                                           given_number,
                                           given_page)
    return list_of_photos


def download_photos(selected_folder, list_of_photos):
    for photo in list_of_photos:
        photo_download_url = photo['urls']['regular']
        downloaded_photo = requests.get(photo_download_url,
                                        allow_redirects=True)
        open(f"{selected_folder}/photo{list_of_photos.index(photo)}.jpg",
             "wb").write(downloaded_photo.content)


def photo_to_numpy(photo):
    photo_data = np.array(photo)
    return photo_data


def generate_photo(photo):
    buffer = BytesIO()
    photo.save(buffer, "JPEG")
    return buffer.getvalue()


def guiMain(args):
    app = QApplication(args)
    window = GalleryWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
