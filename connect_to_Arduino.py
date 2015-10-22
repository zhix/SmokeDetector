import serial
import smtplib

gas_threshold = 200
temp_threshold = 30

ser = serial.Serial('/dev/ttyACM0',9600)
sender = 'Chong72082@Yes.My'
receiver = ['yo_czx@hotmail.com']

message = """From: DR. DIY (in toilet)
To: Sir Chong and Discipline Team
Subject: THERE IS A SMOKER!! 

Alert!! There is a smoker now in the toilet! 
"""

## this "counter" will check to make sure Dr. DIY does not 
## trigger the email in the beginning stage of the 
## startup when the gas and temp values are inconsistent. 
counter = 0

while 1 :
	ser.readline()
	x = ser.readline()
	y = x.split(";")
	temp = float(y[0])
	gas = float(y[1])
	print(temp,gas)

	if counter > 5 and temp > temp_threshold and gas > gas_threshold:
		try:
		        smtpobj = smtplib.SMTP('smtp.gmail.com',587)
	        	smtpobj.ehlo()
		        smtpobj.starttls()
	        	smtpobj.login('Chong72082@Yes.My','8d3a10399d')
		        smtpobj.sendmail(sender, receiver, message)
			counter = -1000
			print("Msg sent via email successfully!")
			#break

		except smtplib.SMTPException:
		        print "Error"

	counter = counter + 1
