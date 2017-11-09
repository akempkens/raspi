#!/usr/bin/python
#This program adds a blinking LED

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup (17, GPIO.OUT)
GPIO.setup (27, GPIO.OUT)

print "Lights on"
GPIO.output (17, GPIO.HIGH)
GPIO.output (27, GPIO.HIGH)

time.sleep(1)

print "Lights off"
GPIO.output (17, GPIO.LOW)
GPIO.output (27, GPIO.LOW)

GPIO.cleanup()
