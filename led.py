#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import threading

class MyPiLed:

  RED = 17
  YELLOW = 4
  THREADS = []

  def __init__(self, pin):
    self.pin = pin
    self.setup()

  def setup(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(self.pin, GPIO.OUT)
    self.off()

  def on(self):
    GPIO.output(self.pin, GPIO.HIGH)

  def off(self):
    GPIO.output(self.pin, GPIO.LOW)

  def wait(self, seconds):
    time.sleep(seconds)
  
  # Threaded (non-blocking) implementation of blink
  def blink(self, times, speed, block=False):
    if block == False:
      t = threading.Thread(target=self.__blink, args=(times, speed))
      self.__class__.THREADS.append(t)
      t.start()
      return t # so we can synchronise threads outside of the class
    else:
      self.__blink(times, speed)

  # Non-threaded (blocking), private implementation of blink
  def __blink(self, times, speed):
   for num in range(times):
      self.on()
      self.wait(speed)
      self.off()
      self.wait(speed)
