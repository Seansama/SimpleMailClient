import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Change this to your preferred internet mail host and port
server.ehlo()
# server.starttls()
with open('text.txt', 'r') as f:
    password = f.read()

server.login('eobardtesting@gmail.com', password)  # Edit the user to your own email address

msg = MIMEMultipart()
msg['From'] = 'Eobard'
msg['To'] = 'shawnramito@gmail.com'  # Should be the recipient email.
msg['Subject'] = 'Mail client testing'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'img.png'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('eobardtesting@gmail.com', 'shawnramito@gmail.com', text)
# From address should be the email address provided for the user and the to address should be the recipient email.
