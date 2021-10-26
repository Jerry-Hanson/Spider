# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tt2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

from rfa import RfaSpider
from multiprocessing import Process
import os

from PyQt5.Qt import (QApplication, QWidget, QPushButton,
                      QThread)

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
class Ui_dialog(object):
    self.runner = CrawlerProcess(get_project_settings())

    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(661, 428)
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(560, 30, 56, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 110, 56, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.radioButton = QtWidgets.QRadioButton(dialog)
        self.radioButton.setGeometry(QtCore.QRect(40, 40, 68, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 40, 68, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(200, 40, 68, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(280, 40, 68, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.lineEdit = QtWidgets.QLineEdit(dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 100, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(30, 100, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 140, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 100, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(210, 100, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(420, 100, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(370, 100, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(270, 140, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(dialog)
        self.label_5.setGeometry(QtCore.QRect(210, 140, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.spinBox = QtWidgets.QSpinBox(dialog)
        self.spinBox.setGeometry(QtCore.QRect(110, 200, 42, 22))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.label_6 = QtWidgets.QLabel(dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 200, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(dialog)
        self.label_7.setGeometry(QtCore.QRect(160, 200, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.progressBar = QtWidgets.QProgressBar(dialog)
        self.progressBar.setGeometry(QtCore.QRect(80, 380, 561, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_8 = QtWidgets.QLabel(dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 378, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(240, 200, 62, 22))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.textEdit = QtWidgets.QTextEdit(dialog)
        self.textEdit.setGeometry(QtCore.QRect(90, 310, 551, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.radioButton_5 = QtWidgets.QRadioButton(dialog)
        self.radioButton_5.setGeometry(QtCore.QRect(30, 250, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 250, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_9 = QtWidgets.QLabel(dialog)
        self.label_9.setGeometry(QtCore.QRect(30, 310, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "网络爬虫"))
        self.pushButton.setText(_translate("dialog", "开始"))
        self.pushButton_2.setText(_translate("dialog", "停止"))
        self.radioButton.setText(_translate("dialog", "推特"))
        self.radioButton_2.setText(_translate("dialog", "亚洲自由"))
        self.radioButton_3.setText(_translate("dialog", "美国之音"))
        self.radioButton_4.setText(_translate("dialog", "大纪元"))
        self.label.setText(_translate("dialog", "数据库IP"))
        self.label_2.setText(_translate("dialog", "数据库名"))
        self.label_3.setText(_translate("dialog", "user"))
        self.label_4.setText(_translate("dialog", "password"))
        self.label_5.setText(_translate("dialog", "数据表名"))
        self.label_6.setText(_translate("dialog", "爬取数量(条)"))
        self.label_7.setText(_translate("dialog", "休眠时间(s)"))
        self.label_8.setText(_translate("dialog", "进度条"))
        self.radioButton_5.setText(_translate("dialog", "关键词爬取"))
        self.label_9.setText(_translate("dialog", "运行日志"))
        self.pushButton.clicked.connect(self.start_crawl)
        self.pushButton_2.clicked.connect(self.stop_crawl)

    def start_crawl(self):
        self.runner.crawl(RfaSpider)
        self.thread1 = Thread_1(self.runner)
        self.thread1.start()



    def stop_crawl(self):
        print("爬虫结束")
        self.runner.stop()

# run spider thread
class SpiderThread(QThread):
    def __init__(self, runner):
        super().__init__()
        self.runner = runner

    def run(self):
        self.runner.start()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_dialog()  # ui_from是类名
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

