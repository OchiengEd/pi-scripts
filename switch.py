#!/usr/bin/env python 2.7

import time
import RPi.GPIO as GPIO

class Switch:

 """
 def __init__(self):
  GPIO.setmode(GPIO.BCM)
  switchPIN = 17 # Pin 11 on the Pi
  GPIO.setup(switchPIN, GPIO.OUT)
  """

 """
 Turn GPIO port high
 """
 def on(self, GPIO_PIN):
  #GPIO.output(GPIO_PIN, GPIO.HIGH)
  print("Turn on")

 """
 Turn GPIO port low
 """
 def off(self, GPIO_PIN):
  #GPIO.output(GPIO_PIN, GPIO.LOW)
  print("Turn off")
 

if __name__ == "__main__":
 switch = Switch()
 switch.on(17)
 print("Task completed!")
