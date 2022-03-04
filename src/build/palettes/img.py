from src.config import variable_base


class Img:

    def SVG(self, val, img):
        return f"{variable_base.do_img}/{val}/theme/{img}"

    def main(self):
        return self.SVG(val="logo", img="logo")
