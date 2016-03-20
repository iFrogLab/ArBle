/*	This is an example on how to send and receive data from the iFrogLab ArBle via Serial
//
//	Powen Ko
//	Initial Date: 15 May 2016
//	http://www.ifroglab.com/
//
//	To compile:
// 	gcc ser.c -l wiringPi
//
//	To run:
// 	./a.out
*/
#include <wiringSerial.h>
int main(void)
{
	int handle = serialOpen ("/dev/ttyAMA0", 9600);	//Open the Serial port
	serialFlush(handle);	//Clear the stream of old data packets
	while(1)
	{	
		serialPutchar (handle, 's');		//Send 's' to the iFrogLab ArBle
		char inp=serialGetchar(handle);		//Receive the characters from the iFrogLab ArBle
		printf("%c",inp);
	}
	return 0;
}