import os.path

from src.config import *


class Cur:
    # def __init__(self):

    # self.dct = {
    #     "agrandir": self.agrandir,
    #     "copier": self.copier,
    #     "crayon": self.crayon,
    #     "croix": self.croix,
    #     "fleche_nesw": self.fleche_nesw,
    #     "fleche_ns": self.fleche_ns,
    #     "fleche_nwse": self.fleche_nwse,
    #     "fleche_top": self.fleche_top,
    #     "fleche_tout": self.fleche_tout,
    #     "fleche_we": self.fleche_we,
    #     "IBeam": self.IBeam,
    #     "infos": self.infos,
    #     "main": self.main,
    #     "non": self.non,
    #     "retour": self.retour,
    #     "souris": self.souris,
    #     "souris_main": self.souris_main,
    #     "souris_non": self.souris_non,
    #     "wait": self.wait,
    # }

    def CUR(self, img):
        curseur = f"src/assets/cursor/{Configue().cfg['config']['curseur']}/{img}"
        return next(
            (
                f"{curseur}{ext}"
                for ext in [".cur", ".ani"]
                if os.path.exists(f"{curseur}{ext}")
            ),
            None,
        )

    # def RTN_CUR(self, cur="souris"):
    #     return self.dct.get(cur)()

    def agrandir(self):
        return [self.CUR("agrandir"), 9, 1]

    def DragCopy(self):
        return [self.CUR("DragCopy"), 9, 1]

    def crayon(self):
        return [self.CUR("crayon"), 1, 32]

    def Cross(self):
        return [self.CUR("Cross"), 16, 16]

    def SizeBDiag(self):
        return [self.CUR("SizeBDiag"), 16, 16]

    def SizeVer(self):
        return [self.CUR("SizeVer"), 16, 16]

    def SizeFDiag(self):
        return [self.CUR("SizeFDiag"), 16, 16]

    def UpArrow(self):
        return [self.CUR("UpArrow"), 16, 1]

    def SizeAll(self):
        return [self.CUR("SizeAll"), 16, 16]

    def SizeHor(self):
        return [self.CUR("SizeHor"), 16, 16]

    def IBeam(self):
        return [self.CUR("IBeam"), 16, 16]

    def WhatsThis(self):
        return [self.CUR("WhatsThis"), 9, 1]

    def PointingHand(self):
        return [self.CUR("PointingHand"), 9, 1]

    def CloseHand(self):
        return [self.CUR("CloseHand")]

    def Forbidden(self):
        return [self.CUR("Forbidden"), 16, 16]

    def retour(self):
        return [self.CUR("retour"), 9, 1]

    def Arrow(self):
        return [self.CUR("Arrow"), 9, 1]

    def souris_main(self):
        return [self.CUR("souris_main"), 9, 1]

    def souris_non(self):
        return [self.CUR("souris_non"), 9, 1]

    def Wait(self):
        return [self.CUR("Wait"), 16, 16]
