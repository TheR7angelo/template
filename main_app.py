import sys
import time

from PySide6 import QtCore, QtWidgets, QtGui

from src import *


class main(Ui_main, QtWidgets.QWidget):
    dragPos: QtCore.QPoint

    def __init__(self):
        super(main, self).__init__()

        ### AJOUTS DE BASE ###
            # size_grip
        self.size_grip = QtWidgets.QSizeGrip(self)

        #     # tray
        # self.tray = QtWidgets.QSystemTrayIcon(QtGui.QPixmap(f"{Img().main()}th3.svg"), self)
        # self.tray.activated.connect(self.trayActivate)
        # self.timer_double_click = QtCore.QTimer(self)
        # self.timer_double_click.setSingleShot(True)
        # self.timer_double_click.timeout.connect(self.traySingleClick)
        #     # tray_menu
        # self.tray_menu = QtWidgets.QMenu()
        # self.tray_menu.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        # ### VARIABLES DE BASES ###
        # self.win_state = QtCore.Qt.WindowNoState
        #
        ### FONCTIONS AU LANCEMENT ###
        self.setup(
            [self.in_base, "Configuration des éléments principaux"],
            [lambda: self.setupUi(self), "Initialisation de l'interface graphique"]
        )

        splash_screen.close()

    def in_base(self):
        ### Fenetre principal ###
        self.setWindowTitle(Configue().cfg["infos"]["nom"])
        self.setWindowIcon(QtGui.QPixmap(f"{Img().main()}th3.svg"))
        self.setWindowOpacity(Configue().cfg["config"]["opacity"])
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #self.e_resize_screen()

    def setup(self, *args):
        for fct in args:
            splash_screen.lb_chargement.setText(fct[1])
            splash_screen.pg_chargement.setValue((splash_screen.pg_chargement.value() + 100 / len(args)) - 1)

            fct[0]()
            time.sleep(2)

        splash_screen.lb_chargement.setText("Lancement de l'application")
        splash_screen.pg_chargement.setValue(100)
        time.sleep(2)

        #
        # ### CREATION DES EVENT ###
        # self.evt = Event(self)
        # self.mousePressEvent = self.evt.mousePressEvent
        # self.mouseDoubleClickEvent = self.evt.mouseDoubleClickEvent
        # self.mouseMoveEvent = self.evt.mouseMoveEvent
        # self.mouseReleaseEvent = self.evt.mouseReleaseEvent

if __name__ == "__main__":

    Configue().update(section="variable", clef="auto_reload", valeur=False)
    # Configue().update(section="config", clef="opacity", valeur=15)

    Functions().GEN_SVG()

    app = QtWidgets.QApplication(sys.argv)

    splash_screen = SplashScreen()
    splash_screen.open()

    app.processEvents()

    fen = main()
    fen.show()

    sys.exit(app.exec())
