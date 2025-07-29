from PyQt5 import QtWidgets


class graphicsScene(QtWidgets.QGraphicsScene):

    def dragMoveEvent(self, event):
        event.setAccepted(True)
