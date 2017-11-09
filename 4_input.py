#!/usr/bin/python
#This program adds a blinking LED

import os
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

#Setup variables for user input
led_choice = 0
count = 0

os.system('clear')
print "Witch LED would you like to blink"
print "1: Red"
print "2: Blue"

led_choice = input("Choose your option: ")

if led_choice == 1:
	os.system('clear')
	print "You picked the Red LED"
	count = input("How many times would you like it to blink?: ")
	while count > 0:
		GPIO.output(27, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(27, GPIO.LOW)
		time.sleep(1)
		count = count -1

if led_choice == 2:
	os.system('clear')
	print "You picked the Blue LED"
	count = input("How many times would you like it to blink?: ")
	while count > 0:
		GPIO.output(17, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(17, GPIO.LOW)
		time.sleep(1)
		count = count -1


#print "Lights on"
#GPIO.output (17, GPIO.HIGH)
#GPIO.output (27, GPIO.HIGH)

#time.sleep(1)

#print "Lights off"
#GPIO.output (17, GPIO.LOW)
#GPIO.output (27, GPIO.LOW)

GPIO.cleanup()
