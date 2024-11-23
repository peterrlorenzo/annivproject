from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1184, 696)
        self.gif_label = QtWidgets.QLabel(Dialog)
        self.gif_label.setGeometry(QtCore.QRect(0, 0, 1191, 701))
        self.gif_label.setText("")
        self.gif_label.setObjectName("gif_label")
        self.paws_label = QtWidgets.QLabel(Dialog)
        self.paws_label.setGeometry(QtCore.QRect(780, 635, 150, 40))
        self.paws_label.setText("Click the paws!")
        self.paws_label.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.paws_label.setVisible(False)
        self.white_paw_label = QtWidgets.QLabel(Dialog)
        self.white_paw_label.setGeometry(QtCore.QRect(720, 635, 250, 40))  
        self.white_paw_label.setText("Click the White Paw\n   one more time!")
        self.white_paw_label.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.white_paw_label.setVisible(False)
        self.gif_paths = [
            "resources/02_1-ezgif.com-loop-count.gif",
            "resources/02_2-ezgif.com-loop-count.gif",
            "resources/02_3-ezgif.com-loop-count.gif",
            "resources/02_4-ezgif.com-loop-count.gif",
            "resources/02_5-ezgif.com-loop-count.gif",
            "resources/02_6-ezgif.com-loop-count.gif",
            "resources/02_7-ezgif.com-loop-count.gif",
            "resources/02_8-ezgif.com-loop-count.gif",
            "resources/02_9-ezgif.com-loop-count.gif",
            "resources/02_10-ezgif.com-loop-count.gif",
            "resources/02_11-ezgif.com-loop-count.gif",
        ]
        self.current_gif_index = 0
        self.update_gif()
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(900, 620, 91, 71))
        self.back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/image-removebg-preview(6).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon1.addPixmap(QtGui.QPixmap("resources/image-removebg-preview(7).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.forward.clicked.connect(self.next_gif)
        self.back.clicked.connect(self.prev_gif)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def prev_gif(self):
        if self.current_gif_index > 0:
            self.current_gif_index -= 1
            self.update_gif()

    def update_gif(self):
        current_path = self.gif_paths[self.current_gif_index]
        self.movie = QtGui.QMovie(current_path)
        if not self.movie.isValid():
            print(f"Error: Invalid GIF or path: {current_path}")
            return
        self.gif_label.setMovie(self.movie)
        self.gif_label.setScaledContents(True)
        self.movie.start()
        if self.current_gif_index == 0:
            self.paws_label.setVisible(True)
            self.white_paw_label.setVisible(False)
        elif self.current_gif_index == 10:
            self.paws_label.setVisible(False)
            self.white_paw_label.setVisible(True) 
        else:
            self.paws_label.setVisible(False)
            self.white_paw_label.setVisible(False) 

    def next_gif(self):
        if self.current_gif_index == len(self.gif_paths) - 1:
            self.show_flower_message()
        else:
            self.current_gif_index += 1
            self.update_gif()

    def show_flower_message(self):
        flower_images = [
            "resources/catflower1.jpg",
            "resources/catflower_2.jpg",
            "resources/catflower3.jpg",
            "resources/catflower4.jpg",
            "resources/otterheart.jpg"
        ]
        flower_texts = [
            "Here is another flower <3",
            "And another...",
            "One more...",
            "Also take my heart and love with you <3 \n I love you"
        ]   
        def display_flower_msg():
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("A Flower for You")
            msg.setTextFormat(QtCore.Qt.RichText)
            msg.setText("<h3 style='text-align: center;'>Here is a flower for you <3</h3>")
            flower_pixmap = QtGui.QPixmap(flower_images[0]).scaled(300, 300, QtCore.Qt.KeepAspectRatio)
            msg.setIconPixmap(flower_pixmap)
            take_button = msg.addButton("Take the Flower", QtWidgets.QMessageBox.AcceptRole)
            deny_button = msg.addButton("Deny the Flower", QtWidgets.QMessageBox.RejectRole)
            msg.exec_()
            if msg.clickedButton() == take_button:
                for i, flower_image in enumerate(flower_images[1:]):
                    another_flower_msg = QtWidgets.QMessageBox()
                    another_flower_msg.setWindowTitle("Here is Another Flower")
                    flower_text = flower_texts[i] if i < len(flower_texts) else "Here's another one..."
                    another_flower_msg.setText(f"<h3 style='text-align: center;'>{flower_text}</h3>")
                    another_flower_pixmap = QtGui.QPixmap(flower_image).scaled(300, 300, QtCore.Qt.KeepAspectRatio)
                    another_flower_msg.setIconPixmap(another_flower_pixmap)
                    another_flower_msg.addButton("Thank You", QtWidgets.QMessageBox.AcceptRole)
                    another_flower_msg.exec_()
                continue_msg = QtWidgets.QMessageBox()
                continue_msg.setWindowTitle("End or Continue?")
                continue_msg.setTextFormat(QtCore.Qt.RichText)
                continue_msg.setText("<h3 style='text-align: center;'>Do you want to exit the program or keep reading the letter?</h3>")
                continue_msg.addButton("Exit", QtWidgets.QMessageBox.AcceptRole)
                continue_msg.addButton("Still looking", QtWidgets.QMessageBox.RejectRole)
                continue_msg.exec_()
                if continue_msg.clickedButton().text() == "Exit":
                    QtWidgets.QApplication.quit()  # End the program
                elif continue_msg.clickedButton().text() == "Still looking":
                    return

            elif msg.clickedButton() == deny_button:
                sad_msg = QtWidgets.QMessageBox()
                sad_msg.setWindowTitle("Why Not? :(")
                sad_msg.setTextFormat(QtCore.Qt.RichText)
                sad_msg.setText("<h3 style='text-align: center;'>WHY NOT? :(</h3>")
                sad_pixmap = QtGui.QPixmap("resources/why_not.jpg").scaled(300, 300, QtCore.Qt.KeepAspectRatio)
                sad_msg.setIconPixmap(sad_pixmap)
                return_button = sad_msg.addButton("Okay, I'm sorry", QtWidgets.QMessageBox.AcceptRole)
                sad_msg.exec_()
                if sad_msg.clickedButton() == return_button:
                    display_flower_msg()
        display_flower_msg()
        
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
