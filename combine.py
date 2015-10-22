#!/usr/bin/python

import serial
import smtplib

ser = serial.Serial('/dev/ttyACM0',9600)
sender = 'Chong72082@Yes.My'
receiver = ['lhu@live.com.my']

try:

##read from Arduino 
	ser.readline()
	x = ser.readline()

	message = x

##send email 
        smtpobj = smtplib.SMTP('smtp.gmail.com',587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.login('Chong72082@Yes.My','8d3a10399d')
        smtpobj.sendmail(sender, receiver, message)

except smtplib.SMTPException:
        print "Error"
