from PySide6.QtCore import QRect
from PySide6.QtGui import QColor, QPainter, QPen, QFont, Qt
from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QProgressBar


class PyCircularProgress(QProgressBar):

    def __init__(self, shadow=None, value=0,
                 width=0, height=0, progress_width=10,
                 progress_rounded_cap=True, progress_color=0x498BD1, max_value=100,
                 font_family="Segoe UI", font_size=12, suffix='%',
                 text_color=0x498BD1, enable_shadow=True):

        QWidget.__init__(self)

        # CUSTOM PROPERTY
        self.shadow = shadow
        self.value = value
        self.width = width
        self.height = height
        self.progress_width = progress_width
        self.progress_rounded_cap = progress_rounded_cap
        self.progress_color = progress_color
        self.max_value = max_value
        self.font_family = font_family
        self.font_size = font_size
        self.suffix = suffix
        self.text_color = text_color
        self.enable_shadow = enable_shadow

        # DEFAULT SIZE VALUE WITHOUT LAYOUT
        self.resize(self.width, self.height)

    # ADD SHADOW
    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 120))
            self.setGraphicsEffect(self.shadow)

    # SET VALUE
    def set_value(self, value):
        self.value = value
        self.repaint()

    # PAINT EVENT
    def paintEvent(self, event):
        # SET PROGRESS PARAMETER
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value

        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(Qt.NoPen)
        p.setFont(QFont(self.font_family, self.size))

        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width, self.height)
        p.drawRect(rect)

        # PEN
        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)

        # SET ROUND CAP
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # CREATE ARC / CIRCULAR PROGRESS
        p.setPen(pen)
        p.drawArc(margin, margin, width, height, -90 * 16, -value * 16)

        pen.setColor(QColor(self.text_color))
        p.setPen(pen)
        p.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")

        # END
        p.end()
