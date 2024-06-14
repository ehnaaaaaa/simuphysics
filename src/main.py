import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog
from mainUI import Ui_MainWindow
from modalInfo import Ui_Dialog


class InfoModal(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.infoBtn.clicked.connect(self.__info_dialog)

    @classmethod
    def __info_dialog(cls):
        cls.infoModal.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    MainWindow.infoModal = InfoModal()
    window.show()

    sys.exit(app.exec())
