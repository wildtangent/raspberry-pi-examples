import time
import RPi.GPIO as GPIO
from security_system import SecuritySystem
from my_logger import MyLogger

try:
  logger = MyLogger("SecurityTester")
  logger.info("Started security system test")
  security_system = SecuritySystem()
  logger.info("Security system enabled")
  security_system.enable()

  for i in range(10):
    logger.info("Active for " + str(10-i) + " more seconds")
    time.sleep(1)


  security_system.disable()
  logger.info("Security system disabled")

except KeyboardInterrupt:
  logger.info("Quit!")
  if security_system.enabled:
    security_system.disable()

finally:
  GPIO.cleanup()

