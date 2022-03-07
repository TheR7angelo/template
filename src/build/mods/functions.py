import glob
import os
import pathlib
import shutil

from PySide6 import QtCore, QtGui

from src.config import config
from src.lib.palettes import *


class Functions:
    def __init__(self, **kwargs):

        self.kwargs = kwargs

    def CUR(self):

        cursor = {
            "Arrow": QtGui.QCursor(QtCore.Qt.ArrowCursor),
            "Busy": QtGui.QCursor(QtCore.Qt.BusyCursor),
            "CloseHand": QtGui.QCursor(QtCore.Qt.ClosedHandCursor),
            "DragCopy": QtGui.QCursor(QtCore.Qt.DragCopyCursor),
            "DragLink": QtGui.QCursor(QtCore.Qt.DragLinkCursor),
            "DragMove": QtGui.QCursor(QtCore.Qt.DragMoveCursor),
            "Forbidden": QtGui.QCursor(QtCore.Qt.ForbiddenCursor),
            "IBeam": QtGui.QCursor(QtCore.Qt.IBeamCursor),
            "OpenHand": QtGui.QCursor(QtCore.Qt.OpenHandCursor),
            "PointingHand": QtGui.QCursor(QtCore.Qt.PointingHandCursor),
            "SizeAll": QtGui.QCursor(QtCore.Qt.SizeAllCursor),
            "SizeBDiag": QtGui.QCursor(QtCore.Qt.SizeBDiagCursor),
            "SizeFDiag": QtGui.QCursor(QtCore.Qt.SizeFDiagCursor),
            "SizeHor": QtGui.QCursor(QtCore.Qt.SizeHorCursor),
            "SizeVer": QtGui.QCursor(QtCore.Qt.SizeVerCursor),
            "SplitH": QtGui.QCursor(QtCore.Qt.SplitHCursor),
            "SplitV": QtGui.QCursor(QtCore.Qt.SplitVCursor),
            "UpArrow": QtGui.QCursor(QtCore.Qt.UpArrowCursor),
            "Wait": QtGui.QCursor(QtCore.Qt.WaitCursor),
            "WhatsThis": QtGui.QCursor(QtCore.Qt.WhatsThisCursor)
        }
        cur = self.kwargs.get("cur")
        if cur[0] is None:
            cur = Cur().Arrow()
        elif ".ani" in cur[0]:
            cur = os.path.split(cur[0])[1].split(".")[0]
            return cursor[cur]
        return QtGui.QCursor(QtGui.QPixmap(cur[0]), cur[1], cur[2])

    def DIM(self):
        wg = self.kwargs.get("wg")
        if wg is None:
            return None

        w, h = self.kwargs.get("w"), self.kwargs.get("h")

        wg.setFixedWidth(w) if w is not None else False
        wg.setFixedHeight(h) if h is not None else False

    # def FONT(self):
    #     font = self.kwargs.get("font")
    #     if font is None: font = config.font
    #
    #     font_size = self.kwargs.get("font_size")
    #     if font_size is None: return
    #
    #     ft = QtGui.QFont()
    #     ft.setFamily(font)
    #     ft.setPointSize(font_size)
    #     return ft

    def GEN_SVG(self):
        hx1, hx2, hx3, hxbn1, hxbn2 = Rgb().hx_th1(), Rgb().hx_th2(), Rgb().hx_th3(), Rgb().hx_bn1(), Rgb().hx_bn2()
        ls_couleurs = [
            {"rgb_base": "#1D1D1B", "rgb_rep_th1": hx1, "rgb_rep_th2": hx2, "rgb_rep_th3": hx3, "rgb_rep_bn1": hxbn1, "rgb_rep_bn2": hxbn2},
            {"rgb_base": "#3C3C3B", "rgb_rep_th1": hx2, "rgb_rep_th2": hx1, "rgb_rep_th3": hx1, "rgb_rep_bn1": hx2, "rgb_rep_bn2": hx2},
            {"rgb_base": "#575756", "rgb_rep_th1": hx3, "rgb_rep_th2": hx3, "rgb_rep_th3": hx2, "rgb_rep_bn1": hx3, "rgb_rep_bn2": hx3},
            {"rgb_base": "#E30613", "rgb_rep_th1": hxbn1, "rgb_rep_th2": hxbn1, "rgb_rep_th3": hxbn1, "rgb_rep_bn1": hxbn1, "rgb_rep_bn2": hxbn1},
            {"rgb_base": "#00983A", "rgb_rep_th1": hxbn2, "rgb_rep_th2": hxbn2, "rgb_rep_th3": hxbn2, "rgb_rep_bn1": hxbn2, "rgb_rep_bn2": hxbn2}
        ]
        dct_rep_th = {
            "th1": "rgb_rep_th1",
            "th2": "rgb_rep_th2",
            "th3": "rgb_rep_th3",
            "bn1": "rgb_rep_bn1",
            "bn2": "rgb_rep_bn2"
        }

        liens_img = os.listdir("src/assets/img/")
        for lien_img in liens_img:
            lien = f"src/assets/img/{lien_img}/"
            lien_rgb = f"{lien}rgb"

            if not os.path.exists(lien_rgb):
                os.makedirs(lien_rgb)
            else:
                fichiers = glob.glob(f"{lien_rgb}/*")
                for fichier in fichiers:
                    os.remove(fichier)

            for svg in glob.glob(f"{lien}*.svg"):
                if "thc" not in svg:
                    for rep in dct_rep_th:
                        img_rgb_svg = f"{pathlib.Path(svg).stem}{rep}.svg"
                        shutil.copyfile(svg, f"{lien_rgb}/{img_rgb_svg}")

                        for couleur in ls_couleurs:
                            with open(f"{lien_rgb}/{img_rgb_svg}", "r+") as svgMod:
                                data = svgMod.read()

                                data = data.replace(couleur["rgb_base"], couleur[dct_rep_th[rep]])
                                svgMod.seek(0)
                                svgMod.write(data)
                else:
                    shutil.copyfile(svg, f"{lien_rgb}/{pathlib.Path(svg).stem[:-4]}.svg")
    # def ICON(self):
    #     wg, img, dim = self.kwargs.get("wg"), self.kwargs.get("img"), self.kwargs.get("dim")
    #     if wg is None or img is None or dim is None: return
    #
    #     icon = QtGui.QIcon()
    #     icon.addPixmap(QtGui.QPixmap(f"{img}.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
    #     wg.setIcon(icon)
    #     wg.setIconSize(QtCore.QSize(dim, dim))
    # def PIXMAP(self):
    #     wg, img, dim = self.kwargs.get("wg"), self.kwargs.get("img"), self.kwargs.get("dim")
    #     if wg is None or img is None or dim is None: return
    #
    #     wg.setPixmap(QtGui.QPixmap(f"{img}.svg"))
    #     wg.setScaledContents(True)
    # def RGB_HEX(self, rgb):
    #     return "#" + "%02x%02x%02x" % rgb
    # def HEX_RGB(self, hex_colors):
    #     rgb = hex_colors.lstrip('#')
    #     lv = len(rgb)
    #     return tuple(int(rgb[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    # def QACTION(self, slf, tray, ico, ico_rgb, txt, shortcut, fct, height):
    #     if height is None : height=12
    #
    #     tray.addAction(QtGui.QAction(slf, icon=QtGui.QPixmap(f"{ico}{ico_rgb}.svg").scaledToHeight(height), text=txt, shortcut=shortcut, triggered=fct))
    # def QSHORTCUT(self, slf, sht_1, sht_2, sht_3, fct):
    #     shortcut = int()
    #     if sht_1 is not None: shortcut += sht_1
    #     if sht_2 is not None: shortcut += sht_2
    #     if sht_3 is not None: shortcut += sht_3
    #
    #     QtGui.QShortcut(QtGui.QKeySequence(shortcut), slf).activated.connect(fct)