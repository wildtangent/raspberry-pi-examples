from my_queue import MyQueue
from led import MyPiLed


try:
  # Running code
  led1 = MyPiLed(MyPiLed.YELLOW)
  led2 = MyPiLed(MyPiLed.RED)

  q = MyQueue()
  q.put([led1, 50, 0.1])
  q.put([led2, 10, 0.5])

  q.join()

  q.clear()

except KeyboardInterrupt:
  q.clear()
  led1.off()
  led2.off()
  MyPiLed.reset()
