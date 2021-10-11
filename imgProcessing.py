import --\
    cv2
import numpy as np
from matplotlib import pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, \
    QFormLayout, QLineEdit
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 572)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 71, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 71, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 161, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 380, 161, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 260, 141, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        self.label_5.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 330, 121, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.dosyaAc = QtWidgets.QPushButton(self.centralwidget)
        self.dosyaAc.setGeometry(QtCore.QRect(10, 20, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dosyaAc.setFont(font)
        self.dosyaAc.setObjectName("dosyaAc")
        self.kaydet = QtWidgets.QPushButton(self.centralwidget)
        self.kaydet.setGeometry(QtCore.QRect(80, 20, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.kaydet.setFont(font)
        self.kaydet.setObjectName("kaydet")
        self.orjinalLabel = QtWidgets.QLabel(self.centralwidget)
        self.orjinalLabel.setGeometry(QtCore.QRect(380, 50, 231, 231))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.orjinalLabel.setPalette(palette)
        self.orjinalLabel.setStyleSheet("background:white")
        self.orjinalLabel.setText("")
        self.orjinalLabel.setObjectName("orjinalLabel")
        self.islenmisLabel = QtWidgets.QLabel(self.centralwidget)
        self.islenmisLabel.setGeometry(QtCore.QRect(380, 320, 231, 231))
        self.islenmisLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.islenmisLabel.setText("")
        self.islenmisLabel.setObjectName("islenmisLabel")
        self.videoKenarButon = QtWidgets.QPushButton(self.centralwidget)
        self.videoKenarButon.setGeometry(QtCore.QRect(10, 350, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.videoKenarButon.setFont(font)
        self.videoKenarButon.setObjectName("videoKenarButon")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(380, 25, 141, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_7.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(380, 290, 141, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_8.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.BlurButton = QtWidgets.QPushButton(self.centralwidget)
        self.BlurButton.setGeometry(QtCore.QRect(10, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.BlurButton.setFont(font)
        self.BlurButton.setObjectName("BlurButton")
        self.cannyButton = QtWidgets.QPushButton(self.centralwidget)
        self.cannyButton.setGeometry(QtCore.QRect(60, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.cannyButton.setFont(font)
        self.cannyButton.setObjectName("cannyButton")
        self.bilateralButton = QtWidgets.QPushButton(self.centralwidget)
        self.bilateralButton.setGeometry(QtCore.QRect(110, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.bilateralButton.setFont(font)
        self.bilateralButton.setObjectName("bilateralButton")
        self.medianButton = QtWidgets.QPushButton(self.centralwidget)
        self.medianButton.setGeometry(QtCore.QRect(160, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.medianButton.setFont(font)
        self.medianButton.setObjectName("medianButton")
        self.gaussianButton = QtWidgets.QPushButton(self.centralwidget)
        self.gaussianButton.setGeometry(QtCore.QRect(210, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.gaussianButton.setFont(font)
        self.gaussianButton.setObjectName("gaussianButton")
        self.laplaceButton = QtWidgets.QPushButton(self.centralwidget)
        self.laplaceButton.setGeometry(QtCore.QRect(10, 90, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.laplaceButton.setFont(font)
        self.laplaceButton.setObjectName("laplaceButton")
        self.sobelButton = QtWidgets.QPushButton(self.centralwidget)
        self.sobelButton.setGeometry(QtCore.QRect(60, 90, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.sobelButton.setFont(font)
        self.sobelButton.setObjectName("sobelButton")
        self.filterTwoDbutton = QtWidgets.QPushButton(self.centralwidget)
        self.filterTwoDbutton.setGeometry(QtCore.QRect(110, 90, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.filterTwoDbutton.setFont(font)
        self.filterTwoDbutton.setObjectName("filterTwoDbutton")
        self.boxButton = QtWidgets.QPushButton(self.centralwidget)
        self.boxButton.setGeometry(QtCore.QRect(160, 90, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.boxButton.setFont(font)
        self.boxButton.setObjectName("boxButton")
        self.sharpeningButton = QtWidgets.QPushButton(self.centralwidget)
        self.sharpeningButton.setGeometry(QtCore.QRect(210, 90, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.sharpeningButton.setFont(font)
        self.sharpeningButton.setObjectName("sharpeningButton")
        self.grafikButton = QtWidgets.QPushButton(self.centralwidget)
        self.grafikButton.setGeometry(QtCore.QRect(10, 140, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.grafikButton.setFont(font)
        self.grafikButton.setObjectName("grafikButton")
        self.esitlikButton = QtWidgets.QPushButton(self.centralwidget)
        self.esitlikButton.setGeometry(QtCore.QRect(70, 140, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.esitlikButton.setFont(font)
        self.esitlikButton.setObjectName("esitlikButton")
        self.dokRotateButton = QtWidgets.QPushButton(self.centralwidget)
        self.dokRotateButton.setGeometry(QtCore.QRect(10, 210, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.dokRotateButton.setFont(font)
        self.dokRotateButton.setObjectName("dokRotateButton")
        self.yuzRotButton = QtWidgets.QPushButton(self.centralwidget)
        self.yuzRotButton.setGeometry(QtCore.QRect(70, 210, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.yuzRotButton.setFont(font)
        self.yuzRotButton.setObjectName("yuzRotButton")
        self.ikiYuzRotButton = QtWidgets.QPushButton(self.centralwidget)
        self.ikiYuzRotButton.setGeometry(QtCore.QRect(130, 210, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ikiYuzRotButton.setFont(font)
        self.ikiYuzRotButton.setObjectName("ikiYuzRotButton")
        self.cropButton = QtWidgets.QPushButton(self.centralwidget)
        self.cropButton.setGeometry(QtCore.QRect(10, 230, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.cropButton.setFont(font)
        self.cropButton.setObjectName("cropButton")
        self.resizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.resizeButton.setGeometry(QtCore.QRect(70, 230, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.resizeButton.setFont(font)
        self.resizeButton.setObjectName("resizeButton")
        self.flipButton = QtWidgets.QPushButton(self.centralwidget)
        self.flipButton.setGeometry(QtCore.QRect(130, 230, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.flipButton.setFont(font)
        self.flipButton.setObjectName("flipButton")
        self.erosionButton = QtWidgets.QPushButton(self.centralwidget)
        self.erosionButton.setGeometry(QtCore.QRect(130, 300, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.erosionButton.setFont(font)
        self.erosionButton.setObjectName("erosionButton")
        self.tophatButton = QtWidgets.QPushButton(self.centralwidget)
        self.tophatButton.setGeometry(QtCore.QRect(70, 300, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tophatButton.setFont(font)
        self.tophatButton.setObjectName("tophatButton")
        self.gradientButton = QtWidgets.QPushButton(self.centralwidget)
        self.gradientButton.setGeometry(QtCore.QRect(10, 300, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.gradientButton.setFont(font)
        self.gradientButton.setObjectName("gradientButton")
        self.closingButton = QtWidgets.QPushButton(self.centralwidget)
        self.closingButton.setGeometry(QtCore.QRect(130, 280, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.closingButton.setFont(font)
        self.closingButton.setObjectName("closingButton")
        self.openingButton = QtWidgets.QPushButton(self.centralwidget)
        self.openingButton.setGeometry(QtCore.QRect(70, 280, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.openingButton.setFont(font)
        self.openingButton.setObjectName("openingButton")
        self.dilationButton = QtWidgets.QPushButton(self.centralwidget)
        self.dilationButton.setGeometry(QtCore.QRect(10, 280, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.dilationButton.setFont(font)
        self.dilationButton.setObjectName("dilationButton")
        self.logButton = QtWidgets.QPushButton(self.centralwidget)
        self.logButton.setGeometry(QtCore.QRect(10, 400, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.logButton.setFont(font)
        self.logButton.setObjectName("logButton")
        self.contrastButton = QtWidgets.QPushButton(self.centralwidget)
        self.contrastButton.setGeometry(QtCore.QRect(130, 400, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.contrastButton.setFont(font)
        self.contrastButton.setObjectName("contrastButton")
        self.gammaButton = QtWidgets.QPushButton(self.centralwidget)
        self.gammaButton.setGeometry(QtCore.QRect(70, 400, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.gammaButton.setFont(font)
        self.gammaButton.setObjectName("gammaButton")

        self.crossedButton = QtWidgets.QPushButton(self.centralwidget)
        self.crossedButton.setGeometry(QtCore.QRect(190, 280, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.crossedButton.setFont(font)
        self.crossedButton.setObjectName("crossedButton")

        self.blackHatButton = QtWidgets.QPushButton(self.centralwidget)
        self.blackHatButton.setGeometry(QtCore.QRect(190, 300, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.blackHatButton.setFont(font)
        self.blackHatButton.setObjectName("blackHatButton")

        self.elipsButton = QtWidgets.QPushButton(self.centralwidget)
        self.elipsButton.setGeometry(QtCore.QRect(250, 280, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.elipsButton.setFont(font)
        self.elipsButton.setObjectName("elipsButton")

        self.rectButton = QtWidgets.QPushButton(self.centralwidget)
        self.rectButton.setGeometry(QtCore.QRect(250, 300, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.rectButton.setFont(font)
        self.rectButton.setObjectName("rectButton")

        """

        """

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.dosyaAc.clicked.connect(self.openFile)

        self.kaydet.clicked.connect(self.saveFile)

        self.gaussianButton.clicked.connect(self.GaussianBlur)
        self.BlurButton.clicked.connect(self.Blur)
        self.laplaceButton.clicked.connect(self.Laplace)
        self.sobelButton.clicked.connect(self.Sobel)
        self.filterTwoDbutton.clicked.connect(self.filter2D)
        self.boxButton.clicked.connect(self.boxFilter)
        self.medianButton.clicked.connect(self.median)
        self.cannyButton.clicked.connect(self.canny)
        self.sharpeningButton.clicked.connect(self.sharpening)
        self.bilateralButton.clicked.connect(self.bilateral)
        self.erosionButton.clicked.connect(self.erosion)
        self.dilationButton.clicked.connect(self.dilation)
        self.openingButton.clicked.connect(self.opening)
        self.closingButton.clicked.connect(self.closing)
        self.gradientButton.clicked.connect(self.gradyan)
        self.tophatButton.clicked.connect(self.tophat)
        self.dokRotateButton.clicked.connect(self.dokRotate)
        self.yuzRotButton.clicked.connect(self.yuzRotate)
        self.ikiYuzRotButton.clicked.connect(self.ikiYuzRotate)
        self.cropButton.clicked.connect(self.cropping)
        self.flipButton.clicked.connect(self.flip)
        self.resizeButton.clicked.connect(self.resize)
        self.esitlikButton.clicked.connect(self.histogramEqualization)
        self.grafikButton.clicked.connect(self.histogramGrafik)
        self.contrastButton.clicked.connect(self.contrast)
        self.logButton.clicked.connect(self.logTransform)
        self.gammaButton.clicked.connect(self.gammaTransform)
        self.rectButton.clicked.connect(self.Rect)
        self.blackHatButton.clicked.connect(self.blackHat)
        self.elipsButton.clicked.connect(self.Elipse)
        self.crossedButton.clicked.connect(self.Cross)
        self.videoKenarButon.clicked.connect(self.video)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Filtreler"))
        self.label_2.setText(_translate("MainWindow", "Histogram"))
        self.label_3.setText(_translate("MainWindow", "Uzaysal Dönüşüm İşlemleri"))
        self.label_4.setText(_translate("MainWindow", "Yoğunluk Dönüşümü İşlemleri"))
        self.label_5.setText(_translate("MainWindow", "Morfolojik İşlemler"))
        self.label_6.setText(_translate("MainWindow", "Video Kenar Belirleme"))
        self.dosyaAc.setText(_translate("MainWindow", "Dosya Aç"))
        self.kaydet.setText(_translate("MainWindow", "Kaydet"))
        self.videoKenarButon.setText(_translate("MainWindow", "Video Aç"))
        self.label_7.setText(_translate("MainWindow", "Orjinal Görsel"))
        self.label_8.setText(_translate("MainWindow", "İşlenmiş Görsel"))
        self.BlurButton.setText(_translate("MainWindow", "Blur"))
        self.cannyButton.setText(_translate("MainWindow", "Canny"))
        self.bilateralButton.setText(_translate("MainWindow", "Bilateral"))
        self.medianButton.setText(_translate("MainWindow", "Median"))
        self.gaussianButton.setText(_translate("MainWindow", "Gaussian"))
        self.laplaceButton.setText(_translate("MainWindow", "Laplace"))
        self.sobelButton.setText(_translate("MainWindow", "Sobel"))
        self.filterTwoDbutton.setText(_translate("MainWindow", "Filter2D"))
        self.boxButton.setText(_translate("MainWindow", "BoxFilter"))
        self.sharpeningButton.setText(_translate("MainWindow", "Sharpening"))
        self.grafikButton.setText(_translate("MainWindow", "Grafik"))
        self.esitlikButton.setText(_translate("MainWindow", "Eşitliği"))
        self.dokRotateButton.setText(_translate("MainWindow", "90 Rotate"))
        self.yuzRotButton.setText(_translate("MainWindow", "180 Rot."))
        self.ikiYuzRotButton.setText(_translate("MainWindow", "270 Rot."))
        self.cropButton.setText(_translate("MainWindow", "Cropping"))
        self.resizeButton.setText(_translate("MainWindow", "Resize"))
        self.flipButton.setText(_translate("MainWindow", "Flip"))
        self.erosionButton.setText(_translate("MainWindow", "Eroision"))
        self.tophatButton.setText(_translate("MainWindow", "Tophat"))
        self.gradientButton.setText(_translate("MainWindow", "Gradient"))
        self.closingButton.setText(_translate("MainWindow", "Closing"))
        self.openingButton.setText(_translate("MainWindow", "Opening"))
        self.dilationButton.setText(_translate("MainWindow", "Dilation"))
        self.logButton.setText(_translate("MainWindow", "Logaritmik"))
        self.contrastButton.setText(_translate("MainWindow", "Contrast"))
        self.gammaButton.setText(_translate("MainWindow", "Gamma"))
        self.rectButton.setText(_translate("MainWindow", "Rect"))
        self.crossedButton.setText(_translate("MainWindow", "Cross"))
        self.blackHatButton.setText(_translate("MainWindow", "BlackHat"))
        self.elipsButton.setText(_translate("MainWindow", "Elips"))

    def saveFile(self):
        filename, _ = QFileDialog.getSaveFileName(None, " ", '.',
                                                  'Image Files (*.png *.jpg *.jpeg *.bmp)')

        cv2.imwrite(filename, self.image)

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(None, 'Fotograf Seciniz', '.',
                                                  'Image Files (*.png *.jpg *.jpeg *.bmp )')
        if filename:
            with open(filename, "rb") as file:
                data = np.array(bytearray(file.read()))
                self.image = cv2.imdecode(data, cv2.IMREAD_UNCHANGED)
                self.image = self.olceklendir(self.image)
                self.openImage()



    def openImage(self):
        size = self.image.shape
        step = self.image.size / size[0]
        qformat = QImage.Format_Indexed8

        if len(size) == 3:
            if size[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        img = QImage(self.image, size[1], size[0], step, qformat)
        img = img.rgbSwapped()

        self.orjinalLabel.setPixmap(QPixmap.fromImage(img))

    def processedImg(self):
        size = self.image.shape
        step = self.image.size / size[0]
        qformat = QImage.Format_Indexed8

        if len(size) == 3:
            if size[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        img = QImage(self.image, size[1], size[0], step, qformat)
        img = img.rgbSwapped()
        self.islenmisLabel.setPixmap(QPixmap.fromImage(img))

    def Blur(self):
        if self.image is not None:
            self.image = cv2.blur(self.image, (10, 10))
            self.processedImg()

    def GaussianBlur(self):
        if self.image is not None:
            self.image = cv2.GaussianBlur(self.image, (21, 21), 0, 0)
            self.processedImg()

    def Laplace(self):
        if self.image is not None:
            self.image = cv2.Laplacian(self.image, cv2.CV_32FC4)
            self.processedImg()

    def Sobel(self):
        if self.image is not None:
            self.image = cv2.Sobel(self.image, cv2.CV_8U, 1, 0, ksize=5)
            self.processedImg()

    def filter2D(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            self.image = cv2.filter2D(self.image, -1, kernel)
            self.processedImg()

    def boxFilter(self):
        if self.image is not None:
            self.image = cv2.boxFilter(self.image, 0, (3, 3), self.image, (-1, -1), False, cv2.BORDER_DEFAULT)
            self.processedImg()

    def median(self):
        if self.image is not None:
            self.image = cv2.medianBlur(self.image, ksize=7)
            self.processedImg()

    def canny(self):
        if self.image is not None:
            self.image = cv2.Canny(self.image, 50, 200)
            self.processedImg()

    def sharpening(self):
        if self.image is not None:
            kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            self.image = cv2.filter2D(self.image, -1, kernel)
            self.processedImg()

    def bilateral(self):
        if self.image is not None:
            self.image = cv2.bilateralFilter(self.image, 13, 70, 50)
            self.processedImg()

    # morfolojik işlemler
    def erosion(self):
        if self.image is not None:
            kernelErosion = np.ones((5, 5), np.uint8)
            self.image = cv2.erode(self.image, kernelErosion, iterations=1)
            self.processedImg()

    def dilation(self):
        if self.image is not None:
            kernelDilation = np.ones((15, 15), np.uint8)
            self.image = cv2.dilate(self.image, kernelDilation, iterations=1)
            self.processedImg()

    def opening(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            self.image = cv2.morphologyEx(self.image, cv2.MORPH_OPEN, kernel)
            self.processedImg()

    def closing(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            self.image = cv2.morphologyEx(self.image, cv2.MORPH_CLOSE, kernel)
            self.processedImg()

    def gradyan(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            self.image = cv2.morphologyEx(self.image, cv2.MORPH_GRADIENT, kernel)
            self.processedImg()

    def tophat(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            self.image = cv2.morphologyEx(self.image, cv2.MORPH_TOPHAT, kernel)
            self.processedImg()

    def Cross(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            self.image = cv2.morphologyEx(self.image, cv2.MORPH_CROSS, kernel)
            self.processedImg()

    def Elipse(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            self.image = cv2.morphologyEx(self.image, cv2.MORPH_ELLIPSE, kernel)
            self.processedImg()

    def Rect(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            self.image = cv2.morphologyEx(self.image, cv2.MORPH_RECT, kernel)
            self.processedImg()

    def blackHat(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            self.image = cv2.morphologyEx(self.image, cv2.MORPH_BLACKHAT, kernel)
            self.processedImg()

    # uzaysal dönüşüm işlemleri
    def olceklendir(self, img):
        img = cv2.resize(img, (231, 231))
        return img

    def dokRotate(self):
        if self.image is not None:
            (h, w) = self.image.shape[:2]
            center = (w / 2, h / 2)
            M = cv2.getRotationMatrix2D(center, 90, 1)
            self.image = cv2.warpAffine(self.image, M, (h, w))
            self.processedImg()

    def yuzRotate(self):
        if self.image is not None:
            (h, w) = self.image.shape[:2]
            center = (w / 2, h / 2)
            M = cv2.getRotationMatrix2D(center, 180, 1)
            self.image = cv2.warpAffine(self.image, M, (h, w))
            self.processedImg()

    def ikiYuzRotate(self):
        if self.image is not None:
            (h, w) = self.image.shape[:2]
            center = (w / 2, h / 2)
            M = cv2.getRotationMatrix2D(center, 270, 1)
            self.image = cv2.warpAffine(self.image, M, (h, w))
            self.processedImg()

    def cropping(self):
        if self.image is not None:

            self.image = self.image[1:150 ,1:150]
            self.image =cv2.resize(self.image,(231,231))
            self.processedImg()

    def flip(self):
        if self.image is not None:
            self.image = cv2.flip(self.image, 1, None)
            self.processedImg()

    def resize(self):
        if self.image is not None:
            self.image = cv2.resize(self.image, (150, 150))
            self.processedImg()

    # Histogram Grafiği ve Eşitleme
    def histogramEqualization(self):
        if self.image is not None:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.image = cv2.equalizeHist(self.image)
            self.processedImg()

    def histogramGrafik(self):
        if self.image is not None:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.image = cv2.equalizeHist(self.image)
            plt.hist(self.image.ravel(), 256, [0, 256])
            self.processedImg()

    # yoğunluk dönüşüm işlemleri
    def contrast(self):
        if self.image is not None:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            r1 = 70
            s1 = 0
            r2 = 140
            s2 = 255

            def pixelVal(pix, r1, s1, r2, s2):
                if (0 <= pix and pix <= r1):
                    return (s1 / r1) * pix
                elif (r1 < pix and pix <= r2):
                    return ((s2 - s1) / (r2 - r1)) * (pix - r1) + s1
                else:
                    return ((255 - s2) / (255 - r2)) * (pix - r2) + s2

            pixelVal_vec = np.vectorize(pixelVal)

            contrast_stretched = pixelVal_vec(self.image, r1, s1, r2, s2)
            cv2.imshow("Contrast", contrast_stretched)

    def logTransform(self):
        if self.image is not None:
            c = 255 / (np.log(1 + np.max(self.image)))
            self.log_transformed = c * np.log(1 + self.image)

            self.log_transformed = np.array(self.log_transformed, dtype=np.uint8)
            self.processedImg()

    def gammaTransform(self):
        if self.image is not None:
            a = 5
            b = 12
            c = 3
            d = 8

            for gamma in [a, b, c, d]:
                gamma_corrected = np.array(255 * (self.image / 255) ** gamma, dtype='uint8')

                cv2.imshow("gamma transformed" + str(gamma) + ".jpg", gamma_corrected)
    def video(self):
        filename, _ = QFileDialog.getOpenFileName(None, ' ', '.',
                                                  'MP4 Files (*.mp4)')
        cap = cv2.VideoCapture(filename)

        while (cap.isOpened()):
            # Videodan bir görüntü al.
            ret, frame = cap.read()

            # Gri formatta okumak için
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            edges = cv2.Canny(gray, 100, 200)

            cv2.imshow('Video Kenar Belirleme', edges)

            # q tuşuna basıldığında çık.
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
