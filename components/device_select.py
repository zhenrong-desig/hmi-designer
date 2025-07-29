import os
import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QStandardItem, QStandardItemModel


class device_select(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("components/ui/device_select.ui", self)
        self.treeView = self.findChild(QtWidgets.QTreeView, "treeView")
        self.model = QStandardItemModel()
        plc_item = QStandardItem("PLC")
        meter_item = QStandardItem("仪表")
        frequency_converter_item = QStandardItem("变频器")
        model_item = QStandardItem("模块类")

        plc_siemens = QStandardItem("西门子")
        plc_omron = QStandardItem("欧姆龙")
        plc_ab = QStandardItem("AB")
        plc_ge = QStandardItem("GE")
        plc_lg = QStandardItem("LG")
        plc_mitsubishi = QStandardItem("三菱")
        plc_koyo = QStandardItem("光洋")
        plc_delta = QStandardItem("台达")
        plc_hollysys = QStandardItem("和利时")
        plc_kazuzen = QStandardItem("和泉")
        plc_keyence = QStandardItem("基恩士")
        plc_fuji = QStandardItem("富士")
        plc_matsushita = QStandardItem("松下")
        plc_yonghong = QStandardItem("永宏")
        plc_aimosheng = QStandardItem("艾默生")
        plc_modikang = QStandardItem("莫迪康")
        plc_item.appendRows([
            plc_siemens, plc_omron, plc_ab, plc_ge, plc_lg, plc_mitsubishi,
            plc_koyo, plc_delta, plc_hollysys, plc_kazuzen, plc_keyence,
            plc_fuji, plc_matsushita, plc_yonghong, plc_aimosheng, plc_modikang
        ])

        meter_yuguang = QStandardItem("宇光仪表")
        meter_shanwu = QStandardItem("山武仪表")
        meter_oulu = QStandardItem("欧陆仪表")
        meter_hongrun = QStandardItem("虹润仪表")
        meter_item.appendRows(
            [meter_yuguang, meter_shanwu, meter_oulu, meter_hongrun])

        frequency_converter_mitsubishi = QStandardItem("三菱")
        frequency_converter_dongyuan = QStandardItem("东元")
        frequency_converter_danfusi = QStandardItem("丹佛斯")
        frequency_converter_taida = QStandardItem("台达")
        frequency_converter_anchuan = QStandardItem("安川")
        frequency_converter_siemens = QStandardItem("西门子")
        frequency_converter_item.appendRows([
            frequency_converter_mitsubishi, frequency_converter_dongyuan,
            frequency_converter_danfusi, frequency_converter_taida,
            frequency_converter_anchuan, frequency_converter_siemens
        ])

        model_hongge = QStandardItem("泓格")
        model_yanhua = QStandardItem("研华")
        model_item.appendRows([model_hongge, model_yanhua])

        self.model.appendRow(plc_item)
        self.model.appendRow(meter_item)
        self.model.appendRow(frequency_converter_item)
        self.model.appendRow(model_item)
        self.treeView.setModel(self.model)
