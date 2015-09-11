#!/usr/bin/phyton

import smtplib

sender = 'Chong72082@Yes.My'
receiver = ['lhu@live.com.my']

message = """From: From Sir Chong <Chong72082@Yes.My>
To: To Lim <lhu@live.com.my>
Subject: Test

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
