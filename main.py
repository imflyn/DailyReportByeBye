import time
from widget import MailUI
import configparser

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
mail_sender.title = title

mail_sender.send('this is a test email !')
