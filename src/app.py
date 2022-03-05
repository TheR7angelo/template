import sys
import time

from PySide6 import QtCore, QtWidgets, QtGui

from src.config import *
from src.gui import *
from src.build import *

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

        self.tray = QtWidgets.QSystemTrayIcon(QtGui.QPixmap(ico_logo), self)
        self.tray_menu = QtWidgets.QMenu()
        self.tray_menu.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setupUi(self)

        self.setup()

    def setup(self, *args):

        self.setCursor(Fct(cur=Cur().wait()).CUR())

        # for fct in args:
        #     splash_screen


ico_logo = f"{Img().main()}.svg"
app = QtWidgets.QApplication(sys.argv)

app.processEvents()
#
fen = main()
# splash_screen = SplashScreen()
# splash_screen.open()
fen.show()
#
sys.exit(app.exec())