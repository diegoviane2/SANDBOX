from datetime import datetime
from os import link
import time
import random
from typing import Counter
import webbrowser
from pynput.keyboard import Key, Controller

like_cnt = 0
pause_cnt = 0
refresh_cnt = 0

class Count:
  # Set and Return Counters
  def __init__(self, like, pause, refresh):
    self.like = like
    self.pause = pause
    self.refresh = refresh

  def all(self):
    # Return ALL counters as STRING
    s_like = str(self.like)
    s_pause = str(self.pause)
    s_refresh = str(self.refresh)
    all = s_like +"/"+ s_pause +"/"+ s_refresh

    return all

  def get_like(self):
    # Return LIKE counter as STRING
    s_like = str(self.like)
    return s_like

  def get_pause(self):
    # Return PAUSE counters as STRING
    s_pause = str(self.pause)
    return s_pause

  def get_refresh(self):
    # Return PAUSE counters as STRING
    s_refresh = str(self.refresh)
    return s_refresh
  
  def plus_like(self):
    self.like = self.like + 1
  
  def plus_pause(self):
    self.pause = self.pause + 1
  
  def plus_refresh(self):
    self.refresh = self.refresh + 1
  
class Logger():
  #Log the activities in the console and on a logfile with the given parameters
  
  #old code
  #now = datetime.now()
  #timestamp = now.strftime("%m/%d/%Y %H:%M:%S")
  
  def __init__(self, message, value):
    self.message = message
    self.value = value

  def console(self):
    # Print a notification on CONSOLE
    print(Timer.now() + "\t" + self.message + "\t" + str(self.value))
    
  def file(self):
    # Print a notification on a log FILE
    # For now the log file is fixed
    with open('log.txt', 'a') as file:
          file.write(Timer.now() + "\t" + self.message + "\t" + str(self.value) + "\n")
  
class Key_stroker():
  #Press and release the given key over the keyboard
  keyboard = Controller()

  def __init__(self, key):
    self.key = key
    
  def press(self):
    self.keyboard.press(self.key)
    self.keyboard.release(self.key)
    #For debug purposes
    #log = Logger(str(self.key), str(0))
    #log.Console()

class Timer():
  # Do all time calculations
  def now():
    now = datetime.now()
    timestamp = now.strftime("%m/%d/%y %H:%M:%S")
    return timestamp
  
  def sleep(self,min, max):
    tmp = random.randint(min,max)
    log = Logger("pause", tmp)
    log.console()
    log.file()
    time.sleep(tmp)







def main():
  a = Logger("TESTE", 10)
  a.console()

  b = Timer()
  b.sleep(0,3)


main()