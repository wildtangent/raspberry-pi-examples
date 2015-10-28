import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

CONTROL_PINS = [22,23,24,25]

for pin in CONTROL_PINS:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, GPIO.LOW)

seq = [
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]
      ]

for i in range(512):
  for halfstep in range(8):
    for pin in range(4):
      GPIO.output(CONTROL_PINS[pin], seq[halfstep][pin])
    time.sleep(0.001)


GPIO.cleanup()


