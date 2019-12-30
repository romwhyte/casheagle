import sys
from PyQt5.QtWidgets import QApplication
from casheagle import mainwindow

def run(db):
    app = QApplication(sys.argv)
    w = mainwindow.MainForm()
    w.setPers(db)
    w.show()
    sys.exit(app.exec_())