## **iFrogLab ArBle**
This project combines the brains of a Raspberry Pi with the brawn of an Arduino and Bluetooth 4.0 Ble.  [Read more about the iFrogLab ArBle here.](http://www.iFrogLab.com)

![Picture](iFrogLabArble_Logo_4.jpg)

These files have been made available online through a [Creative Commons Attribution-ShareAlike 3.0](http://creativecommons.org/licenses/by-sa/3.0/) license.

## Getting Started

We've devoted some serious time to trying to make sure that it's easy to get started.  If you're lost, we would like to first direct you to our [website for the iFrogLab ArBle] (http://www.iFrogLab.com/)

## This Repository

This repository only holds firmware and hardware designs.  
**Python** - If you're looking for our iFrogLab ArBle Python libraries, look here:	https://github.com/iFrogLab/ArBle
	
**C** - If you're looking for the iFrogLab ArBle C Libraries, look here: 		https://github.com/iFrogLab/ArBle
	
**Scratch** - If you're looking for the iFrogLab ArBle Scratch libraries, look here:	https://github.com/iFrogLab/ArBle

**Script** - If you're looking for the iFrogLab ArBle Scripts for installing the softwares and other settings on the Raspberry PI, look here:	https://github.com/iFrogLab/ArBle/tree/master/script

## Image for the SD Card
Our custom image for the Raspberry Pi makes using the iFrogLab ArBle easy.  We've modified wheezy a little bit.  You can download the latest image [here.](http://www.dexterindustries.com/howto/raspberry-pi-tutorials/install-raspbian-for-robots-image-on-an-sd-card/)
	
## Firmware
The board firmware is made in Arduino in order to make it super-hackable.  The firmware is written in Arduino 1.0 and can be uploaded directly from the Raspberry Pi itself .

The board supports most of the Arduino sensors and shields and can interact with the Raspberry Pi via I2C and Serial and SPI is used for code burning.

## Pin Description
![ iFrogLab ArBle Upload ](iFrogLabArble_hardware_description.png)

## Uploading the Code to iFrogLab ArBle
Select the programmer as "Raspberry Pi GPIO"and Use CTRL + Shift + U to Upload the Code to the iFrogLab ArBle

![iFrogLab ArBle Upload](uploadProgram.JPG)


[iFrogLab ArBle.] (http://www.iFrogLab.com)