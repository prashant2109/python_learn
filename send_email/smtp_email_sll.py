import os
import smtplib
EMAIL_ADDRESS = '9109kumar@gmail.com'
EMAIL_PASSWORD = 'prashant91'


# python -m smtpd -c DebuggingServer -n localhost:1025 # debug using local host
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Grab dinner this weekend?'
    body = 'How about dinner at 6am this Saturday?'

    msg = f'Subject: {subject}\n\n{body}'
    # print (msg)
    smtp.sendmail(EMAIL_ADDRESS, '9109kumar@gmail.com', msg)