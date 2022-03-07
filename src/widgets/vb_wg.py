from src.config.config import Configue
from src.lib.palettes import *


########################
##     DIMENSIONS     ##
########################
WIDTH = None
HEIGHT = Dim().h9()


####################
##     POLICE     ##
####################
font = Configue().cfg["config"]["font"]
font_size = Font().h4()
font_size_HD = Font().h3()


########################
##     PARAMETRES     ##
########################
# BUTTON_SYMBOLS = ButtonSymbols().plus_minus()
# DRAG_DROP_MODE = DragDropMode().no_drag()
# DROP_ACTION = DropAction().move()
edit = False
focus_policy = FocusPolicy().strong_focus()
frame_shape = FrameShape().no_frame()
frame_shadow = FrameShadow().plain()
insert_policy = InsertPolicy().insert_bottom()
max_visible_items = 10
no_focus = False
# SELECTION_BEHAVIOR = SelectionBehavior().row()
# SELECTION_MODE = SelectionMode().single()
text_visible = True
val_min = 0
val_max = 100
val_step = 1
# TEXT_FORMAT = TextFormat().plain()
word_wrap = True


#####################
##     CURSEUR     ##
#####################
cur = Cur().Arrow()
cur_main = Cur().PointingHand()
cur_view = Cur().souris_main()
cur_viewport = Cur().Cross()
cur_le = Cur().IBeam()


######################
##     COULEURS     ##
######################
    # BG
bg = Rgb().th3()
bg_alternate = Rgb().th2()
bg_hover = Rgb().th3()
bg_checked = Rgb().th1()
bg_checked_hover = Rgb().th1()
bg_indeterminate = Rgb().th2()
bg_indeterminate_hover = Rgb().th2()
bg_pressed = Rgb().th3()
bg_checked_pressed = Rgb().th1()
bg_selection = Rgb().th1()
    # BG item
bg_item = Rgb().th3()
bg_item_hover = Rgb().th3()
bg_item_checked = Rgb().th1()
bg_item_checked_hover = Rgb().th1()
    # BG Autres
bg_chunk = Rgb().th2()
bg_chunk_hover = Rgb().bn1()
bg_groove = Rgb().th3()
bg_groove_hover = Rgb().th3()
bg_groove_pressed = Rgb().th3()
bg_handle = Rgb().th2()
bg_handle_hover = Rgb().th2()
bg_handle_pressed = Rgb().bn1()
bg_separator = Rgb().bn1()

    # FG
fg = Rgb().th1()
fg_hover = Rgb().bn1()
fg_checked = Rgb().th3()
fg_checked_hover = Rgb().bn1()
fg_indeterminate = Rgb().th3()
fg_indeterminate_hover = Rgb().th1()
fg_pressed = Rgb().bn1()
fg_checked_pressed = Rgb().bn2()
fg_selection = Rgb().th3()
fg_placeholder = Rgb().th2()
    # FG item
fg_item = Rgb().th1()
fg_item_hover = Rgb().bn1()
fg_item_checked = Rgb().th3()
fg_item_checked_hover = Rgb().bn1()

    # Autres
gridline = Rgb().th2()


####################
##     IMAGES     ##
####################
    # Check
img_unchecked = Img().check0()
img_unchecked_HOVER = Img().check0()
img_checked = Img().check2()
img_checked_hover = Img().check2()
img_indeterminate = Img().check1()
img_indeterminate_hover = Img().check1()
img_unroll = Img().fleche_bottom()
img_unroll_hover = Img().fleche_bottom()
    # Check RGB
img_UNCHECK_RGB = "th2"
img_UNCHECK_HOVER_RGB = "bn1"
img_CHECK_RGB = "th2"
img_CHECK_HOVER_RGB = "bn1"
img_INDETERMINATE_RGB = "th3"
img_INDETERMINATE_HOVER_RGB = "th1"
img_UNROLL_RGB = "th2"
img_UNROLL_HOVER_RGB = "bn1"

    # Fleches
img_UP = Img().plus()
img_DOWN = Img().moins()
img_RIGHT = Img().fleche_droite()
img_LEFT = Img().fleche_gauche()
    # Fleches RGB
img_UP_RGB = "th2"
img_DOWN_RGB = "th2"
img_RIGHT_RGB = "th3"
img_LEFT_RGB = "th3"

    # img dim
img_width = HEIGHT * StyleBase().x_ico()
IMG_WIDTH = HEIGHT * StyleBase().X_ICO()
img_height = HEIGHT * StyleBase().x_ico()
IMG_HEIGHT = HEIGHT * StyleBase().X_ICO()


#####################
##     BORDURE     ##
#####################
BORDER_WIDTH = (0,) * 4
BORDER_STYLE = "solid"
BORDER_RGB = Rgb().tr()


###################
##     RAYON     ##
###################
RADIUS_SIZE = 3
RADIUS = (RADIUS_SIZE,) * 4


####################
##     SCROLL     ##
####################
SCROLL_BG = Rgb().th1()
SCROLL_WIDTH = 10
SCROLL_HEIGHT = 10

SCROLL_HANDLE_BG = Rgb().th3()
SCROLL_HANDLE_BG_HOVER = Rgb().th3()
SCROLL_HANDLE_FG = Rgb().th2()
SCROLL_HANDLE_FG_HOVER = Rgb().bn1()
SCROLL_HANDLE_MIN_WIDTH = 20
SCROLL_HANDLE_MIN_HEIGHT = 20

SCROLL_H = Scroll().need()
SCROLL_V = Scroll().need()
HEADER_H = True
HEADER_V = True
