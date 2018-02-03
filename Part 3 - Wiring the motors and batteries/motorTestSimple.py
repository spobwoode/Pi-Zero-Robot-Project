#!/usr/bin/env python

# Import required modules
import time
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
GPIO.setup(7, GPIO.OUT)  # PWMA
GPIO.setup(11, GPIO.OUT) # AIN1
GPIO.setup(12, GPIO.OUT) # AIN2
GPIO.setup(13, GPIO.OUT) # STB
GPIO.setup(15, GPIO.OUT) # BIN1
GPIO.setup(16, GPIO.OUT) # BIN2
GPIO.setup(18, GPIO.OUT) # PWMB

# drive robot clockwise
# Motor A:
GPIO.output(12, GPIO.HIGH) # Set AIN1
GPIO.output(11, GPIO.LOW)  # set AIN2
# Motor B:
GPIO.output(15, GPIO.HIGH) # Set BIN1
GPIO.output(16, GPIO.LOW)  # Set BIN2

# Set the motor speed
# Motor A:
GPIO.output(7, GPIO.HIGH) # set PWMA
# Motor B:
GPIO.output(18, GPIO.HIGH) # set PWMB

# Disable STBY (standby)
GPIO.output(13, GPIO.HIGH)

time.sleep(5)

# Reset the GPIO pins
GPIO.output(12, GPIO.LOW) # AIN1
GPIO.output(11, GPIO.LOW) # AIN2
GPIO.output(7, GPIO.LOW)  # PWMA
GPIO.output(13, GPIO.LOW) # STBY
GPIO.output(15, GPIO.LOW) # BIN1
GPIO.output(16, GPIO.LOW) # BIN2
GPIO.output(18, GPIO.LOW) # PWMB
