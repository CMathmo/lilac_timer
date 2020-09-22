import subprocess
import shutil
import os

if __name__ == '__main__':
    builder_commond = ["pyinstaller", "-F", "-w", "app.py"]
    subprocess.call(builder_commond)
    shutil.rmtree('dist/Img')
    shutil.copytree('Img', 'dist/Img')
