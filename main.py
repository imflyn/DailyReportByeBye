import time
import sys
import git
import os
from widget import MailUI
import configparser
from PyQt5.QtWidgets import QApplication

# 2016_07_25
from mail_sender import MailSender


def get_mail_content(logs: list) -> str:
    content = ''
    content += 'Hi all, \n'
    content += 'Today\'s report: \n\n'
    content += 'DONE: \n'
    for index, log in enumerate(logs):
        content += str(index + 1) + '. ' + log + '.\n'
    content += '\n'
    content += 'TODO: \n\n'
    content += 'Thanks, \n'
    content += 'Flyn \n'
    return content


date = time.strftime('%Y%m%d', time.localtime(time.time()))
title = 'Daily_Report_Flyn_%s' % date

configparser = configparser.ConfigParser()
configparser.read(os.path.dirname(os.path.realpath(__file__)) + '\\config.txt')

mail_sender = MailSender()

mail_sender.to_address = configparser.get("Info", "to_address")
mail_sender.from_address = configparser.get("Info", "from_address")
mail_sender.my_name = configparser.get("Info", "my_name")
mail_sender.password = configparser.get("Info", "password")
mail_sender.smtp_server = configparser.get("Info", "smtp_server")
mail_sender.smtp_server_port = configparser.get("Info", "smtp_server_port")

paths = configparser.get("Info", "path")  # type:str
path_list = paths.split(",")
git_logs = git.get_commit_logs(path_list, 'flyn.yu')
content = get_mail_content(git_logs)

app = QApplication(sys.argv)
mail_ui = MailUI()


def send_listener():
    mail_title = mail_ui.te_title.toPlainText()
    mail_content = mail_ui.te_content.toPlainText()
    mail_sender.send(mail_title, mail_content,
                     lambda: mail_ui.show_info_message_box('Info', '发送成功!', lambda: mail_ui.close_self()),
                     lambda exception: mail_ui.show_question_message_box('Warning', exception + '\n' + '发送失败,是否重新发送?',
                                                                         send_listener,
                                                                         lambda: mail_ui.close_self())
                     )


mail_ui.set_send_listener(send_listener)
mail_ui.show(title, content)
app.exec_()
