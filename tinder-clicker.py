import time
import random
import webbrowser
from pynput.keyboard import Key, Controller

keyboard = Controller()

def clicker(iteration,min,max):
  n = min
  x = max
  i = iteration
  a = 1
  while a <= i:
   t = random.randint(n,x)
   keyboard.press(Key.right)
   keyboard.release(Key.right)
   #print(a)
   time.sleep(t)
   a = a + 1

# Clicker:
# Do actions in a number A of iterations betweem a B minimum amount of time and a C maximun amount of time
# Usage:
# clicker(A,B,C)

def normalized_clicker():
    webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("http://tinder.com")
    while 1:
        clicker(4,1,8)
        time.sleep(random.randint(1,5))
        keyboard.press(Key.f5)

normalized_clicker()