import sys
import os
from os.path import expanduser
import shutil
import matplotlib.pyplot as plt
import pandas as pd
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QTextEdit, QPushButton

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

        self.button = QPushButton("Выберите файл csv", self)
        self.button.setGeometry(50,50,200,50)
        self.button.clicked.connect(self.openFileDialog)

        self.button = QPushButton("Cохраните файл", self)
        self.button.setGeometry(250,50,200,50)
        self.button.clicked.connect(self.saveFileDialog)

        self.button = QPushButton("Построить диаграмму", self)
        self.button.setGeometry(50,400,200, 50)
        self.button.clicked.connect(self.PlotDiagram)

        self.button = QPushButton("Выход", self)
        self.button.setGeometry(250, 400, 200, 50)
        self.button.clicked.connect(sys.exit)

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

    def saveFileDialog(self):
        filename2 = QFileDialog.getSaveFileName(self, 'Сохраните файл', 'mydata.csv', 'Файлы csv (*.csv)')
        if filename2[0]:
            f = open(filename2[0], 'w', encoding='utf-8')
            with f:
                f.write(self.__data)
        __mypath1 = os.path.join(expanduser("~"), 'mydat.csv')
        shutil.copyfile(filename2[0], __mypath1)

    def PlotDiagram(self):
        __mypath = os.path.join(expanduser("~"), 'mydat.csv')
        data = pd.read_csv(__mypath, sep=';', encoding='utf-8')
        data = data.sort_values(by='Статьи РИНЦ')[:20]
        cafedra = data.values[:, 0]
        article = data.values[:, 1]

        plt.figure(figsize=(10, 5))
        plt.barh(cafedra, article)
        plt.title = "Топ 20 кафедр СибГМУ, издавающих статьи в РИНЦ (апрель 2020г.)"
        plt.show()

