from PySide6 import QtCore, QtWidgets, QtGui

from src.gui.dialog.interface import splash_screen_ui
from src.build import *
from src.config import *
from src.build.functions import Img


class SplashScreen(splash_screen_ui.Ui_SplashScreen, QtWidgets.QDialog):
    def __init__(self):
        super(SplashScreen, self).__init__()

        self.width = 600
        self.height = 400
        self.opacity = 1

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
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
    # def IN_CLASSE(self):
    #     ### QFrame ###
    #     Frame.SplashScreen(self.fr_main)
    #     ### /QFrame ###
    #
    #
    #     ### QLabel ###
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
        self.setCursor(Fct(cur=Cur().Wait()).CUR())

        # Icone de l'app
        dim = Dim().h5()
        # Fct(wg=self.lb_ico, w=dim, h=dim).DIM()
        self.lb_ico.setPixmap(QtGui.QPixmap(f"{variable_base.do_img_logo}/inari.svg"))
        self.lb_ico.setFixedWidth(200)
        self.lb_ico.setFixedHeight(200)

        self.lb_ico.setScaledContents(True)

        self.lb_titre.setText(config.configue().cfg["infos"]["nom"])
        self.lb_description.setText(config.configue().cfg["infos"]["description"])
    def IN_CONNECTIONS(self):
        pass
    def IN_ACT(self):
        pass
    def IN_WG_BASE(self):
        pass
    def INIT(self):
        self.IN_BASE()
        # self.IN_CLASSE()
        self.IN_WG()
        self.IN_CONNECTIONS()
        self.IN_ACT()
        self.IN_WG_BASE()
    ############################
    ##    /INITIALISATION     ##
    ############################
