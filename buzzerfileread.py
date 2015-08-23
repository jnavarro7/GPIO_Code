#!/usr/bin/python

from sys import argv
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
GPIO.setup(17, GPIO.OUT)

while True:
	
	f = open("test.txt", "r")
	string = f.read(1)
	f.close()
#	print (string)
	time.sleep(1)	
	if string == "0":
		GPIO.output(17, GPIO.HIGH)
		time.sleep(2)
		print "Ethernet Connected"
	elif string == "1":
		GPIO.output(17, GPIO.LOW)
		time.sleep(2)
		print "Ethernet Disconnected"
	else:
		print "will stop"
		break

#	f = open("usbstatus.txt", "r")
#        string = f.read(1)
#        f.close()
#        time.sleep(1)
#        if string == "0":
#                GPIO.output(17, GPIO.HIGH)
#                time.sleep(2)
#                print "USB Connected"
#        elif string == "1":
#                GPIO.output(17, GPIO.LOW)
#                time.sleep(2)
#                print "USB Disconnected"


print "done"
GPIO.cleanup()

