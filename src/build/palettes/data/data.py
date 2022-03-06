import json

from src.config import variable_base, config


class Data:

    def __init__(self, grp=""):
        self.grp = grp

    def open_json(self, fichier_json):
        with open(fr"{fichier_json}.json", "r") as fichier:
            return json.load(fichier)

    def get_val(self, val):
        js = self.open_json(fichier_json=f"{variable_base.do_data}/{self.grp}")
        return js.get(val)

    def th(self, val):
        dt = self.open_json(fichier_json=f"{variable_base.do_themes}/{config.configue().cfg['config']['theme']}")
        return tuple(dt[val])

    def th_hex(self, rgb):
        return f"#{'%02x%02x%02x' % rgb}"
