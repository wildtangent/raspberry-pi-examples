from led import MyPiLed

led1 = MyPiLed(MyPiLed.RED)
led2 = MyPiLed(MyPiLed.YELLOW)

print("Non blocking")
threads = []
threads.append(led1.blink(20,0.5))
threads.append(led2.blink(30,0.2))
for t in threads:
  t.join()

print("Blocking")
led1.blink(5,0.5,True)
led2.blink(5,0.5,True)


