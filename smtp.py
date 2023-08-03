import smtplib, ssl
from email.message import EmailMessage


def send_mail(message,eml_subject):

    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = eml_subject
    msg['From'] = "kylesgeemai@gmail.com"
    msg['To'] = "kk7ahk@winlink.org"


    # Send the actual message
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("kylesgeemail@gmail.com", "trvzxacwfybnsskp")
    server.send_message(msg)
    server.quit()

