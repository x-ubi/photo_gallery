from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
import sys
from ui_MainMenu import Ui_MainMenu
from ui_NewGallery import Ui_NewGallery
from ui_NewCollage import Ui_NewCollage
from fetching_topic import get_topics
from fetching_photos import fetch_photos_of_topic
from PIL import Image
import json
import requests


class GalleryWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.ui.action_New_Gallery.triggered.connect(self.new_gallery)
        self.ui.action_Collage.triggered.connect(self.collage)

    def new_gallery(self):
        creation_dialog = GalleryDialog(self)
        if creation_dialog.exec_():
            topics = creation_dialog.get_list_of_topics()
            chosen_topic_index = creation_dialog.ui.topicsList.currentIndex()
            chosen_topic_id = topics[chosen_topic_index].id()
            number_of_photos = creation_dialog.ui.spinBox.value()
            list_of_photos = photos_list(chosen_topic_id, number_of_photos, 1)
            save_dialog = SaveGallery(self)
            if save_dialog.exec_():
                selected_folder = save_dialog.selected_folder()
                download_photos(selected_folder, list_of_photos)

    def collage(self):
        creation_dialog = CollageDialog(self)
        if creation_dialog.exec_():
            chosen_gallery = creation_dialog.chosen_gallery
            save_dialog = SaveCollage(self)
            if save_dialog.exec_():
                pass


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

    def choose_gallery(self):
        choose_dir = OpenGallery(self)
        if choose_dir.exec_():
            self.chosen_gallery = choose_dir.selected_folder()
            self.ui.Directory.setPlainText(self.chosen_gallery)
            return self.chosen_gallery


class SaveGallery(QFileDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFileMode(QFileDialog.Directory)
        self.setAcceptMode(QFileDialog.AcceptSave)
        self.setOption(QFileDialog.ShowDirsOnly, True)

    def selected_folder(self):
        # self.folderName = QFileDialog.getSaveFileName(self, self.tr("Choose folder"),"",tr("Directory")
        return self.selectedFiles()[0]


class OpenGallery(QFileDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFileMode(QFileDialog.Directory)
        self.setAcceptMode(QFileDialog.AcceptOpen)
        self.setOption(QFileDialog.ShowDirsOnly, True)

    def selected_folder(self):
        return self.selectedFiles()[0]


class SaveCollage(QFileDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fileName = QFileDialog.getSaveFileName(self,
                                                    self.tr("Save As"), "",
                                                    self.tr("Images (*.jpg)"))




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
        photo_download_url = photo['urls']['full']
        downloaded_photo = requests.get(photo_download_url,
                                        allow_redirects=True)
        open(f"{selected_folder}/photo{list_of_photos.index(photo)}.jpg",
             "wb").write(downloaded_photo.content)


def guiMain(args):
    app = QApplication(args)
    window = GalleryWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
