from PySide6 import QtCore, QtWidgets, QtGui

from src.gui.ui.splashScreen import splash_screen
from src.config import *
from src.build import *
from src.lib import *


class SplashScreen(splash_screen.Ui_SplashScreen, QtWidgets.QDialog):
    def __init__(self):
        super(SplashScreen, self).__init__()

        self.width = 600
        self.height = 400
        self.opacity = 1

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.setupUi(self)
        self.INIT()


    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        # Fenetre
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setWindowOpacity(self.opacity)

        self.fr_main.setStyleSheet("""
                                    .QFrame{
                                    background-color: rgba(255, 151, 75, 200);
                                    }
                                    """)

        self.lb_chargement.setAlignment(QtCore.Qt.AlignCenter)



        self.pg_chargement.setAlignment(QtCore.Qt.AlignCenter)

    def IN_CLASSE(self):
    #     ### QFrame ###
    #     Frame.SplashScreen(self.fr_main)
    #     ### /QFrame ###
    #
    #
    #     ### QLabel ###



        pass


    #     Label.Base_tr(self.lb_titre, font_size=Font().h3())
    #     Label.Base_tr(self.lb_description, self.lb_chargement, font_size=Font().h5())
    #     ### /QLabel ###
    #
    #
    #     ### QProgressBar ###
    #     ProgressBar.Chargement(self.pg_chargement)
    #     ### /QProgressBar ###
    def IN_WG(self):
        # Base
        self.setCursor(Functions(cur=Cur().Wait()).CUR())

        # Icone de l'app
        dim = Dim().h5()
        Functions().SET_DIM(self.lb_ico, width=dim, height=dim)
        self.lb_ico.setPixmap(QtGui.QPixmap("src/assets/img/main/inari_thc.svg"))
        self.lb_ico.setScaledContents(True)

        self.lb_titre.setText(Configue().cfg["infos"]["nom"])
        self.lb_description.setText(Configue().cfg["infos"]["description"])
    def IN_CONNECTIONS(self):
        pass
    def IN_ACT(self):
        pass
    def IN_WG_BASE(self):
        pass
    def INIT(self):
        self.IN_BASE()
        self.IN_CLASSE()
        self.IN_WG()
        self.IN_CONNECTIONS()
        self.IN_ACT()
        self.IN_WG_BASE()
    ############################
    ##    /INITIALISATION     ##
    ############################
