import RPi.GPIO as GPIO
import time
from stepper_motor import MyPiStepperMotor


try:
  print("Starting FullStep Motor")
  stepper_motor = MyPiStepperMotor(MyPiStepperMotor.DEFAULT, MyPiStepperMotor.FULLSTEP)
  stepper_motor.rotate(90)

  time.sleep(5)

  print("Starting HalfStep Motor")
  stepper_motor2 = MyPiStepperMotor(MyPiStepperMotor.DEFAULT, MyPiStepperMotor.HALFSTEP)
  stepper_motor2.rotate(90)

except KeyboardInterrupt:
  print("Quit!")

finally:
  GPIO.cleanup()

