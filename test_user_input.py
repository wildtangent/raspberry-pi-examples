from led import MyPiLed
from my_queue import MyQueue
import os

try:
  yellow = MyPiLed(4)
  red = MyPiLed(17)

  q = MyQueue()
  
  count = 0
  led_choice = 0

  os.system("clear")

  print("Which LED do you want to flash?")
  print("1: Yellow?")
  print("2: Red?")

  led_choice = input("Choose your option: ")

  os.system("clear")
  if led_choice == '1':
    print("You picked the Yellow LED")
    count = input("How many times do you want to blink?: ")
    yellow.blink(int(count), 0.5)
  if led_choice == '2':
    print("You picked the Red LED")
    count = input("How many times do you want to blink?: ")
    red.blink(int(count), 0.5)
except:
  MyPiLed.reset()
