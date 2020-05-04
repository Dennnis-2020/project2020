import sys
from PyQt5.QtWidgets import QApplication
from MyAllWindow import MyWindow

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(App.exec())



