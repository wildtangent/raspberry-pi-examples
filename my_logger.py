import time
from datetime import datetime

class MyLogger:
  def __init__(self, name, format=None):
    self.name = name
    if format is None:
      self.format = "%H:%M:%S, %a %d/%m/%Y"
    else:
      self.format = format

  def log(self, msg):
    print("[" + self.name + "] [" + self.timestamp() + "] " + msg)

  def info(self, msg):
    self.log(msg)

  def debug(self, msg):
    self.log(msg)

  def warn(self, msg):
    self.log(msg)

  def timestamp(self):
    return datetime.now().strftime(self.format)
  

