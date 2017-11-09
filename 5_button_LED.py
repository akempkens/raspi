#!/usr/bin/python
#This program adds a blinking LED

import os
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Setup variables for user input
led_choice = 0
count = 0
button = GPIO.input(10)

os.system('clear')
print "Blink LED based on button pressed"
print "Button State = " + str(button)
print "Witch LED would you like to blink"
print "1: Red"
print "2: Blue"
print "3: Both"
led_choice = input("Choose your option? ")

def ledON(led_choice):
	"function to switch the LED on"
	if led_choice == 1:
		print "Red LED on"
		GPIO.output(27, GPIO.HIGH)

	if led_choice == 2:
		print "Blue LDE on"
		GPIO.output(17, GPIO.HIGH)
		
	if led_choice == 3:
		print "Blue and Red LDE on"
		GPIO.output(17, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		
	return

def ledOFF(led_choice):
	"function to switch the LED off"
	if led_choice == 1:
		print "Red LED off"
		GPIO.output(27, GPIO.LOW)

	if led_choice == 2:
		print "Blue LDE off"
		GPIO.output(17, GPIO.LOW)
		
	if led_choice == 3:
		print "Blue and Red LDE off"
		GPIO.output(17, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
	return

try:
	print "Please press the button"
	buttonState = 0
	while True:
	    if ( GPIO.input(10) == False ):
	    	print("Button Pressed")
	    	os.system('date') # print the systems date and time
	    	ledON(led_choice)
	    	buttonState = 1
	    elif ( GPIO.input(10) == True and buttonState == 1 ):
			os.system('clear')
			print("Button freed - please press the button")
			ledOFF(led_choice)
			buttonState = 0

except KeyboardInterrupt:
	GPIO.cleanup()

print "Bye bye and thx for the fish."
