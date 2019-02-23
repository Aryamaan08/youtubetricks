import time
import pyautogui

time.sleep(5)
pyautogui.typewrite(['a', 'w', 'e', 's', 'o', 'm', 'e'], interval=0.4)
time.sleep(5)
pyautogui.typewrite(['a', 'w', 'e', 's', 'o', 'm', 'e'], interval=0.4)
time.sleep(2)
for i in range(0, 2):
    pyautogui.keyDown('c')
    pyautogui.keyUp('c')
    time.sleep(0.4)
time.sleep(2)
for j in range(0, 2):
    pyautogui.keyDown('m')
    pyautogui.keyUp('m')
    time.sleep(0.4)
time.sleep(2)
pyautogui.keyDown('t')
pyautogui.keyUp('t')
time.sleep(1)
pyautogui.keyDown('k')
pyautogui.keyUp('k')
