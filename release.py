import subprocess
import shutil
import os

if __name__ == '__main__':
    os.system("pyinstaller -F -w -n lilac_timer app.py".encode('utf-8').decode('gbk'))
