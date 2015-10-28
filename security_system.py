import time
import threading
import RPi.GPIO as GPIO

from pir import MyPiPIR
from led import MyPiLed
from buzzer import MyPiBuzzer
from my_logger import MyLogger
from lock import Lock

class SecuritySystem:

  CHECK_INTERVAL = 0.01
  THREADS = []
  CODE = 1234

  def __init__(self):
    self.pir = MyPiPIR(MyPiPIR.DEFAULT)
    self.led = MyPiLed(MyPiLed.RED)
    self.buzzer = MyPiBuzzer(MyPiBuzzer.DEFAULT)
    self.locks = []
    self.tries = 0
    self.max_tries = 3
    self.locks.append(Lock('Vault'))
    
    self.logger = MyLogger("SecuritySystem")
    self.check_interval = self.__class__.CHECK_INTERVAL
    self.enabled = False

  def __check_code(self):
    while self.tries <= self.max_tries:
      code = input("Enter security system code (Tries: " + str(self.max_tries - self.tries) + "): ")
      if str(code) == str(self.__class__.CODE):
        return True
      else:
        self.tries+=1

    self.logger.warn("Code entered incorrectly " + str(self.max_tries) + " times")
    self.buzzer.on()
    return False
      

  # Public implementation (non-blocking)
  def enable(self):
    if self.__check_code():
      self.lockdown()
      if len(self.__class__.THREADS) == 0:
        self.enabled = True
        t = threading.Thread(target=self.__enable)
        t.start()
        self.__class__.THREADS.append(t)
        return t
      else:
        self.logger.warn("Security already active")
        return self.__class__THREADS[0]
    
  # Private implementation (blocking)
  def __enable(self):
    while self.enabled == True:
      state = self.pir.state()
      if state == MyPiPIR.ACTIVATED:
        self.logger.warn("Motion detected!")
        self.buzzer.on()
        self.led.blink(5,0.2)
        time.sleep(1)
      elif state == MyPiPIR.DEACTIVATED:
        self.logger.info("Waiting for motion...")
        self.led.off()
        self.buzzer.off()
      elif state == MyPiPIR.ACTIVE:
        self.logger.warn("Motion still being detected!")
        self.led.blink(5,0.2)
        self.buzzer.on()
        time.sleep(1)
      elif state == MyPiPIR.INACTIVE:
        self.led.off()
        self.buzzer.off()

      time.sleep(self.check_interval)

  # Disable the security system, wait for threads to finish
  def disable(self):
    if self.__check_code():
      self.enabled = False
      self.end_lockdown()
    for t in self.__class__.THREADS:
      t.join()


  def lockdown(self):
    for lock in self.locks:
      lock.lock()

  def end_lockdown(self):
    for lock in self.locks:
      lock.unlock()


