from buzzer import MyPiBuzzer
import time

buzzer = MyPiBuzzer(27)
buzzer.on()
time.sleep(4)
buzzer.off()

print("Done!")

