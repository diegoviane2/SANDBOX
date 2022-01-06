from datetime import datetime

import time
import random
import webbrowser
from pynput.keyboard import Key, Controller

g = 0
h = 0

keyboard = Controller()

def clicker(iteration,min,max):
  global g
  n = min
  x = max
  i = iteration
  a = 1
  while a <= i:
   t = random.randint(n,x)
   keyboard.press(Key.right)
   keyboard.release(Key.right)
   time.sleep(random.randint(1,2))
   keyboard.press(Key.right)
   keyboard.release(Key.right)
   now = datetime.now()
   date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
   with open('log.txt', 'a') as file:
     file.write('Like' + ',' + str(g) + ',' + date_time + '\n')
   g = g + 1
   time.sleep(t)
   a = a + 1

# Clicker:
# Do actions in a number A of iterations betweem a B minimum amount of time and a C maximun amount of time
# Usage:
# clicker(A,B,C)

def normalized_clicker(limit):
    global h
    webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("http://tinder.com")
    while limit >= 0:
        clicker(9,0,2)
        keyboard.press(Key.f5)
        h = h + 1
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        with open('log.txt', 'a') as file:
          file.write('Refresh' + ',' + str(h) + ',' + date_time + '\n')  
        limit = limit - 1
        time.sleep(random.randint(1,2))
t = 0
def run_clicker(limit):
  with open('log.txt', 'a') as file:
    file.write('INICIANDO PROGRAMA' + '\n')
  print('INICIANDO PROGRAMA')
  normalized_clicker(limit)
  with open('log.txt', 'a') as file:
    file.write('FIM' + '\n')
  print('FIM')

def automate(loop):
  
    run_clicker(3)