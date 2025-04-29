"""Definition of the application view"""
import platform
import os
from PySide6.QtWidgets import QWidget, QMainWindow
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from src.View.ui_mainwindow import ui_MainWindow

loader = QUiLoader()


class View(QMainWindow, ui_MainWindow):
     def __init__(self, model):
        super(ui_MainWindow, self).__init__()
        super(View, self).__init__()
        self.model = model
        self.setupUi(self)
        # self.setWindowTitle("Curve Extraction")
        self.resize(QtCore.QSize(800, 800))

