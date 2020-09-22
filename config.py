DEBUF = False
Ui_PATH = './ui'
Src_UI_PATH = './src/ui'

import logging

if DEBUF:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)
