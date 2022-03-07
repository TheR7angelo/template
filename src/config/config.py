import json
import pyinstaller_versionfile
import os.path


class Configue:
    def __init__(self):
        if not os.path.isfile("src/config/config.json"):
            self.cfg = {
                "infos": {"nom": "Template",
                          "description": "Je suis un test de description",
                          "version": "0.1",
                          "auteur": "ZP6177",
                          "compagnie": "ZP6177"},
                "config": {"curseur": "TheR7angelo",
                           "theme": "default",
                           "font": "Berlin Sans FB Demi",
                           "widht": 1066,
                           "height": 600,
                           "opacity": 0.96},
                "variable": {"auto_reload": False}
            }
            with open("src/config/config.json", "w") as output:
                json.dump(self.cfg, output, indent=4)
            self.write_version_file()
        else:
            with open("src/config/config.json") as json_file:
                self.cfg = json.load(json_file)

    def write_version_file(self):
        pyinstaller_versionfile.create_versionfile(
            output_file="src/config/version_file.txt",
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
        with open("src/config/config.json", "r+") as output:
            self.cfg[section][clef] = valeur
            output.seek(0)
            json.dump(self.cfg, output, indent=4)
            output.truncate()

        self.write_version_file()

