import json
import pyinstaller_versionfile
import os.path

from src.config.vrb import cfg_config, version_file


class configue:
    def __init__(self):
        if not os.path.isfile(cfg_config):
            self.cfg = {
                "infos": {"nom": "Je suis un test de nommage",
                          "description": "Je suis un test de description",
                          "version": "0.0",
                          "auteur": "ZP6177",
                          "compagnie": "ZP6177"},
                "config": {"curseur": "TheR7angelo",
                           "theme": "defaut",
                           "font": "Berlin Sans FB Demi",
                           "widht": 1200,
                           "height": 800,
                           "opacity": 0.96},
                "variable": {"auto_reload": False}
            }
            with open(cfg_config, "w") as output:
                json.dump(self.cfg, output, indent=4)
            self.write_version_file()
        else:
            with open(cfg_config) as json_file:
                self.cfg = json.load(json_file)

    def write_version_file(self):
        pyinstaller_versionfile.create_versionfile(
            output_file=version_file,
            version=self.cfg["infos"]["version"],
            company_name=self.cfg["infos"]["compagnie"],
            file_description=self.cfg["infos"]["description"],
            internal_name=self.cfg["infos"]["nom"],
            legal_copyright="",  # "© My Imaginary Company. All rights reserved.",
            original_filename=f'{self.cfg["infos"]["nom"]}.exe',
            product_name=self.cfg["infos"]["nom"]
        )

    def get(self):
        return self.cfg

    def update(self, section: str, clef: str, valeur):
        """
        :param section: infos || config || variable
        :param clef: nom | description | version | auteur | compagnie || curseur | theme || auto_reload
        :param valeur: string || string || bool
        :return: None
        """
        with open(cfg_config, "r+") as output:
            self.cfg[section][clef] = valeur
            output.seek(0)
            json.dump(self.cfg, output, indent=4)
            output.truncate()

        self.write_version_file()
