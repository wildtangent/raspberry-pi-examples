import RPi.GPIO as GPIO

class MyPiPIR:

  # Current Pin on GPIO
  DEFAULT = 7

  # States
  INACTIVE = 0
  ACTIVE = 1
  ACTIVATED = 2
  DEACTIVATED = 3

  def __init__(self, pin):
    self.pin = pin
    self.current_state = 0
    self.previous_state = 0
    self.setup()

  def setup(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(self.pin, GPIO.IN)
    # Wait for PIR to settle down
    while GPIO.input(self.pin) == 1:
      self.ready = False
    self.ready = True
    self.current_state = self.__state()

  def __state(self):
    return GPIO.input(self.pin)

  def state(self):
    self.current_state = self.__state()
    if self.current_state == 1 and self.previous_state == 0:
      self.previous_state = 1
      return self.__class__.ACTIVATED
    elif self.current_state == 0 and self.previous_state == 1:
      self.previous_state = 0
      return self.__class__.DEACTIVATED
    elif self.current_state == 1 and self.previous_state == 1:
      return self.__class__.ACTIVE
    elif self.current_state == 0 and self.previous_state == 0:
      return self.__class__.INACTIVE

