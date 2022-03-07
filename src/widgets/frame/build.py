from src.build.mods import Functions
from src.lib.palettes import *
from src.widgets import vb_wg, vb_app


class Build:
    def __init__(
            self,
            *wgs,

            # Dimensions
            width=vb_app.WIDTH,
            height=vb_app.HEIGHT,

            # Paramètres
            focus_policy=vb_wg.focus_policy,
            frame_shape=vb_wg.frame_shape,
            frame_shadow=vb_wg.frame_shadow,
            line_width=0,
            shadow=None,

            # Curseur
            cursor=Cur().Arrow(),

            # Couleurs BG
            bg=vb_wg.bg,

            # Bordures
            border=vb_wg.BORDER_WIDTH,
            border_style=vb_wg.BORDER_STYLE,
            border_rgb=vb_wg.BORDER_RGB,
            # Bordures hover
            border_hover=vb_wg.BORDER_WIDTH,
            border_hover_style=vb_wg.BORDER_STYLE,
            border_hover_rgb=vb_wg.BORDER_RGB,

            # Rayons
            radius=vb_wg.RADIUS,
    ):
        """
        *Border_Style: str() : dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none \n
        *Cur: list() : Cur().%nomCurseur() \n
        *Dim: int() : Dim().%nomDim() \n
        *FocusPolicy: QtCore.Qt : FocusPolicy().%nomFocus \n
        *Rgb: tuple() : Rgb().%nomCouleur() \n
        *Shadow: QtWidgets.QGraphicsDropShadowEffect(self) : Shadow().%nomOmbre() \n
        *FrameShape: QtWidgets.QFrame : FrameShape().%nomFrameForme \n
        *FrameShadow: QtWidgets.QFrame : FrameShadow().%nomFrameOmbre \n
        *Tuple: tuple() : (int(), int(), int(), int()) == (Top, Bottom, Right, Left) | (TopRight, TopLeft, BottomRight, BottomLeft) \n

        :param wgs: wgs: Widgets séparés par ","
        :param width: *Dim
        :param height: *Dim
        :param focus_policy: *FocusPolicy
        :param frame_shape: *FrameShape
        :param frame_shadow: *FrameShadow
        :param line_width: int()
        :param shadow: *Shadow
        :param cursor: *Cur
        :param bg: *Rgb
        :param border: *Tuple
        :param border_style: *Border_Style
        :param border_rgb: *Rgb
        :param border_hover: *Tuple
        :param border_hover_style: *Border_Style
        :param border_hover_rgb: *Rgb
        :param radius: *Tuple
        """

        style = f"""
                /* FRAME */
                .QFrame {{
                background-color: rgba{bg};
                }}

                /* BORDURES */
                .QFrame {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QFrame:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}

                /* RAYONS */
                .QFrame {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""
        for wg in wgs:
            # Dimensions
            Functions().SET_DIM(wg, width=width, height=height)

            # Paramètres
            wg.setFocusPolicy(focus_policy)
            wg.setFrameShape(frame_shape)
            wg.setFrameShadow(frame_shadow)
            wg.setLineWidth(line_width)
            if shadow is not None: wg.setGraphicsEffect(shadow)

            # Curseur
            wg.setCursorFunctions(cur=Cur().Arrow()).CUR()

            # Style
            wg.setStyleSheet(style)
