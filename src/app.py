import sys
import time

from PySide6 import QtCore, QtWidgets, QtGui

from src.config import *

from src.gui.mainWindow import Ui_mainWindow

class main(Ui_mainWindow, QtWidgets.QMainWindow):
    dragPos: QtCore.QPoint

    def __init__(self):
        super(main, self).__init__()

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowIcon(QtGui.QPixmap(ico_logo))

        self.sizegrip = QtWidgets.QSizeGrip(self)
        self.win_state = QtCore.Qt.WindowNoState

        # self.tray = QtWidgets.QSystemTrayIcon(QtGui.QPixmap(ICO_MAIN), self)
        # self.tray_menu = QtWidgets.QMenu()
        # self.tray_menu.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setupUi(self)
        self.show()

# ico_logo = f"{Img().main()}th2.svg"
ico_logo = f"{variable_base.do_img_logo}/logo.svg"
app = QtWidgets.QApplication(sys.argv)
splash = QtWidgets.QSplashScreen(QtGui.QPixmap(ico_logo).scaledToHeight(400), QtCore.Qt.WindowStaysOnTopHint)
splash.show()
time.sleep(5)
app.processEvents()
#
fen = main()
splash.finish(fen)
fen.show()
#
sys.exit(app.exec())