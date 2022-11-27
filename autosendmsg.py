import pyautogui
import time

time.sleep(4)
count=0
while count<=5:
    pyautogui.typewrite('what')
    pyautogui.press ('enter')
    count+=1