import sys
from PyQt5.QtWidgets import QApplication
from .action import main

def run(db):
    app = QApplication(sys.argv)
    w = main.MainForm()
    w.setPers(db)
    w.show()
    sys.exit(app.exec_())