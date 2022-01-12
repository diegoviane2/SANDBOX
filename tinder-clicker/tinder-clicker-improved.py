from datetime import datetime
import time
import random
from typing import Counter
import webbrowser
from pynput.keyboard import Key, Controller

cnt = 0

def counter():
  global cnt
  cnt = cnt + 1

class Logger():
  #Log the activities in the console and on a logfile with the given parameters
  now = datetime.now()
  timestamp = now.strftime("%m/%d/%Y %H:%M:%S")
  
  def __init__(self, message, value):
    self.message = message
    self.value = value

  def Console(self):
    print(self.timestamp + "\t" + self.message + "\t" + str(self.value))
    
  def File(self):
    with open('log.txt', 'a') as file:
          file.write(self.timestamp + "\t" + self.message + "\t" + str(self.value) + "\n")
  

class Key_stroker():
  keyboard = Controller()

  def __init__(self, key):
    self.key = key
    
  def Press(self):
    self.keyboard.press(self.key)
    self.keyboard.release(self.key)
    print("Tecla " + str(self.key))

