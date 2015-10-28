import RPi.GPIO as GPIO

class MyPiBuzzer:

  DEFAULT = 27

  def __init__(self, pin):
    self.pin = pin
    self.setup()

  def setup(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(self.pin, GPIO.OUT)

  def on(self):
    GPIO.output(self.pin, GPIO.HIGH)

  def off(self):
    GPIO.output(self.pin, GPIO.LOW)




