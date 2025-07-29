import sys
from PyQt5 import QtWidgets, uic
from components.device_select import device_select
from components.new_project_setup import new_project_setup
from components.user_manual import user_manual
import os


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        ui_path = "components/ui/mainwindow.ui"
        uic.loadUi(ui_path, self)
        self.actionnew.triggered.connect(self.show_new_project_setup)
        self.actiondevice_select.triggered.connect(self.show_device_seletct)
        self.actionnew_user_window.triggered.connect(self.show_user_manual)

    def show_new_project_setup(self):
        dialog = new_project_setup(self)
        dialog.exec_()

    def show_device_seletct(self):
        dialog = device_select(self)
        dialog.exec_()

    def show_user_manual(self):
        dialog = user_manual(self)
        dialog.showMaximized()
        dialog.exec_()

    def list_resources(self):
        base_path = getattr(sys, "_MEIPASS", os.getcwd())
        print("Base path:", base_path)
        for root, dirs, files in os.walk(base_path):
            for file in files:
                print("Found:", os.path.join(root, file))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    # window.list_resources()
    sys.exit(app.exec_())
