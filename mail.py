#!/usr/bin/python

import smtplib

sender = 'Chong72082@Yes.My'
receiver = ['yo_czx@hotmail.com']

message = """From: DR. DIY (in toilet)
To: Sir Chong and Discipline Team
Subject: THERE IS A SMOKER!! 

This is a test message
"""

try:
	smtpobj = smtplib.SMTP('smtp.gmail.com',587)
	smtpobj.ehlo()
	smtpobj.starttls()
	smtpobj.login('Chong72082@Yes.My','8d3a10399d')
	smtpobj.sendmail(sender, receiver, message)

except smtplib.SMTPException:
	print "Error"
