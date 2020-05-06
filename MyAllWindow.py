import sys
import os
from os.path import expanduser
import shutil
import matplotlib.pyplot as plt
import pandas as pd
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QTextEdit, QWidget, QPushButton, QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import QtCore, QtWidgets
import csv

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__data = None

        self.title = "Работа с файлом csv"
        self.top = 50
        self.left = 50
        self.width = 500
        self.height = 500
        self.InitWindow()

    def InitWindow(self):

        self.textedit = QTextEdit(self)
        self.textedit.setGeometry(50,100,400,300)

        self.button = QPushButton("Посмотреть таблицу", self)
        self.button.setGeometry(250, 0, 200, 50)
        self.button.clicked.connect(self.ShowTable)

        self.button = QPushButton("Выберите файл csv", self)
        self.button.setGeometry(50,50,200,50)
        self.button.clicked.connect(self.openFileDialog)

        self.button = QPushButton("Выход", self)
        self.button.setGeometry(250,50,200,50)
        self.button.clicked.connect(sys.exit)

        self.button = QPushButton("Гистограмма по кол-ву статей", self)
        self.button.setGeometry(50,400,200, 50)
        self.button.clicked.connect(self.PlotDiagramArt)

        self.button = QPushButton("Гистограмма по цитированиям", self)
        self.button.setGeometry(250, 400, 200, 50)
        self.button.clicked.connect(self.PlotDiagramCit)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setFixedSize(500, 500)

    def openFileDialog(self):
        filename = QFileDialog.getOpenFileName(self, 'Выберите файл csv', expanduser("~"), filter='Файлы csv (*.csv)')
        if filename[0]:
            f = open(filename[0], 'r', encoding='cp1251')
            with f:
                self.__data = f.read()
                self.textedit.setText(self.__data)
        __mypath = os.path.join(expanduser("~"), 'mydata.csv')
        shutil.copyfile(filename[0], __mypath)

    def ShowTable(self):
        self.ex = MyWidget()
        self.ex.show()

    def PlotDiagramArt(self):
        __mypath = os.path.join(expanduser("~"), 'mydata.csv')
        data = pd.read_csv(__mypath, sep=';', encoding='cp1251')
        data = data.sort_values(by='Статьи РИНЦ')[:20]
        cafedra = data.values[:, 0]
        article = data.values[:, 1]

        plt.figure(figsize=(10, 5))
        plt.barh(cafedra, article)
        plt.title = "Топ 20 кафедр СибГМУ, издавающих статьи в РИНЦ (апрель 2020г.) по кол-ву статей"
        plt.show()

    def PlotDiagramCit(self):
        __mypath = os.path.join(expanduser("~"), 'mydata.csv')
        data = pd.read_csv(__mypath, sep=';', encoding='cp1251')
        data = data.sort_values(by='Цитирования РИНЦ')[:20]
        cafedra = data.values[:, 0]
        citation = data.values[:, 2]

        plt.figure(figsize=(10, 5))
        plt.barh(cafedra, citation)
        plt.title = "Топ 20 кафедр СибГМУ, издавающих статьи в РИНЦ (апрель 2020г.) по цитирования"
        plt.show()

class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        __mypath = os.path.join(expanduser("~"), 'mydata.csv')
        self.loadTable(__mypath)

    def loadTable(self, __mypath):
        self.setFixedSize(880, 600)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 870, 600))
        csvfile = open(__mypath, encoding="cp1251")
        reader = csv.reader(csvfile, delimiter=';')
        title = next(reader)
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(reader):
            self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()
