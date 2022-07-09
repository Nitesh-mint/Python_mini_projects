import pyautogui
import time
import random

time.sleep(3)

m = ['Hi','hello','namaste',['fuck you']]

while True:
    message = random.randint(0,3)
    pyautogui.typewrite(m[message])
    time.sleep(2)
    pyautogui.press('enter')
    print(m[message])