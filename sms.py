import urllib
import urllib.parse
import urllib.request
import json
from my_logger import MyLogger

class SMSPi:


  API_KEY = "f02698566b63e36cc58dcf4bc46f1b41"
  API_URL = "http://www.smspi.co.uk/send/"
  
  def __init__(self, key=None):
    self.key = key or self.__class__.API_KEY
    self.logger = MyLogger("SMS")

  def send(self, to, message):
    values = {
      'to': to,
      'message': message,
      'hash': self.key
    }

    postdata = urllib.parse.urlencode(values)
    encoded_postdata = postdata.encode("utf8")
    req = urllib.request.Request(self.__class__.API_URL, encoded_postdata)
    self.logger.info("Attempting to send SMS")

    try:
      response = urllib.request.urlopen(req)
      response_url = response.geturl()
      if response_url == url:
        self.logger.info(response.read)
    except urllib.error.HTTPError as e:
      self.logger.warn("Send Failed!")
      body = e.read()
      try:
        error = json.loads(str(body))
        self.logger.warn(error['message'])
      except:
        self.logger.warn("Unable to decode reason for failure")
        self.logger.warn(str(body))
