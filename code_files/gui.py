from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
import sys
from ui_MainMenu import Ui_MainMenu
from ui_NewGallery import Ui_NewGallery
from fetching_topic import get_topics
import json


class GalleryWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.ui.action_New_Gallery.triggered.connect(self.new_gallery)

    def new_gallery(self):

        dialog = GalleryDialog(self)
        if dialog.exec_():
            pass


class GalleryDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NewGallery()
        self.ui.setupUi(self)
        self.topics_list()

    def topics_list(self):
        with open("api.json") as file:
            data = json.load(file)
            url_topics = data["topic-fetching-url"]
            list_of_topics = get_topics(url_topics)
        for topic in list_of_topics:
            self.ui.topicsList.addItem(str(topic))


def guiMain(args):
    app = QApplication(args)
    window = GalleryWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
