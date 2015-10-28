import time
import RPi.GPIO as GPIO

from pir import MyPiPIR
from led import MyPiLed
from buzzer import MyPiBuzzer
from my_logger import MyLogger

logger = MyLogger("PIR")
logger.debug("PIR Module Test (Ctrl-C to exit)")

pir1 = MyPiPIR(MyPiPIR.DEFAULT)
led1 = MyPiLed(MyPiLed.RED)
buzzer1 = MyPiBuzzer(MyPiBuzzer.DEFAULT)

check_interval = 0.01

try:
  logger.info("Ready!")

  while True:
    state = pir1.state()
    if state == MyPiPIR.ACTIVATED:
      logger.warn("Motion detected!")
      buzzer1.on()
      led1.blink(5,0.2)
      time.sleep(1)
    elif state == MyPiPIR.DEACTIVATED:
      logger.info("Waiting for motion...")
      led1.off()
      buzzer1.off()
    elif state == MyPiPIR.ACTIVE:
      logger.warn("Motion still being detected!")
      led1.blink(5,0.2)
      buzzer1.on()
      time.sleep(1)
    elif state == MyPiPIR.INACTIVE:
      led1.off()
      buzzer1.off()

    time.sleep(check_interval)

except KeyboardInterrupt:
  logger.info("Quit!")


finally:
  GPIO.cleanup()

