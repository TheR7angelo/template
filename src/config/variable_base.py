import datetime
import os

### VARIABLES
guid = str(os.getenv("USERNAME"))
date_now = datetime.datetime.now()
date_now_format = date_now.strftime("%d/%m/%Y")

### DOSSIER
do_img_ui = "src/assets/ui"
do_img_logo = "src/assets/img/logo"
do_img_divers = "src/assets/img/divers"
do_cur = "src/assets/cursor"
do_script = "src/scripts"

### FICHIERS
cfg_config = "src/config/config.json"
version_file = "src/config/version_file.txt"

