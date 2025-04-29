# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CurveExtraction.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import matplotlib.pyplot as plt
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QStringListModel)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QPixmap)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QSplitter, QStatusBar, QVBoxLayout, QWidget, QFileDialog)

import sys
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PIL.ImageQt import ImageQt
import numpy as np
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar



class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent = None):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

class ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.curve_figure = MplCanvas()
        self.image_figure = MplCanvas()
        #self.loded_file = ""
        self.dialog = QObject

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(710, 529)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter_4 = QSplitter(self.centralwidget)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.splitter_2 = QSplitter(self.splitter_4)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        #self.image_widget = QWidget(self.widget)
        #self.image_widget = self.image_figure
        self.image_widget = QLabel(self)
        self.image_widget.setObjectName(u"image_widget")

        self.verticalLayout_2.addWidget(self.image_widget)

        #self.curve_widget = QWidget(self.widget)
        self.curve_widget = self.curve_figure
        self.curve_widget.setObjectName(u"curve_widget")

        self.verticalLayout_2.addWidget(self.curve_widget)

        self.splitter.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.thresh_label = QLabel(self.widget1)
        self.thresh_label.setObjectName(u"thresh_label")

        self.verticalLayout.addWidget(self.thresh_label)

        self.threshold_slider = QSlider(self.widget1)
        self.threshold_slider.setObjectName(u"threshold_slider")
        self.threshold_slider.setOrientation(Qt.Vertical)


        self.verticalLayout.addWidget(self.threshold_slider)

        self.threshold_box = QSpinBox(self.widget1)
        self.threshold_box.setObjectName(u"threshold_box")
        self.threshold_box.setEnabled(True)

        self.verticalLayout.addWidget(self.threshold_box)

        self.splitter.addWidget(self.widget1)
        self.splitter_2.addWidget(self.splitter)
        self.widget2 = QWidget(self.splitter_2)
        self.widget2.setObjectName(u"widget2")
        self.horizontalLayout = QHBoxLayout(self.widget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.start_lable = QLabel(self.widget2)
        self.start_lable.setObjectName(u"start_lable")

        self.horizontalLayout.addWidget(self.start_lable)

        self.point_slider1 = QSlider(self.widget2)
        self.point_slider1.setObjectName(u"point_slider1")
        self.point_slider1.setMaximum(100)
        self.point_slider1.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.point_slider1)

        self.spinbox1 = QSpinBox(self.widget2)
        self.spinbox1.setObjectName(u"spinbox1")

        self.horizontalLayout.addWidget(self.spinbox1)

        self.splitter_2.addWidget(self.widget2)
        self.widget3 = QWidget(self.splitter_2)
        self.widget3.setObjectName(u"widget3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.start_lable_2 = QLabel(self.widget3)
        self.start_lable_2.setObjectName(u"start_lable_2")

        self.horizontalLayout_2.addWidget(self.start_lable_2)

        self.point_slider2 = QSlider(self.widget3)
        self.point_slider2.setObjectName(u"point_slider2")
        self.point_slider2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.point_slider2)

        self.spinbox2 = QSpinBox(self.widget3)
        self.spinbox2.setObjectName(u"spinbox2")

        self.horizontalLayout_2.addWidget(self.spinbox2)

        self.splitter_2.addWidget(self.widget3)
        self.splitter_4.addWidget(self.splitter_2)
        self.splitter_3 = QSplitter(self.splitter_4)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.export_button = QPushButton(self.splitter_3)
        self.export_button.setObjectName(u"export_button")
        self.export_button.clicked.connect(self.export_button_clicked)
        self.splitter_3.addWidget(self.export_button)

        self.load_button = QPushButton(self.splitter_3)
        self.load_button.clicked.connect(self.load_button_clicked)
        self.load_button.setObjectName(u"import_button")
        self.splitter_3.addWidget(self.load_button)
        self.splitter_4.addWidget(self.splitter_3)

        self.verticalLayout_3.addWidget(self.splitter_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.point_slider1.valueChanged.connect(self.spinbox1.setValue)
        self.point_slider2.valueChanged.connect(self.spinbox2.setValue)
        self.spinbox1.valueChanged.connect(self.point_slider1.setValue)
        self.spinbox2.valueChanged.connect(self.point_slider2.setValue)
        self.threshold_box.valueChanged.connect(self.threshold_slider.setValue)
        self.threshold_slider.sliderMoved.connect(self.threshold_box.setValue)

        QMetaObject.connectSlotsByName(MainWindow)

        self.threshold_slider.setRange(0,255)
        self.threshold_box.setRange(0,255)

        self.threshold_slider.sliderMoved.connect(self.thresh_changed)
        self.threshold_box.valueChanged.connect(self.thresh_changed)

        self.point_slider1.valueChanged.connect(self.line_moved)
        self.point_slider2.valueChanged.connect(self.line_moved)
        self.spinbox1.valueChanged.connect(self.line_moved)
        self.spinbox2.valueChanged.connect(self.line_moved)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.thresh_label.setText(QCoreApplication.translate("MainWindow", u"threshold", None))
        self.start_lable.setText(QCoreApplication.translate("MainWindow", u"start point", None))
        self.start_lable_2.setText(QCoreApplication.translate("MainWindow", u"end point", None))
        self.export_button.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"Load Dicom", None))
    # retranslateUi

    def load_button_clicked(self):
        self.model.reset()
        self.image_widget.clear()
        self.image_figure.axes.cla()
        self.dialog = QFileDialog(self)
        self.dialog.setFileMode(QFileDialog.ExistingFile)
        self.dialog.setWindowTitle('Open file...')
        folder_names = QStringListModel
        if self.dialog.exec():
            self.model.directory = self.dialog.selectedFiles()[0]
            check = self.model.loadDicom()
            if check == -1:
                return -1

        self.threshold_box.setValue(self.model.defaultThresh)
        self.point_slider1.setMaximum(self.model.image_width)
        self.spinbox1.setMaximum(self.model.image_width)
        self.spinbox2.setMaximum(self.model.image_width)
        self.point_slider2.setMaximum(self.model.image_width)
        self.point_slider2.setValue(self.model.image_width)
        self.update_grey()

    def update_grey(self):
        temp = ImageQt(self.model.final_image)
        pix = QPixmap.fromImage(temp)
        self.image_widget.setPixmap(pix)


    def update_graph(self):
        temp_graph = np.array(self.model.graph)
        max_idx = np.argmax(temp_graph, axis=0)
        min_idx = np.argmin(temp_graph, axis=0)
        max_x, max_y = temp_graph[max_idx]
        min_x, min_y = temp_graph[min_idx]

        self.curve_figure.axes.cla()
        numpy_graph = np.array(self.model.graph).T

        self.curve_figure.axes.plot(numpy_graph[0], numpy_graph[1], c='b')

        self.curve_figure.axes.vlines(self.model.red_graph,min_y[1], max_y[1], colors='r')
        self.curve_figure.axes.vlines(self.model.green_graph,min_y[1], max_y[1], colors='g')
        self.curve_figure.draw()

    def thresh_changed(self):
        self.model.update_image_thresh(self.threshold_slider.value())
        self.line_moved()
        self.model.update_graph()
        self.update_grey()
        self.update_graph()

    def line_moved(self):
        self.model.image_add_lines(self.point_slider1.value(), self.point_slider2.value())
        self.update_grey()
        self.update_graph()

    def export_button_clicked(self):
        self.dialog = QFileDialog(self)
        file_name = QFileDialog.getSaveFileName(self, 'Dialog Title',
                                               '/path/to/default/directory', selectedFilter='*.csv')
        if file_name:
            check = self.model.export(file_name, self.point_slider1.value(),
                                      self.point_slider2.value())
            if check == -1:
                return -1

