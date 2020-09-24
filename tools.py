import os
import subprocess
from config import Ui_PATH, Src_UI_PATH
import logging


class UiBuilder:
    @classmethod
    def build(cls):
        logging.info("开始构建ui文件")
        if not os.path.exists(Ui_PATH):
            return FileNotFoundError("找不到UI文件夹，请查看config.py配置文件")
        if not os.path.exists(Src_UI_PATH):
            os.makedirs(Src_UI_PATH)
        for _, _, files in os.walk(Ui_PATH):
            for filename in files:
                cls().build_one(Ui_PATH, Src_UI_PATH, filename)

    def build_one(self, ui_path_prefix, src_path_prefix, filename):
        ui_filename = os.path.join(ui_path_prefix, filename)
        src_filename = os.path.join(src_path_prefix, os.path.splitext(filename)[0] + '.py')
        try:
            commond = ["pyuic5", ui_filename, "-o", src_filename]
            logging.info("Building: {}".format(" ".join(commond)))
            subprocess.call(["pyuic5", ui_filename, "-o", src_filename])
        except subprocess.CalledProcessError as e:
            logging.debug(e)
            raise e


if __name__ == '__main__':
    UiBuilder.build()
