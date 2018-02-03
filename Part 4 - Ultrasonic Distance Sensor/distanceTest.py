#!/usr/bin/env python

# Import required modules
import time
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

trig = 22
echo = 29

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

GPIO.output(trig, 0)

print "waiting for sensor to settle"
time.sleep(2)

try:
    while True:
    	GPIO.output(trig, 1)
    	time.sleep(0.00001)
    	GPIO.output(trig,0)

        while GPIO.input(echo)==0:
        	pulse_start = time.time()

        while GPIO.input(echo)==1:
        	pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance,2)

        print "Distance: ",distance,"cm"
        time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
	print('interrupted!')