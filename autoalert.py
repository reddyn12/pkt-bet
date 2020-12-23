import smtplib
from email.message import EmailMessage


def text(body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["to"] = to
    user = "pktbettingupdates@gmail.com"
    msg["from"] = user
    password = "wesrwbhpnjuqqstt"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


if __name__ == "__main__":
    text("Nikhil is GOD", "7814547221@vtext.com")
