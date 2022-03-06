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

        self.setup(
            [self.setup_test, "test"]
        )
        splash_screen.close()

    def setup_test(self):
        print("test")

    def setup(self, *args):

        self.setCursor(Fct(cur=Cur().Arrow()).CUR())

        for fct in args:
            splash_screen.lb_chargement.setText(fct[1])
            splash_screen.pg_chargement.setValue(splash_screen.pg_chargement.value() + 100 / len(args))

            fct[0]()

        splash_screen.lb_chargement.setText("Lancement de l'application")
        splash_screen.pg_chargement.setValue(100)
        time.sleep(10)


ico_logo = f"{Img().main()}.svg"
app = QtWidgets.QApplication(sys.argv)

splash_screen = SplashScreen()
splash_screen.open()

app.processEvents()

fen = main()
fen.show()

sys.exit(app.exec())
