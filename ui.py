# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\project\qt\爬虫项目.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sys

# add module path
from PyQt5.QtCore import QThread, QDate
from PyQt5.QtWidgets import QButtonGroup

sys.path.append(sys.path[0] + '/BigdataSpider')
sys.path.append(sys.path[0] + '/AsiaFree')
sys.path.append(sys.path[0] + '/TweetScraper')
sys.path.append(sys.path[0] + '/voaSpider')

from BigdataSpider.start import start_crawl as start_bigdata_crawl
from AsiaFree.start import start_crawl as start_asia_crawl
from TweetScraper.start import start_crawl as start_tweet_crawl
from voaSpider.start import start_crawl as start_voa_crawl

from multiprocessing import Process, Manager  # 多进程
from functools import partial  # 包装传入进程的 func


class Ui_MainWindow(object):
    def __init__(self):
        self.spider_index = {"tweet": 1, "asia": 2, "voa": 3, "bigdata": 4}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 617)
        # main window container
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_IP = QtWidgets.QLabel(self.centralwidget)
        self.label_IP.setObjectName("label_IP")
        self.horizontalLayout.addWidget(self.label_IP)
        self.lineEdit_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.horizontalLayout.addWidget(self.lineEdit_ip)
        self.label_user = QtWidgets.QLabel(self.centralwidget)
        self.label_user.setObjectName("label_user")
        self.horizontalLayout.addWidget(self.label_user)
        self.lineEdit_user = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.horizontalLayout.addWidget(self.lineEdit_user)
        self.label_passward = QtWidgets.QLabel(self.centralwidget)
        self.label_passward.setObjectName("label_passward")
        self.horizontalLayout.addWidget(self.label_passward)
        self.lineEdit_passward = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_passward.setObjectName("lineEdit_passward")
        self.horizontalLayout.addWidget(self.lineEdit_passward)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_datebasename = QtWidgets.QLabel(self.centralwidget)
        self.label_datebasename.setObjectName("label_datebasename")
        self.horizontalLayout_2.addWidget(self.label_datebasename)
        self.lineEdit_dbname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_dbname.setObjectName("lineEdit_dbname")
        self.horizontalLayout_2.addWidget(self.lineEdit_dbname)
        self.label_datetable_name = QtWidgets.QLabel(self.centralwidget)
        self.label_datetable_name.setObjectName("label_datetable_name")
        self.horizontalLayout_2.addWidget(self.label_datetable_name)
        self.lineEdit_dtname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_dtname.setObjectName("lineEdit_dtname")
        self.horizontalLayout_2.addWidget(self.lineEdit_dtname)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        # tab widget 1
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_gjc1 = QtWidgets.QLabel(self.tab)
        self.label_gjc1.setObjectName("label_gjc1")
        self.horizontalLayout_3.addWidget(self.label_gjc1)
        self.lineEdit_gjc1 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_gjc1.setObjectName("lineEdit_gjc1")
        self.horizontalLayout_3.addWidget(self.lineEdit_gjc1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_number1 = QtWidgets.QLabel(self.tab)
        self.label_number1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_number1.setObjectName("label_number1")
        self.horizontalLayout_4.addWidget(self.label_number1)
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_4.addWidget(self.spinBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_time1 = QtWidgets.QLabel(self.tab)
        self.label_time1.setObjectName("label_time1")
        self.horizontalLayout_4.addWidget(self.label_time1)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.tab)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.horizontalLayout_4.addWidget(self.timeEdit_2)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(4, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.start1 = QtWidgets.QPushButton(self.tab)
        self.start1.setObjectName("start1")
        self.verticalLayout_2.addWidget(self.start1)
        self.stop1 = QtWidgets.QPushButton(self.tab)
        self.stop1.setObjectName("stop1")
        self.verticalLayout_2.addWidget(self.stop1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_logo1 = QtWidgets.QLabel(self.tab)
        self.label_logo1.setObjectName("label_logo1")
        self.verticalLayout_4.addWidget(self.label_logo1)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_progressbar1 = QtWidgets.QLabel(self.tab)
        self.label_progressbar1.setObjectName("label_progressbar1")
        self.horizontalLayout_6.addWidget(self.label_progressbar1)
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_6.addWidget(self.progressBar)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab, "")

        # tab widget 2
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_gjc2 = QtWidgets.QLabel(self.tab_2)
        self.label_gjc2.setObjectName("label_gjc2")
        self.horizontalLayout_8.addWidget(self.label_gjc2)
        self.lineEdit_gjc2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_gjc2.setObjectName("lineEdit_gjc2")
        self.horizontalLayout_8.addWidget(self.lineEdit_gjc2)
        self.horizontalLayout_8.setStretch(1, 2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_number2 = QtWidgets.QLabel(self.tab_2)
        self.label_number2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_number2.setObjectName("label_number2")
        self.horizontalLayout_9.addWidget(self.label_number2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_9.addWidget(self.spinBox_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.label_time2 = QtWidgets.QLabel(self.tab_2)
        self.label_time2.setObjectName("label_time2")
        self.horizontalLayout_9.addWidget(self.label_time2)
        self.timeEdit_3 = QtWidgets.QDateEdit(self.tab_2)
        self.timeEdit_3.setDisplayFormat("yyyy-MM")
        self.timeEdit_3.setDate(QDate.currentDate())
        self.timeEdit_3.setObjectName("timeEdit_3")
        self.horizontalLayout_9.addWidget(self.timeEdit_3)
        self.horizontalLayout_9.setStretch(1, 1)
        self.horizontalLayout_9.setStretch(2, 1)
        self.horizontalLayout_9.setStretch(4, 1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.start2 = QtWidgets.QPushButton(self.tab_2)
        self.start2.setObjectName("start2")
        self.verticalLayout_8.addWidget(self.start2)
        self.stop2 = QtWidgets.QPushButton(self.tab_2)
        self.stop2.setObjectName("stop2")
        self.verticalLayout_8.addWidget(self.stop2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)
        self.horizontalLayout_7.setStretch(0, 1)
        self.verticalLayout_20.addLayout(self.horizontalLayout_7)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_logo2 = QtWidgets.QLabel(self.tab_2)
        self.label_logo2.setObjectName("label_logo2")
        self.verticalLayout_13.addWidget(self.label_logo2)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_13.addWidget(self.textBrowser_2)
        self.verticalLayout_20.addLayout(self.verticalLayout_13)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_20.addWidget(self.label_20)
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout_20.addWidget(self.progressBar_2)
        self.verticalLayout_20.addLayout(self.horizontalLayout_20)
        self.tabWidget.addTab(self.tab_2, "")

        # tab widget 3
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_gjc3 = QtWidgets.QLabel(self.tab_3)
        self.label_gjc3.setObjectName("label_gjc3")
        self.horizontalLayout_11.addWidget(self.label_gjc3)
        self.lineEdit_gjc3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_gjc3.setObjectName("lineEdit_gjc3")
        self.horizontalLayout_11.addWidget(self.lineEdit_gjc3)
        self.horizontalLayout_11.setStretch(1, 2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_number3 = QtWidgets.QLabel(self.tab_3)
        self.label_number3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_number3.setObjectName("label_number3")
        self.horizontalLayout_12.addWidget(self.label_number3)
        self.spinBox_3 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_12.addWidget(self.spinBox_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.llabel_time3 = QtWidgets.QLabel(self.tab_3)
        self.llabel_time3.setObjectName("llabel_time3")
        self.horizontalLayout_12.addWidget(self.llabel_time3)
        self.timeEdit_4 = QtWidgets.QTimeEdit(self.tab_3)
        self.timeEdit_4.setObjectName("timeEdit_4")
        self.horizontalLayout_12.addWidget(self.timeEdit_4)
        self.horizontalLayout_12.setStretch(1, 1)
        self.horizontalLayout_12.setStretch(2, 1)
        self.horizontalLayout_12.setStretch(4, 1)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_10.addLayout(self.verticalLayout_9)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.start3 = QtWidgets.QPushButton(self.tab_3)
        self.start3.setObjectName("start3")
        self.verticalLayout_10.addWidget(self.start3)
        self.stop3 = QtWidgets.QPushButton(self.tab_3)
        self.stop3.setObjectName("stop3")
        self.verticalLayout_10.addWidget(self.stop3)
        self.horizontalLayout_10.addLayout(self.verticalLayout_10)
        self.horizontalLayout_10.setStretch(0, 1)
        self.verticalLayout_21.addLayout(self.horizontalLayout_10)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_logo3 = QtWidgets.QLabel(self.tab_3)
        self.label_logo3.setObjectName("label_logo3")
        self.verticalLayout_14.addWidget(self.label_logo3)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_14.addWidget(self.textBrowser_3)
        self.verticalLayout_21.addLayout(self.verticalLayout_14)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_27 = QtWidgets.QLabel(self.tab_3)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_21.addWidget(self.label_27)
        self.progressBar_3 = QtWidgets.QProgressBar(self.tab_3)
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.horizontalLayout_21.addWidget(self.progressBar_3)
        self.verticalLayout_21.addLayout(self.horizontalLayout_21)
        self.tabWidget.addTab(self.tab_3, "")

        # tab widget 4
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_gjc4 = QtWidgets.QLabel(self.tab_4)
        self.label_gjc4.setObjectName("label_gjc4")
        self.horizontalLayout_14.addWidget(self.label_gjc4)
        self.lineEdit_gjc4 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_gjc4.setObjectName("lineEdit_gjc4")
        self.horizontalLayout_14.addWidget(self.lineEdit_gjc4)
        self.horizontalLayout_14.setStretch(1, 2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_number4 = QtWidgets.QLabel(self.tab_4)
        self.label_number4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_number4.setObjectName("label_number4")
        self.horizontalLayout_19.addWidget(self.label_number4)
        self.spinBox_5 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_5.setObjectName("spinBox_5")
        self.horizontalLayout_19.addWidget(self.spinBox_5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem6)
        self.label_time4 = QtWidgets.QLabel(self.tab_4)
        self.label_time4.setObjectName("label_time4")
        self.horizontalLayout_19.addWidget(self.label_time4)
        self.timeEdit_6 = QtWidgets.QDateEdit(self.tab_4)
        self.timeEdit_6.setObjectName("timeEdit_6")
        self.horizontalLayout_19.addWidget(self.timeEdit_6)
        self.horizontalLayout_19.setStretch(1, 1)
        self.horizontalLayout_19.setStretch(2, 1)
        self.horizontalLayout_19.setStretch(4, 1)
        self.verticalLayout_11.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_13.addLayout(self.verticalLayout_11)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem7)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.start4 = QtWidgets.QPushButton(self.tab_4)
        self.start4.setObjectName("start4")
        self.verticalLayout_12.addWidget(self.start4)
        self.stop4 = QtWidgets.QPushButton(self.tab_4)
        self.stop4.setObjectName("stop4")
        self.verticalLayout_12.addWidget(self.stop4)
        self.horizontalLayout_13.addLayout(self.verticalLayout_12)
        self.horizontalLayout_13.setStretch(0, 1)
        self.verticalLayout_22.addLayout(self.horizontalLayout_13)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_logo4 = QtWidgets.QLabel(self.tab_4)
        self.label_logo4.setObjectName("label_logo4")
        self.verticalLayout_19.addWidget(self.label_logo4)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.verticalLayout_19.addWidget(self.textBrowser_5)
        self.verticalLayout_22.addLayout(self.verticalLayout_19)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_29 = QtWidgets.QLabel(self.tab_4)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_22.addWidget(self.label_29)
        self.progressBar_5 = QtWidgets.QProgressBar(self.tab_4)
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setObjectName("progressBar_5")
        self.horizontalLayout_22.addWidget(self.progressBar_5)
        self.verticalLayout_22.addLayout(self.horizontalLayout_22)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_6.addWidget(self.tabWidget)
        self.verticalLayout_6.setStretch(0, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action12 = QtWidgets.QAction(MainWindow)
        self.action12.setObjectName("action12")
        self.action23 = QtWidgets.QAction(MainWindow)
        self.action23.setObjectName("action23")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数据爬虫"))
        self.label_IP.setText(_translate("MainWindow", "数据库IP"))
        self.label_user.setText(_translate("MainWindow", "账号"))
        self.label_passward.setText(_translate("MainWindow", "密码"))
        self.label_datebasename.setText(_translate("MainWindow", "数据库名"))
        self.label_datetable_name.setText(_translate("MainWindow", "数据表名"))
        self.label_gjc1.setText(_translate("MainWindow", "爬取内容关键词："))
        self.label_number1.setText(_translate("MainWindow", "爬取数量（条）："))
        self.label_time1.setText(_translate("MainWindow", "休眠时间（s）："))
        self.start1.setText(_translate("MainWindow", "开始"))
        self.stop1.setText(_translate("MainWindow", "停止"))
        self.label_logo1.setText(_translate("MainWindow", "运行日志"))
        self.label_progressbar1.setText(_translate("MainWindow", "进度条"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "推特"))
        self.label_gjc2.setText(_translate("MainWindow", "爬取内容关键词："))
        self.label_number2.setText(_translate("MainWindow", "爬取数量（条）："))
        self.label_time2.setText(_translate("MainWindow", "休眠时间（s）："))
        self.start2.setText(_translate("MainWindow", "开始"))
        self.stop2.setText(_translate("MainWindow", "停止"))
        self.label_logo2.setText(_translate("MainWindow", "运行日志"))
        self.label_20.setText(_translate("MainWindow", "进度条"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "亚洲自由"))
        self.label_gjc3.setText(_translate("MainWindow", "爬取内容关键词："))
        self.label_number3.setText(_translate("MainWindow", "爬取数量（条）："))
        self.llabel_time3.setText(_translate("MainWindow", "休眠时间（s）："))
        self.start3.setText(_translate("MainWindow", "开始"))
        self.stop3.setText(_translate("MainWindow", "停止"))
        self.label_logo3.setText(_translate("MainWindow", "运行日志"))
        self.label_27.setText(_translate("MainWindow", "进度条"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "美国之音"))
        self.label_gjc4.setText(_translate("MainWindow", "爬取内容关键词："))
        self.label_number4.setText(_translate("MainWindow", "爬取数量（页）："))
        self.label_time4.setText(_translate("MainWindow", "休眠时间（s）："))
        self.start4.setText(_translate("MainWindow", "开始"))
        self.stop4.setText(_translate("MainWindow", "停止"))
        self.label_logo4.setText(_translate("MainWindow", "运行日志"))
        self.label_29.setText(_translate("MainWindow", "进度条"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "大纪元"))
        self.action12.setText(_translate("MainWindow", "12"))
        self.action23.setText(_translate("MainWindow", "23"))

        # set button click event
        self.stop1.setEnabled(False)
        self.stop2.setEnabled(False)
        self.stop3.setEnabled(False)
        self.stop4.setEnabled(False)
        # 利用partial偏函数固定spider_name等参数来扩展启动函数,
        self.start1.clicked.connect(
            partial(self.create_process_and_start, spider_name='tweet', start_button=self.start1,
                    stop_button=self.stop1, textBrowser=self.textBrowser, start_func=start_tweet_crawl))
        self.stop1.clicked.connect(
            partial(self.stop_process, spider_name='tweet', start_button=self.start1, stop_button=self.stop1))

        self.start2.clicked.connect(
            partial(self.create_process_and_start, spider_name='asia', start_button=self.start2, stop_button=self.stop2,
                    textBrowser=self.textBrowser_2, start_func=start_asia_crawl))
        self.stop2.clicked.connect(
            partial(self.stop_process, spider_name='asia', start_button=self.start2, stop_button=self.stop2))

        self.start3.clicked.connect(
            partial(self.create_process_and_start, spider_name='voa', start_button=self.start3, stop_button=self.stop3,
                    textBrowser=self.textBrowser_3, start_func=start_voa_crawl))
        self.stop3.clicked.connect(
            partial(self.stop_process, spider_name='voa', start_button=self.start3, stop_button=self.stop3))

        self.start4.clicked.connect(
            partial(self.create_process_and_start, spider_name='big_data', start_button=self.start4,
                    stop_button=self.stop4, textBrowser=self.textBrowser_5, start_func=start_bigdata_crawl))
        self.stop4.clicked.connect(
            partial(self.stop_process, spider_name='big_data', start_button=self.start4, stop_button=self.stop4))

    def create_process_and_start(self, spider_name, start_button, stop_button, textBrowser, start_func):
        start_button.setEnabled(False)
        stop_button.setEnabled(True)
        process_name = spider_name + "_process"
        logThreadName = spider_name + "_logThread"
        queue_name = spider_name + "_queue"
        setattr(self, queue_name, Manager().Queue())
        Q = getattr(self, queue_name, None)
        # 大纪元爬虫
        if spider_name == 'big_data':
            finished_page = self.spinBox_5.value()
            year, month, day = self.timeEdit_6.date().getDate()
            finished_time = '-'.join([str(year), str(month), str(day)])
            process_args = (finished_page, finished_time, Q)

        elif spider_name == "asia":
            year, month, day = self.timeEdit_3.date().getDate()
            process_args = (year, month, Q)

        else:
            # TODO 其他爬虫的定制化启动
            process_args = tuple()

        # 动态创建类属性
        setattr(self, process_name, Process(target=start_func, args=process_args))
        setattr(self, logThreadName, LogThread(Q=Q, textBrowser=textBrowser))
        getattr(self, logThreadName, None).updated.connect(partial(self.show_log, textBrowser=textBrowser))

        # 开启进程
        print(process_name + "started")
        getattr(self, process_name, None).start()
        getattr(self, logThreadName, None).start()

    def stop_process(self, spider_name, start_button, stop_button):

        process_name = spider_name + '_process'
        logThreadName = spider_name + "_logThread"

        if getattr(self, process_name, None) is not None and getattr(self, logThreadName, None) is not None:
            getattr(self, logThreadName, None).terminate()
            getattr(self, process_name, None).terminate()
            print(process_name + " stoped")

        else:
            print("PROCESS NOT EXIST")
            exit(-1)
        start_button.setEnabled(True)
        stop_button.setEnabled(False)

    def show_log(self, msg, textBrowser):
        textBrowser.append(msg)
        cursor = textBrowser.textCursor()
        pos = len(textBrowser.toPlainText())
        cursor.setPosition(pos)
        textBrowser.setTextCursor(cursor)


class LogThread(QThread):
    updated = QtCore.pyqtSignal(str)

    def __init__(self, Q, textBrowser):
        super(LogThread, self).__init__()
        self.Q = Q
        self.textBrowser = textBrowser

    def run(self):
        while True:
            if not self.Q.empty():
                self.updated.emit(str(self.Q.get()))
                pass
                # 确保滑动条到底
                # cursor = self.textBrowser.textCursor()
                # pos = len(self.textBrowser.toPlainText())
                # cursor.setPosition(pos)
                # self.textBrowser.setTextCursor(cursor)

                # if '爬取结束' in self.gui.textBrowser_5.toPlainText():
                #     break

                # 睡眠10毫秒，否则太快会导致闪退或者显示乱码
                # self.sleep(1)


if __name__ == "__main__":
    import sys

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 解决了Qtdesigner设计的界面与实际运行界面不一致的问题
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()  # ui_from是类名
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
