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

except KeyboardInterrupt:
  logger.info("Quit!")
  if security_system.enabled:
    security_system.disable()

finally:
  security_system.cleanup()
  
  GPIO.cleanup()

