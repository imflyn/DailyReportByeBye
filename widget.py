import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel, QApplication, QDesktopWidget, QPushButton, QSpacerItem


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

    def show(self):
        self.resize(500, 400)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setWindowTitle('Daily Report Bye Bye')
        super().show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    notepad = MailUI()
    notepad.show()
    app.exec_()
