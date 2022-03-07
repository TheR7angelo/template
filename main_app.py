import sys
import time

from PySide6 import QtCore, QtWidgets, QtGui

from src import *


class main(Ui_main, QtWidgets.QWidget):
    dragPos: QtCore.QPoint

    def __init__(self):
        super(main, self).__init__()
        self.cfg = Configue().get()

        ### AJOUTS DE BASE ###
            # size_grip
        self.size_grip = QtWidgets.QSizeGrip(self)

            # tray
        self.tray = QtWidgets.QSystemTrayIcon(QtGui.QPixmap(f"{Img().main()}th3.svg"), self)
        # self.tray.activated.connect(self.trayActivate)
        # self.timer_double_click = QtCore.QTimer(self)
        # self.timer_double_click.setSingleShot(True)
        # self.timer_double_click.timeout.connect(self.traySingleClick)
            # tray_menu
        self.tray_menu = QtWidgets.QMenu()
        self.tray_menu.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ### VARIABLES DE BASES ###
        self.win_state = QtCore.Qt.WindowNoState

        ### FONCTIONS AU LANCEMENT ###
        self.setup(
            [self.in_base, "Configuration des éléments principaux"],
            [lambda: self.setupUi(self), "Initialisation de l'interface graphique"],
            [self.in_classe, "Application du theme"],
            [self.in_wg, "Configuration de base des Widgets"]
        )

        splash_screen.close()

    def in_base(self):
        ### Fenetre principal ###
        self.setWindowTitle(self.cfg["infos"]["nom"])
        self.setWindowIcon(QtGui.QPixmap(f"{Img().main()}th3.svg"))
        self.setWindowOpacity(self.cfg["config"]["opacity"])
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #self.e_resize_screen()

    def in_wg(self):
        ### Base ###
        self.setCursor(Functions(cur=Cur().Arrow()).CUR())


        ### Nom de l'app ###
        self.lb_mt_nom.setText(self.cfg["infos"]["nom"])


        ### Widget blanc pour centrer le nom de l'app ###
        dim = Dim().h9() * 1.4
        Functions().SET_DIM(self.wg_mt_blank, width=dim*3, height=dim)


        ### Version de l'app ###
        self.lb_mb_version.setText(f" Version : {self.cfg['infos']['version']}")


        ### size_grip ###
        if True: # config.resize:
            self.size_grip.setCursor(Functions(cur=Cur().SizeFDiag()).CUR())
            self.size_grip.setStyleSheet(
                f"""
                QSizeGrip {{
                image: url({Img().resize()}th3.svg);
                width: {Dim().h10()}px;
                height: {Dim().h10()}px;
                }}
                """
            )
            self.hlay_menu_bottom.addWidget(self.size_grip)

    def in_classe(self):

        ### QFrame ###
        frame.Menu(self.fr_menu_top).top()
        frame.Cadre(self.fr_main, shadow=Shadow().ombre_portee(self)).th2()
        frame.Menu(self.fr_menu_bottom).bottom()
        ### /QFrame ###

        ### QLabel ###
        label.Base(self.lb_mt_ico).ico_main()
        label.Base(self.lb_mt_nom, font_size=Font().h3()).tr()
        label.Base(self.lb_mb_version).tr()
        ### \QLabel ###

    def in_tray(self):
        ### Actions ###
        Functions.ADD_QACTION(
            self,
            tray=self.tray_menu,
            ico=Img().quitter(),
            ico_rgb="bn2",
            txt="Quitter",
            shortcut_txt="Shift+Esc",
            status_tip="Quitter",
            fct=self.e_quitter_tray,
            sht_1=Keys().shift(),
            sht_2=Keys().escape()
        )

        # self.tray_menu.addSeparator()

        self.tray.setContextMenu(self.tray_menu)
        self.tray.show()

    def setup(self, *args):

        for fct in args:
            splash_screen.lb_chargement.setText(fct[1])
            splash_screen.pg_chargement.setValue((splash_screen.pg_chargement.value() + 100 / len(args)) - 1)

            fct[0]()
            time.sleep(2)

        splash_screen.lb_chargement.setText("Lancement de l'application")
        splash_screen.pg_chargement.setValue(100)
        time.sleep(2)

    def e_quitter_tray(self):
        self.show()
        fen.activateWindow()

        if fen.windowState() == QtCore.Qt.WindowMinimized:
            fen.setWindowState(QtCore.Qt.WindowActive)

        # if DLG_Rep().QUITTER():
        #     self.ui.app.quit()
        app.quit()
    #####
    def closeEvent(self, event):
        event.accept()
        app.quit()

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
