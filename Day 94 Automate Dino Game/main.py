import pyautogui
import time
import PIL
import PIL.ImageChops
import numpy as np


time.sleep(2)
print(pyautogui.position())

print(pyautogui.pixel(x=377, y=761))
# (83, 83, 83)


# pyautogui.moveTo(1000,500)
#
# pyautogui.PAUSE = 2.5
#
# print(pyautogui.pixel(1000,500))

# x=691, y=686

pyautogui.moveTo(800,715)
pyautogui.move(30,10)
print(pyautogui.pixel(800,700))
#
while True:
    im = pyautogui.screenshot(region=(500,700, 300, 1))

        # getbox checks if there are any nonblack pixels. After inversion it checks if there are any nonwhite pixels
    if  PIL.ImageChops.invert(im).getbbox()  :
        pyautogui.press('space')
        print('hello')

#
# while True:
#     if pyautogui.pixelMatchesColor(1200, 730, (83,83,83), tolerance=20):
#                 pyautogui.press('space')
