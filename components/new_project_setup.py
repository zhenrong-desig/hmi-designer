import os
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import json


class new_project_setup(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("components/ui/new_project_setup.ui", self)
        self.listView = self.findChild(QtWidgets.QListView, "listView")
        self.label_2.setWordWrap(True)
        self.model = QStandardItemModel()
        base_path = sys._MEIPASS
        config_file_path = os.path.join(base_path, "configs",
                                        "touch_panel_config.json")
        self.load_touch_panel_item_from_config(config_file_path)
        self.listView.setModel(self.model)
        self.listView.setCurrentIndex(self.model.index(0, 0))
        self.listView.clicked.connect(self.on_touch_panel_item_clicked)
        self.on_touch_panel_item_clicked(self.model.index(0, 0))

    def on_touch_panel_item_clicked(self, index):
        touch_panel_info = self.model.itemFromIndex(index).data(role=1)
        self.label_2.setText(f"{touch_panel_info}")

    def load_touch_panel_item_from_config(self, config_file):
        with open(
                config_file,
                "r",
                encoding="utf-8",
        ) as file:
            config_data = json.load(file)

        for item_data in config_data["items"]:
            item = QStandardItem(item_data["text"])
            item.setData(item_data["panel_info"], role=1)
            self.model.appendRow(item)
