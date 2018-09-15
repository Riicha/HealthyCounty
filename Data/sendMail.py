import smtplib

# smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
smtpObj = smtplib.SMTP( [host [, port [, localhost]]] )

sender = 'riicha.r@gmail.com'
receivers = ['riicha_r@yahoo.com']

smtplib.SMTP('mail.your-domain.com', 25)

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"