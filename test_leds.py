#!/usr/bin/python

# Get LED control class
import RPi.GPIO as GPIO
from led import MyPiLed

try:
  yellow = MyPiLed(MyPiLed.YELLOW)
  red = MyPiLed(MyPiLed.RED)

  # Blink LEDs
  yellow.blink(4,0.5)
  red.blink(5,0.8)

except KeyboardInterrupt:
  print("Quit!")

finally:
  GPIO.cleanup()

