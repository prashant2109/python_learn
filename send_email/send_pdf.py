import os
import smtplib
import imghdr
from email.message import EmailMessage

print(os.listdir())

EMAIL_ADDRESS = '9109kumar@gmail.com'
EMAIL_PASSWORD = 'prashant91'

msg = EmailMessage()
msg['Subject'] = 'Grab dinner this weekend?'
msg['From'] = EMAIL_ADDRESS
msg['To'] = '9109kumar@gmail.com'
msg.set_content('Checkout image')

files = ['resume.pdf']
for fl in files:
    with open(fl, 'rb') as f:
        file_data = f.read()
        file_name = f.name

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)