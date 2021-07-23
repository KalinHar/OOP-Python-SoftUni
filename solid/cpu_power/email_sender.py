import smtplib, ssl

gmail_username = 'nbdoibgi@gmail.com'
with open('password.secret') as f:
    gmail_password = f.readlines()[0]

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_username, gmail_password)
message = """"\
Subject: CPU Report

{}
"""


def send_email(body):
    server.sendmail(gmail_username, gmail_password, message)
