import os
from src.main import getPath
from src.main import run
from tools import UiBuilder
from config import DEBUF

if __name__ == '__main__':
    if DEBUF:
        UiBuilder.build()
    run()