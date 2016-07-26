import time, sys
from widget import MailUI
import configparser
from PyQt5.QtWidgets import QApplication

# 2016_07_25
from mail_sender import MailSender

date = time.strftime('%Y%m%d', time.localtime(time.time()))
title = 'Daily_Report_Flyn_%s' % date

configparser = configparser.ConfigParser()
configparser.read('config.txt')

mail_sender = MailSender()

mail_sender.to_address = configparser.get("Info", "to_address")
mail_sender.from_address = configparser.get("Info", "from_address")
mail_sender.my_name = configparser.get("Info", "my_name")
mail_sender.password = configparser.get("Info", "password")
mail_sender.smtp_server = configparser.get("Info", "smtp_server")
mail_sender.smtp_server_port = configparser.get("Info", "smtp_server_port")

app = QApplication(sys.argv)
mail_ui = MailUI()


def send_listener():
    mail_title = mail_ui.te_title.toPlainText()
    mail_content = mail_ui.te_content.toPlainText()
    mail_sender.send(mail_title, mail_content,
                     lambda: mail_ui.show_info_message_box('Info', '发送成功!', lambda: mail_ui.close_self()),
                     lambda: mail_ui.show_question_message_box('Warning', '发送失败,是否重新发送!', send_listener, lambda: mail_ui.close_self())
                     )


mail_ui.set_send_listener(send_listener)
mail_ui.show(title, "World")
app.exec_()
