import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QTextEdit, QApplication, QPushButton

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Загрузка файла csv"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.InitWindow()

    def InitWindow(self):

        self.textedit = QTextEdit(self)
        self.textedit.setGeometry(100,150,400,300)

        self.button = QPushButton("Выберите файл csv", self)
        self.button.setGeometry(100,100,200,50)
        self.button.clicked.connect(self.openFileDialog)

      #  self.button = QPushButton("Cохраните файл", self)
      # self.button.setGeometry(300, 100, 200, 50)
      # self.button.clicked.connect(self.saveFileDialog)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()

    def openFileDialog(self):
        filename = QFileDialog.getOpenFileName(self, 'Выберите файл', 'D:')

        if filename[0]:
            f = open(filename[0], 'r')
            with f:
                data = f.read()
                self.textedit.setText(data)

    #def saveFileDialog(self):
     #   filename2 = QFileDialog.getSaveFileName(self, 'Сохраните файл', 'D:')

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
