from src.build.palettes.data.data import Data

class Dim(Data):
    def __init__(self, grp="dimension"):
        super().__init__(grp)

    def h0(self):
        return self.get_val("h0")
    def h1(self):
        return self.get_val("h1")
    def h2(self):
        return self.get_val("h2")
    def h3(self):
        return self.get_val("h3")
    def h4(self):
        return self.get_val("h4")
    def h5(self):
        return self.get_val("h5")
    def h6(self):
        return self.get_val("h6")
    def h7(self):
        return self.get_val("h7")
    def h8(self):
        return self.get_val("h8")
    def h9(self):
        return self.get_val("h9")
    def h10(self):
        return self.get_val("h10")
