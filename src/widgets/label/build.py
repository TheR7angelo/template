from PySide6 import QtGui

from src.build.mods import Functions
from src.lib.palettes import *
from src.widgets import vb_wg


class Build:
    def __init__(
            self,
            *wgs,

            # Dimensions
            width=None,
            height=None,

            # Police
            font=vb_wg.font,
            font_size=vb_wg.font_size,

            # Paramètres
            align_horizontal=Align().left(),
            align_vertical=Align().v_center(),
            focus_policy=vb_wg.focus_policy,
            frame_shape=vb_wg.frame_shape,
            frame_shadow=vb_wg.frame_shadow,
            indent=5,
            line_width=0,
            open_external_link=False,
            scaled_contents=True,
            text_format=vb_wg.text_format,
            word_wrap=vb_wg.word_wrap,

            # Curseur
            cursor=vb_wg.cur,

            # Couleurs BG
            bg=vb_wg.bg,
            bg_hover=vb_wg.bg_hover,
            # Couleurs FG
            fg=vb_wg.fg,
            fg_hover=vb_wg.fg_hover,

            # Images
            img=None,
            # Images RGB
            img_rgb=vb_wg.img_unchecked,

            # Positions WG
            margin=(0,) * 4,
            padding=(0,) * 4,

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
        *Align: QtCore.Qt : Align().%nomAlign() \n
        *Border_Style: str() : dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none \n
        *Cur: list() : Cur().%nomCurseur() \n
        *Dim: int() : Dim().%nomDim() \n
        *FocusPolicy: QtCore.Qt : FocusPolicy().%nomFocus \n
        *Font: int() : Font().%nomFont() \n
        *Img: str() : Img().%nomImage() \n
        *Img_rgb: str() : th1 | th2 | th3 | bn1 | bn2 \n
        *Rgb: tuple() : Rgb().%nomCouleur() \n
        *FrameShape: QtWidgets.QFrame : FrameShape().%nomFrameForme \n
        *FrameShadow: QtWidgets.QFrame : FrameShadow().%nomFrameOmbre \n
        *TextFormat: QtCore.Qt : TextFormat().%nomFormat() \n
        *Tuple: tuple() : (int(), int(), int(), int()) == (Top, Bottom, Right, Left) | (TopRight, TopLeft, BottomRight, BottomLeft) \n

        :param wgs: Widgets séparés par ","
        :param width: *Dim
        :param height: *Dim
        :param font: str()
        :param font_size: *Font
        :param align_horizontal: *Align
        :param align_vertical: *Align
        :param focus_policy: *FocusPolicy
        :param frame_shape: *FrameShape
        :param frame_shadow: *FrameShadow
        :param indent: int()
        :param line_width: int()
        :param open_external_link: bool()
        :param scaled_contents: bool()
        :param text_format: *TextFormat
        :param word_wrap: bool()
        :param cursor: *Cur
        :param bg: *Rgb
        :param bg_hover: *Rgb
        :param fg: *Rgb
        :param fg_hover: *Rgb
        :param img: *Img
        :param img_rgb: *Img_rgb
        :param margin: *Tuple
        :param padding: *Tuple
        :param border: *Tuple
        :param border_style: *Border_Style
        :param border_rgb: *Rgb
        :param border_hover: *Tuple
        :param border_hover_style: *Border_Style
        :param border_hover_rgb: *Rgb
        :param radius: *Tuple
        """

        style = f"""
                /* LABEL */
                .QLabel {{
                background-color: rgba{bg};
                color: rgba{fg};
                margin-top: {margin[0]}px;
                margin-bottom: {margin[1]}px;
                margin-right: {margin[2]}px;
                margin-left: {margin[3]}px;
                padding-top: {padding[0]}px;
                padding-bottom: {padding[1]}px;
                padding-right: {padding[2]}px;
                padding-left: {padding[3]}px;
                }}
                .QLabel:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}

                /* BORDURES */
                .QLabel {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QLabel:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}

                /* RAYONS */
                .QLabel {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""
        for wg in wgs:
            # Dimensions
            Functions().SET_DIM(wg, width=width, height=height)

            # Police
            Functions().SET_FONT(wg, font=font, font_size=font_size)

            # Paramètres
            wg.setAlignment(align_horizontal | align_vertical)
            wg.setFocusPolicy(focus_policy)
            wg.setFrameShape(frame_shape)
            wg.setFrameShadow(frame_shadow)
            wg.setIndent(indent)
            wg.setLineWidth(line_width)
            wg.setOpenExternalLinks(open_external_link)
            if img is not None:
                wg.setPixmap(QtGui.QPixmap(f"{img}{img_rgb}.svg"))
                wg.setScaledContents(scaled_contents)
            wg.setTextFormat(text_format)
            wg.setWordWrap(word_wrap)

            # Curseur
            # wg.setCursor(Functions().SET_CURSOR(cursor))

            # Style
            wg.setStyleSheet(style)
