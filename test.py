import webbrowser
from pynput.keyboard import Key, Controller
import time

webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("http://tinder.com")


keyboard = Controller()

# Press and release space


a = 1
time.sleep(5)
while a <= 3:
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    a = a + 1
