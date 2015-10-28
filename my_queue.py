#!/usr/bin/python

from queue import Queue
from threading import Thread

class MyQueue:

  def __init__(self):
    self.setup()

  def run(self, queue):
    while True:
      item = queue.get()
      if item is None:
        break
      led = item[0]
      count = item[1]
      speed = item[2]
      led.blink(count, speed)
      queue.task_done()

  def setup(self):
    self.queue = Queue(maxsize=0)
    self.num_threads = 10
    self.threads = []

    for i in range(self.num_threads):
      worker = Thread(target=self.run, args=(self.queue,))
      worker.setDaemon(True)
      worker.start()
      self.threads.append(worker)

  def put(self, item):
    self.queue.put(item)

  def join(self):
    self.queue.join()

  def clear(self):
    for i in range(self.num_threads):
      self.queue.put(None)
    for t in self.threads:
      t.join()

