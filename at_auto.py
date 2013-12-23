# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'at.ui'
#
# Created: Thu Dec 19 12:30:36 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_at_auto(object):


    def setupUi(self, at_auto):
        at_auto.setObjectName(_fromUtf8("at_auto"))
        at_auto.resize(400, 300)
        self.command = QtGui.QLineEdit(at_auto)
        self.command.setGeometry(QtCore.QRect(20, 20, 113, 27))
        self.command.setObjectName(_fromUtf8("command"))
        self.time = QtGui.QDateTimeEdit(at_auto)
        self.time.setGeometry(QtCore.QRect(170, 20, 194, 27))
        self.time.setObjectName(_fromUtf8("time"))
        self.schedule = QtGui.QPushButton(at_auto)
        self.schedule.setGeometry(QtCore.QRect(260, 100, 98, 27))
        self.schedule.setObjectName(_fromUtf8("schedule"))

        self.retranslateUi(at_auto)
        QtCore.QMetaObject.connectSlotsByName(at_auto)

    def retranslateUi(self, at_auto):
        at_auto.setWindowTitle(QtGui.QApplication.translate("at_auto", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.schedule.setText(QtGui.QApplication.translate("at_auto", "Schedule", None, QtGui.QApplication.UnicodeUTF8))

