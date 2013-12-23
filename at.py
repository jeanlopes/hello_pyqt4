
__author__ = 'jean'

from PyQt4.Qt import *
from at_auto import Ui_at_auto
import time


class At(Ui_at_auto):

    def __init__(self):
        super(At, self).__init__()
        self.widget = QWidget()
        self.setupUi(self.widget)
        self.children = self.widget.children()
        self.time = self.children[1]
        now = QDateTime()
        now.setTime_t(int(time.time()))
        self.time.setDateTime(now)
        self.schedule = self.children[2]
        print 'hehehe'
        self.schedule.clicked.connect(self.schedule_clicked)

    @staticmethod
    def schedule_clicked():
        msg = QMessageBox()
        msg.about(msg, 'Aviso', 'Eu amo a mo bebeza')


    def show(self):
        self.widget.show()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = At()
    ui.show()

    sys.exit(app.exec_())
