import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = '9109kumar@gmail.com'
EMAIL_PASSWORD = 'prashant91'

msg = EmailMessage()
msg['Subject'] = 'Grab dinner this weekend?'
msg['From'] = EMAIL_ADDRESS
msg['To'] = '9109kumar@gmail.com'
msg.set_content('How about dinner at 6am this Saturday?')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
