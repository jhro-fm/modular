import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email(message, subject, sender_show, recipient_show, to_address):
    smtp_server = os.environ['SMTP_SERVER']
    smtp_port = os.environ['SMTP_PORT']
    smtp_user = os.environ['SMTP_USER']
    smtp_passwd = os.environ['SMTP_PASSWD']
    smtp_obj = smtplib.SMTP(smtp_server, smtp_port)
    smtp_obj.login(smtp_user, smtp_passwd)
    msg = MIMEText(message, "plain", "utf-8")
    msg["From"] = Header(sender_show, "utf-8")
    msg["To"] = Header(recipient_show, "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    smtp_obj.sendmail(smtp_user, [to_address], msg.as_string())
