import sys

from PySide6 import QtCore, QtWidgets, QtGui
from src.gui.mainWindow import Ui_mainWindow

class main(Ui_mainWindow, QtWidgets.QMainWindow):
    dragPos: QtCore.QPoint

    def __init__(self):
        super(main, self).__init__()

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.sizegrip = QtWidgets.QSizeGrip(self)
        self.win_state = QtCore.Qt.WindowNoState

        # self.tray = QtWidgets.QSystemTrayIcon(QtGui.QPixmap(ICO_MAIN), self)
        # self.tray_menu = QtWidgets.QMenu()
        # self.tray_menu.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setupUi(self)
        self.show()

# ICO_MAIN = f"{Img().main()}th2.svg"
app = QtWidgets.QApplication(sys.argv)
# splash = QtWidgets.QSplashScreen(QtGui.QPixmap(ICO_MAIN).scaledToHeight(400), QtCore.Qt.WindowStaysOnTopHint)
# splash.show()
app.processEvents()
#
fen = main()
# splash.finish(fen)
fen.show()
#
sys.exit(app.exec())