
#import serial
#ser = serial.Serial('/dev/ttyACM0',9600)

#while 1 :
#      ser.readline()
#      x = ser.readline()
x = "39.36'C,717\r\n"
y = x.strip(",")
print x
print type(x)
print y
#print type(y)

