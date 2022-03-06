import psutil

from src.config import *
from src.build import *

import os
import time


if __name__ == "__main__":
    run = False

    config.configue().update(section="variable", clef="auto_reload", valeur=False)

    for proc in psutil.process_iter():
        pi = proc.as_dict(attrs=["pid", "name"])
        if pi["name"] == f"{config.configue().cfg['infos']['nom']}.exe":
            run = True

    if config.configue().cfg["variable"]["auto_reload"] and not run:
        os.startfile(os.path.abspath(f"{variable_base.do_script}\convert_ui.bat"))
        time.sleep(1)

    if not run:
        from src.app import app

