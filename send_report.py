# !/usr/bin/env python3
# coding: utf-8
import datetime
import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pdfkit
import pytest
import helper

date = str(datetime.datetime.today())[0:-7]
receiver = helper.get_config_item("mail_report", "receive_mail", f="MAIL_REPORT.conf")
sender = helper.get_config_item("email_account", "username", f="QA.conf")
smtpserver = helper.get_config_item("email_account", "smtpserver", f="QA.conf")
password = helper.get_config_item("email_account", "password", f="QA.conf")

def send_report(file, receiver):
    subject = '自动化测试报告' + date
    text = "hi,管理员：\n这是自动化测试报告，请查收！~"
    part1 = MIMEText(text, 'plain')

    msg = MIMEMultipart('alternative')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    msg.attach(part1)
    # msg.attach(part2)

    att = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="report.pdf"'
    msg.attach(att)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    print("邮件已发送")
    smtp.quit()


def test_send_report():
    path_wk = helper.get_config_item("wkhtmltopdf", "path", f="QA.conf")
    config = pdfkit.configuration(wkhtmltopdf=path_wk)
    project_path = helper.project_path
    file = project_path + "\\report.pdf"
    if os.path.exists(file):
        os.remove(file)
    pdfkit.from_file(project_path + "\\report.html", file, configuration=config)
    send_report(file, receiver)

if __name__ == '__main__':
    pytest.main("-q send_report.py")
