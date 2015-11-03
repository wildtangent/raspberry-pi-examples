import RPi.GPIO as GPIO
from stepper_motor import MyPiStepperMotor

stepper = MyPiStepperMotor(MyPiStepperMotor.DEFAULT)

stepper.rotate(-90)
stepper.rotate(90)

