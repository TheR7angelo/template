import psutil

from src.config import *
from src.build import *

import os
import time


if __name__ == "__main__":
    run = False
    for proc in psutil.process_iter():
        pi = proc.as_dict(attrs=["pid", "name"])
        if pi["name"] == f"{config.configue.get()['nom']}.exe":
            run = True

    if not run:
        from src.app import app

