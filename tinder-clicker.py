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
   with open('log.txt', 'a') as file:
     file.write('Like' + ',' + str(g) + '\n')
   g = g + 1
   time.sleep(t)
   a = a + 1

# Clicker:
# Do actions in a number A of iterations betweem a B minimum amount of time and a C maximun amount of time
# Usage:
# clicker(A,B,C)

def normalized_clicker():
    global h
    webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("http://tinder.com")
    while 1:
        clicker(4,1,8)
        time.sleep(random.randint(1,3))
        keyboard.press(Key.f5)
        h = h + 1
        with open('log.txt', 'a') as file:
          file.write('Refresh' + ',' + str(h) + '\n')  

normalized_clicker()