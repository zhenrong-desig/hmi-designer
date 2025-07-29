from PyQt5 import QtWidgets
from PyQt5.QtGui import QBrush, QColor
from components.custom.graphicsScene import graphicsScene


class canvasView(QtWidgets.QGraphicsView):

    def __init__(self, scene=None, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.viewport().setAcceptDrops(True)
        scene = self.scene()
        if not scene:
            self.setScene(graphicsScene(self))
            view_width = self.viewport().width()
            view_height = self.viewport().height()
            self.scene().setSceneRect(0, 0, view_width, view_height)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        component_name = event.mimeData().text()
        button = QtWidgets.QPushButton(component_name)
        proxy = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(button)
        pos = event.pos()
        scene_pos = self.mapToScene(pos)
        proxy.setPos(scene_pos)
        self.scene().addItem(proxy)
        event.acceptProposedAction()
