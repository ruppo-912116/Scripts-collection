import time
import smtplib
from datetime import datetime


# this function sends mail to the specified person
def sendingMail(sender_email, rec_email, password, message):
    body = message

    headers = ["From: " + sender_email,
               "Subject: " + "Notice from TU",
               "To: " + rec_email,
               "MIME-Version: 1.0",
               "Content-Type: text/plain"]
    headers = "\r\n".join(headers)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email, password)
    print("login successful")
    server.sendmail(sender_email, rec_email, headers + "\r\n\r\n" + body)
    print("Email has been sent to", rec_email)
    server.quit()
    return
