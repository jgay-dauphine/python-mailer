import smtplib
import datetime
from email.mime.multipart import MIMEMultipart

class Gmailer:
    def __init__(self, user, passwd):
        self.gmail_user = user
        self.gmail_password = passwd
        return
    
    def send_mail(self, body):
        try:
            # Mail Configuration
            print('Creating mail')
            msg = MIMEMultipart('alternative')
            msg.attach(body)
            print('~~ body attached')
            msg['From'] = self.gmail_user
            msg['To'] = self.gmail_user
            print('~~ Getting current time')
            now = datetime.datetime.now()
            msg['Subject'] = str(now.year) + '/' + str(now.month) + '/' + str(now.day) + ': Test mail'
            print('~~', str(now.year), str(now.month), str(now.day))
            print("Mail created :")
            print(msg.as_string())
            # Sending email
            print('Connecting to Gmail')
            server = smtplib.SMTP('smtp.gmail.com', 587)
            print('Start TLS session')
            server.starttls()
            print('Login:')
            print('~~', self.gmail_user)
            print('~~', self.gmail_password)
            server.login(self.gmail_user, self.gmail_password)
            print('Sending mail')
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            print('Release Connexion')
            server.close()
            print('Email Sent')
        except Exception as e:
            print(str(e))