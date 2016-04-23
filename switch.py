#!/usr/bin/env python 2.7

import time
import RPi.GPIO as GPIO

class Switch:

 def __init__(self, switchPIN):
  GPIO.setmode(GPIO.BCM)
  #GPIO.setwarnings(False)
  self.switchPIN = switchPIN
  GPIO.setup(switchPIN, GPIO.OUT)

 """
 Turn GPIO port high
 """
 def on(self):
  GPIO.output(self.switchPIN, GPIO.HIGH)
  print("Turn on")

 """
 Turn GPIO port low
 """
 def off(self):
  GPIO.output(self.switchPIN, GPIO.LOW)
  print("Turn off")
 

class Garage(Switch):

 def __init(selfi, PIN):
  Switch.__init__(self, PIN)

 def switcher(self):
  self.on()
  time.sleep(0.5)
  self.off()


if __name__ == "__main__":
 garage = Garage(17)

 try:
  garage.switcher()
 except KeyboardInterrupt:
  print("Interrupt received.Shutting down")
 finally:
  GPIO.cleanup()
 print("Task completed!")
