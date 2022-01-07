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
  normalized_clicker(limit)

def automate(loop):
  print('INICIANDO PROGRAMA')
  with open('log.txt', 'a') as file:
    file.write('INICIANDO PROGRAMA' + '\n')
  webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("http://tinder.com")
  y = 0
  while y <= loop:
    run_clicker(3)
    y = y +1
    time.sleep(random.randint(150,240))
  print('FIM')
  with open('log.txt', 'a') as file:
    file.write('FIM' + '\n')

automate(10)