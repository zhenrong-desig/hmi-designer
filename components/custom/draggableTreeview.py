from json.encoder import py_encode_basestring
from PyQt5 import QtWidgets
from PyQt5.QtCore import QMimeData
from PyQt5.QtGui import QDrag


class draggableTreview(QtWidgets.QTreeView):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragEnabled(True)
        self.setAcceptDrops(False)
        self.setDragDropMode(QtWidgets.QTreeView.DragOnly)
        self.drag_start_index = None

    def dragMoveEvent(self, event):
        event.accept()

    def mousePressEvent(self, event):
        index = self.indexAt(event.pos())
        if index.isValid():
            self.drag_start_index = index
        super().mousePressEvent(event)

    def startDrag(self, supportedActions):
        if not self.drag_start_index or not self.drag_start_index.isValid():
            return

        # 获取 mimeData，并设置文本数据
        mime_data = self.model().mimeData([self.drag_start_index])
        item = self.model().itemFromIndex(self.drag_start_index)
        item_name = item.text()  # 获取 item 的文本（如组件名称）
        mime_data.setText(item_name)  # 设置拖拽文本数据

        # 创建 QDrag 对象并设置 MIME 数据
        drag = QDrag(self)
        drag.setMimeData(mime_data)

        # 执行拖拽操作
        drag.exec_(supportedActions)
