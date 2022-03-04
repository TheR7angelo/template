import psutil

from src.config import *
from src.build import *

import os
import time


if __name__ == "__main__":
    run = False

    # config.configue().update(section="infos", clef="nom", valeur="template")

    for proc in psutil.process_iter():
        pi = proc.as_dict(attrs=["pid", "name"])
        if pi["name"] == f"{config.configue().cfg['infos']['nom']}.exe":
            run = True

    if not run:
        from src.app import app

