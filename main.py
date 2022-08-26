import sys
from PyQt5 import QtWidgets
from Controllers.AppController import AppController

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = AppController()
    form.show()
    sys.exit(app.exec_())