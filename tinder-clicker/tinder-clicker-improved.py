###
#  Tinder Clicker Open a selected webbrowser and stroke the RIGHT keyboard key over a Tinder profile
#  like pressing the like button to swipe right
#  Written by Diego Viane https://github.com.br/diegoviane2
###
# Dependencies
from datetime import datetime
from os import link
import time
import random
from typing import Counter
import webbrowser
from pynput.keyboard import Key, Controller

# Code

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
    self.pause = self.pause
  
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

class Timer():
  # Do all time calculations
  def now():
    now = datetime.now()
    timestamp = now.strftime("%m/%d/%y %H:%M:%S")
    return timestamp
  
  def sleep(self,min, max):
    tmp = random.randint(min,max)
    log = Logger("PAUSA", tmp)
    log.console()
    log.file()
    time.sleep(tmp)

def main():
 #somecode
 
 count = Count(like_cnt, pause_cnt, refresh_cnt)

 log = Logger("INICIANDO PROGRAMA", count.all())
 log.console()
 log.file()
 # webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("http://tinder.com")
 i = 0
 s = random.randint(6,20)
 while i < s:
  key = Key_stroker(Key.right)
  k = 0
  j = random.randint(2,12)
  print("LAÇO repete: " + str(j) + " vezes")
  while k < j:
    count.plus_like()
    log = Logger("LIKE", count.get_like())
    key.press()
    log.console()
    log.file()
    time = Timer()
    time.sleep(1,4)
    k = k + 1

    count.plus_refresh()
    log = Logger("REFRESH", count.get_refresh())
    key = Key_stroker(Key.f5)
    log.console()
    log.file()
    time = Timer()
    time.sleep(30,60)
  i = i + 1
 log = Logger("FINALIZANDO PROGRAMA", count.all())
 log.console()
 log.file()
 
main()


