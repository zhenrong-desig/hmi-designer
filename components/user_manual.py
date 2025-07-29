from PyQt5 import QtWidgets, uic
import os
import sys

from PyQt5.QtCore import QModelIndex
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from components.custom.canvasView import canvasView
from components.custom.draggableTreeview import draggableTreview
from utils.json_parser import json_parser


class user_manual(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("components/ui/user_manual.ui", self)
        self.dialoglayout = self.findChild(QtWidgets.QHBoxLayout,
                                           "horizontalLayout")
        self.treeView = self.findChild(draggableTreview, "treeView")
        self.treeView.setDragEnabled(True)
        self.treeView.setDragDropMode(QtWidgets.QTreeView.DragOnly)
        self.treeView.clicked.connect(self.tree_item_clicked)
        self.dialoglayout.addWidget(self.treeView)

        self.graphiview = self.findChild(canvasView, "graphicsView")
        self.dialoglayout.addWidget(self.graphiview)

        self.tableView = self.findChild(QtWidgets.QTableView, "tableView")
        self.dialoglayout.addWidget(self.tableView)

        self.dialoglayout.setStretchFactor(self.treeView, 1)
        self.dialoglayout.setStretchFactor(self.graphiview, 2)
        self.dialoglayout.setStretchFactor(self.tableView, 1)
        parser = json_parser()
        base_path = sys._MEIPASS
        config_file_path = os.path.join(base_path, "configs",
                                        "user_configuration.json")
        configuration_data = parser.load_item_data_from_config(
            config_file_path)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["控件选择"])
        if "buttons" in configuration_data:
            buttons_item = QStandardItem("按钮")
            self.model.appendRow(buttons_item)
            for button_data in configuration_data["buttons"]:
                buttons_name_item = QStandardItem(button_data["name"])
                buttons_item.appendRow(buttons_name_item)

        if "switchs" in configuration_data:
            switchs_item = QStandardItem("开关")
            self.model.appendRow(switchs_item)
            for switch_data in configuration_data["switchs"]:
                switchs_name_item = QStandardItem(switch_data["name"])
                switchs_item.appendRow(switchs_name_item)

        if "curves" in configuration_data:
            curves_item = QStandardItem("曲线")
            self.model.appendRow(curves_item)
            for curve_data in configuration_data["curves"]:
                curves_name_item = QStandardItem(curve_data["name"])
                curves_item.appendRow(curves_name_item)

        if "charts" in configuration_data:
            charts_item = QStandardItem("图表")
            self.model.appendRow(charts_item)
            for chart_data in configuration_data["charts"]:
                charts_name_item = QStandardItem(chart_data["name"])
                charts_item.appendRow(charts_name_item)

        self.treeView.setModel(self.model)

        self.table_model = QStandardItemModel()
        self.table_model.setHorizontalHeaderLabels(["属性", "值"])
        self.tableView.setModel(self.table_model)
        self.tableView.horizontalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableView.horizontalHeader().setSectionResizeMode(
            1, QtWidgets.QHeaderView.Stretch)
        self.tableView.verticalHeader().setVisible(False)

    def tree_item_clicked(self, index: QModelIndex):
        item = self.treeView.model().itemFromIndex(index)
        name = item.text()
        if self.table_model.rowCount() > 0:
            self.table_model.removeRows(0, self.table_model.rowCount())
        property_data = self.get_item_property(name)
        if property_data is not None:
            for prop in property_data["property"]:
                name_item = QStandardItem(prop["name"])
                value_item = QStandardItem(prop["value"])
                self.table_model.appendRow([name_item, value_item])

    def get_item_property(self, name):
        parser = json_parser()
        base_path = sys._MEIPASS
        config_file_path = os.path.join(base_path, "configs",
                                        "user_configuration.json")
        configuration_data = parser.load_item_data_from_config(
            config_file_path)
        for items_data in configuration_data.values():
            for item_data in items_data:
                if item_data["name"] == name:
                    property_path = os.path.join(
                        base_path, "configs", item_data["property_json_name"])
                    return parser.load_item_data_from_config(property_path)
        return None
