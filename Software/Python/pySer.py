#	This is an example on how to send and receive data from the iFrogLab ArBle via Serial
#
#	Powen Ko
#	Initial Date: 15 May 2016
#	http://www.ifroglab.com/
#!/usr/bin/python
import serial
ser = serial.Serial('/dev/ttyAMA0',  9600, timeout = 0)	#Open the serial Port
ser.flushInput()	# Clear the input buffer

#Recieve a line from the iFrogLab ArBle and return it back
def receive():
  while True:
	state = ser.readline()
	if len(state):	#If something was read from the Serial Port, read and return the line
		return state
 
#Send data to the iFrogLab ArBle
def send(input):
	ser.write(input)
	
while True:
	try:
		send('s')
		print receive(),
	except KeyboardInterrupt:	#If program is terminated, close the serial port before exiting
		ser.close()