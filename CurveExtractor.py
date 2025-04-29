"""main.py, runs the curve extraction tool"""
import numpy as np
import sys
import os
import pydicom
import matplotlib as plt
from PIL import Image
from PySide6.QtWidgets import QApplication

from src.Model.Model import Model
from src.View.MainView import View


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__()
        self.model = Model()
        self.view = View(self.model)


if __name__ == '__main__':
    app = App(sys.argv)
    app.view.show()
    app.exec()
