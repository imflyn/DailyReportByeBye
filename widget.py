import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel, QApplication, QDesktopWidget, \
    QPushButton, QSpacerItem, QMessageBox
from PyQt5.QtCore import QCoreApplication


class MailUI(QWidget):
    def __init__(self):
        super().__init__()
        self.te_title = QTextEdit()
        self.te_content = QTextEdit()
        self.btn_send = QPushButton()
        self.__init_ui()

    def __init_ui(self):
        title_layout = QHBoxLayout()
        label_title = QLabel()
        label_title.setText('Title: ')
        title_layout.addWidget(label_title)
        title_layout.addWidget(self.te_title)

        content_layout = QHBoxLayout()
        label_content = QLabel()
        label_content.setText('From : ')
        content_layout.addWidget(label_content)
        content_layout.addWidget(self.te_content)

        space = QSpacerItem(0, 48)

        send_layout = QHBoxLayout()
        space2 = QSpacerItem(0, 0)
        self.btn_send.setText("Send")
        self.btn_send.setMinimumHeight(48)

        send_layout.addItem(space2)
        send_layout.addWidget(self.btn_send)

        father_layout = QVBoxLayout()
        father_layout.addLayout(title_layout, 1)
        father_layout.addLayout(content_layout, 5)
        father_layout.addItem(space)
        father_layout.addLayout(send_layout)
        self.setLayout(father_layout)

    def show(self, title: str, content: str):
        self.resize(500, 400)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setWindowTitle('Daily Report Bye Bye')
        self.te_title.setText(title)
        self.te_content.setText(content)
        super().show()

    def set_send_listener(self, listener):
        self.btn_send.clicked.connect(listener)

    def show_info_message_box(self, title: str, content: str, callback):
        reply = QMessageBox.information(self, title, content, QMessageBox.Ok)
        if reply == QMessageBox.Ok:
            callback()

    def show_question_message_box(self, title: str, content: str, positive_clicked, negative_clicked):
        reply = QMessageBox.information(self, title, content, QMessageBox.Yes | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            positive_clicked()
        elif reply == QMessageBox.Cancel:
            negative_clicked()

    def close_self(self):
        QCoreApplication.instance().quit()


if __name__ == '__main__':
    def click_listener():
        print('hello world')


    app = QApplication(sys.argv)
    mail_ui = MailUI()
    mail_ui.set_send_listener(click_listener)
    mail_ui.show("Hello", "World")
    app.exec_()
