from stepper_motor import MyPiStepperMotor
from my_logger import MyLogger

class Lock:
  def __init__(self, name):
    self.name = name
    self.motor = MyPiStepperMotor(MyPiStepperMotor.DEFAULT)
    self.logger = MyLogger('Lock')

  #def reset(self):
    # TODO Should reset to known orientation

  def lock(self):
    self.logger.info("Locking " + self.name)
    self.motor.rotate(90)

  def unlock(self):
    # FIXME should rotate anticlockwise
    self.logger.info("Unlocking " + self.name)
    self.motor.rotate(-90)
