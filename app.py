import sys

from PyQt5 import QtGui, QtWidgets


class Window(QtGui.QWindow):
    def __init__(self):
        QtGui.QWindow.__init__(self)
        self.setGeometry(0, 0, 500, 500)
        self.setTitle('Test')


if __name__ == '__main__':
    import sys

    app = QtGui.QGuiApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
