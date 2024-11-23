
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1184, 696)
        self.gif_label = QtWidgets.QLabel(Dialog)
        self.gif_label.setGeometry(QtCore.QRect(0, 0, 1191, 701))
        self.gif_label.setText("")
        self.gif_label.setPixmap(QtGui.QPixmap("../resources/02_1.gif"))
        self.gif_label.setScaledContents(True)
        self.gif_label.setObjectName("gif_label")
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(900, 620, 91, 71))
        self.back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/image-removebg-preview(6).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon)
        self.back.setIconSize(QtCore.QSize(75, 75))
        self.back.setFlat(True)
        self.back.setObjectName("back")
        self.back.setStyleSheet("QPushButton {\n"
"    background-color: transparent;  /* Transparent background */\n"
"    color: white;                   /* White text */\n"
"    padding: 10px 20px;             /* Padding inside the button */\n"
"    font-weight: bold;              /* Bold text */\n"
"    border: none;                   /* Remove the border */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent; /* Light red when pressed */\n"
"    padding-top: 12px;                      /* Simulate pressing by shifting content */\n"
"    padding-left: 22px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:transparent; /* Light semi-transparent red on hover */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: transparent;   /* Transparent when disabled */\n"
"    color: gray;                     /* Gray text when disabled */\n"
"}")
        self.forward = QtWidgets.QPushButton(Dialog)
        self.forward.setGeometry(QtCore.QRect(1040, 620, 71, 71))
        self.forward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./resources/image-removebg-preview(7).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forward.setIcon(icon1)
        self.forward.setIconSize(QtCore.QSize(75, 75))
        self.forward.setFlat(True)
        self.forward.setObjectName("forward")
        self.forward.setStyleSheet("QPushButton {\n"
"    background-color: transparent;  /* Transparent background */\n"
"    color: white;                   /* White text */\n"
"    padding: 10px 20px;             /* Padding inside the button */\n"
"    font-weight: bold;              /* Bold text */\n"
"    border: none;                   /* Remove the border */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent; /* Light red when pressed */\n"
"    padding-top: 12px;                      /* Simulate pressing by shifting content */\n"
"    padding-left: 22px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:transparent; /* Light semi-transparent red on hover */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: transparent;   /* Transparent when disabled */\n"
"    color: gray;                     /* Gray text when disabled */\n"
"}")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
