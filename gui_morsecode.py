# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_morsecode.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 606)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/morse_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.gridLayout_2.addWidget(self.title_label, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 2)
        self.input_code = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_code.setFont(font)
        self.input_code.setObjectName("input_code")
        self.gridLayout_2.addWidget(self.input_code, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 5, 0, 1, 2)
        self.instructions_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instructions_label.sizePolicy().hasHeightForWidth())
        self.instructions_label.setSizePolicy(sizePolicy)
        self.instructions_label.setMaximumSize(QtCore.QSize(16777215, 85))
        self.instructions_label.setObjectName("instructions_label")
        self.gridLayout_2.addWidget(self.instructions_label, 4, 0, 1, 2)
        self.description_label = QtWidgets.QLabel(self.centralwidget)
        self.description_label.setMinimumSize(QtCore.QSize(524, 0))
        self.description_label.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.description_label.setFont(font)
        self.description_label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.description_label.setWordWrap(True)
        self.description_label.setObjectName("description_label")
        self.gridLayout_2.addWidget(self.description_label, 2, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 2)
        self.translate_button = QtWidgets.QPushButton(self.centralwidget)
        self.translate_button.setMaximumSize(QtCore.QSize(16777215, 30))
        self.translate_button.setObjectName("translate_button")
        self.gridLayout_2.addWidget(self.translate_button, 6, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 7, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Morse Code Translator"))
        self.title_label.setText(_translate("MainWindow", "MORSE CODE TRANSLATOR"))
        self.input_code.setPlaceholderText(_translate("MainWindow", "Insert morse code"))
        self.instructions_label.setText(_translate("MainWindow", "1. Write morse code without spaces in the text box.\n"
"2. Click \"Translate\" button or hit enter.\n"
"3. Wait until loading message dissapears.\n"
"4. Scroll over all possible translations in the display box."))
        self.description_label.setText(_translate("MainWindow", "This program will receive a morse code message without any space separations and show all the possible translations for the message."))
        self.translate_button.setText(_translate("MainWindow", "Translate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
