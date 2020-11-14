# Говнокод
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog
import design
import subprocess



class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(ExampleApp, self).__init__()
        self.setupUi(self)
        self.Button_polyakov.clicked.connect(
            lambda: subprocess.Popen(['python', 'Kpolyakov.py', self.LineEdit_link.text()]))
        self.Button_brainly.clicked.connect(
            lambda: subprocess.Popen(['python', 'brainly.py', self.LineEdit_link.text()]))
        #todo self.Button_info.clicked.connect()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()







