import smtplib
from email.mime.text import MIMEText
from email.header import Header

class EmailSender:
    def __init__(self, mail_server, mail_port, mail_user, mail_pass, use_tls=False, debug=False):
        self.mail_server = mail_server
        self.mail_port = mail_port
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.use_tls = use_tls
        self.debug = debug
        self.smtp = None

    def _connect(self):
        self.smtp = smtplib.SMTP()
        if self.debug:
            self.smtp.set_debuglevel(1)

        try:
            self.smtp.connect(self.mail_server, self.mail_port)

            if self.use_tls:
                self.smtp.starttls()

            self.smtp.login(self.mail_user, self.mail_pass)
        except smtplib.SMTPException as e:
            raise e

    def send_email(self, sender, receivers, **args):
        if len(sender) ==0 or len(receivers) == 0:
            raise('sender and receivers must not empty.')

        message = {
            'content': '',
            'content-type': 'plain',
            'encoding': 'utf-8',
        }

        message['content'] = args['content'] if 'content' in args  else message['content']
        message['content-type'] = args['content-type'] if 'content-type' in args  else message['content-type']
        message['encoding'] = args['encoding'] if 'encoding' in args  else message['encoding']

        mime_message = MIMEText(message['content'], message['content-type'], message['encoding'])
        if 'subject' in args:
            mime_message['Subject'] = Header(args['subject'], message['encoding'])
        if '_from' in args:
            mime_message['From'] = Header(args['_from'], message['encoding'])
        if 'to' in args:
            mime_message['To'] = Header(args['to'], message['encoding'])

        try:
            if not self.smtp:
                self._connect()

            self.smtp.sendmail(sender, receivers, mime_message.as_string())
        except smtplib.SMTPException as e:
            raise e

MAIL_SERVER = 'smtp-mail.outlook.com'
MAIL_PORT = 587
MAIL_USER = ''
MAIL_PASS = ''
RECEIVERS = [
    'sunkeysun@outlook.com',  # Sunkey
]

sender = EmailSender(MAIL_SERVER, MAIL_PORT, MAIL_USER, MAIL_PASS, use_tls=True)
sender.send_email(MAIL_USER, RECEIVERS, 'hello,world')

