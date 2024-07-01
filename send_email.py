import smtplib, ssl
import os


def send_email(curated_message):
    host = 'smtp.gmail.com'
    port = 465

    sender = 'segun.adeokun@gmail.com'
    password = os.getenv('PASSWORD')
    receiver = 'shegs637@gmail.com'

    con = ssl.create_default_context()
    message = curated_message

    with smtplib.SMTP_SSL(host, port, context=con) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)

