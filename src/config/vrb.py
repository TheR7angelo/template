import datetime
import os

### VARIABLES
guid = str(os.getenv("USERNAME"))
date_now = datetime.datetime.now()
date_now_format = date_now.strftime("%d/%m/%Y")

### FICHIERS
cfg_config = "src/config/config.json"
# version_file = "src/config/version_file.txt"
version_file = "version_file.txt"
