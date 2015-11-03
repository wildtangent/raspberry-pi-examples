import RPi.GPIO as GPIO
import time

class MyPiStepperMotor:

  DEFAULT = [22,23,24,25]

  RESOLUTION = 512

  HALFSTEP = 'HALFSTEP'
  FULLSTEP = 'FULLSTEP'

  HALFSTEP_SEQ = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
  ]

  FULLSTEP_SEQ = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
  ]

  def __init__(self, pins, stepping_mode=None):
    self.pins = pins
    if stepping_mode == self.__class__.FULLSTEP:
      self.seq = self.__class__.FULLSTEP_SEQ
      self.wait_time = 0.002
    else:
      self.seq = self.__class__.HALFSTEP_SEQ
      self.wait_time = 0.001

    self.setup()

  def setup(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pin in self.pins:
      GPIO.setup(pin, GPIO.OUT)
      GPIO.output(pin, GPIO.LOW)

  def rotate(self, degrees):
    rng = self.__range_from_degrees(degrees)

    # check if se are going in reverse
    if rng < 0:
      reverse = True
      rng = abs(rng)

    for i in range(rng):
      for step in range(len(self.seq)):
        for pin in range(len(self.pins)):
          if reverse:
            # Go in reverse
            GPIO.output(self.pins[pin], self.seq[len(self.seq)-step][pin]))
          else:
            GPIO.output(self.pins[pin], self.seq[step][pin])
        time.sleep(self.wait_time)

  def __range_from_degrees(self, degrees):
    return int(degrees * (self.__class__.RESOLUTION/360))







