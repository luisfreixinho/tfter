import pyautogui
import pytesseract
import time
from PIL import Image
from pynput.keyboard import Listener, Key


print("a - Detect status\n"+
      "b - Detect shop\n"+
      "c - Detect field\n")


def on_press(key):

    if hasattr(key, 'char'):
        if key.char == 'a':
            print('Detecting Status')
        elif key.char == 'x':
            exit()


with Listener(on_press=on_press) as listener:  # Setup the listener
    listener.join()  # Join the thread to the main thread