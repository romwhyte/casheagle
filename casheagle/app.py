import sys
from PyQt5.QtWidgets import QApplication
from casheagle import mainwindow

def run():
    app = QApplication(sys.argv)
    w = mainwindow.MainForm()
    w.show()
    sys.exit(app.exec_())