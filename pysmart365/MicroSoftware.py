from datetime import *
import datetime
from datetime import *
import subprocess
from pywinauto import Application
import os
import sys
import time
from tkinter import messagebox

import pyautogui
from screeninfo import get_monitors
def view_time():
    view_time = datetime.now().strftime("%H:%M:%S")
    return view_time
def view_date():
    view_date = datetime.now().strftime("%d/%m/%Y")
    return view_date
def sleep(delay):
    if delay == '0' or None:
        sleep = time.sleep(0)
        return sleep
    elif delay:
        sleep1 = time.sleep(delay)
        return sleep1
    else:
        print("Error")
def center_screen(width, height):
    try:
        monitors = get_monitors()
        if monitors:
            monitor = monitors[0]
            screen_width = monitor.width
            screen_height = monitor.height
            sw = (screen_width - width) // 2
            sh = (screen_height - height) // 2
            text = f'{width}x{height}+{sw}+{sh}'
            return text
        else:
            return None
    except Exception as error:
        print('Error: ', error)

class EXIT():
    def __init__(self):
        sys.exit()
class wintools():
    def mrt(secs: float) -> None:
        if os.path.exists(f'C:\Windows\System32\mrt.exe'):
            pyautogui.hotkey("winleft", "r")
            pyautogui.typewrite("mrt.exe")
            sleep(0.5)
            pyautogui.press("Enter")
        else:
            messagebox.showerror("Error not found", f"Programm `mrt.exe` not found.")
    def diskmgmt(secs: float) -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("diskmgmt.msc")
        time.sleep(secs)
        pyautogui.press("Enter")
    def computermgmt(secs: float) -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("compmgmt.msc")
        sleep(secs)
        pyautogui.press("Enter")
    def notepad(secs: float) -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("notepad.exe")
        time.sleep(secs)
        pyautogui.press("Enter")
    def calculator(secs: float) -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("calc.exe")
        time.sleep(secs)
        pyautogui.press("Enter")
    def paint(secs: float) -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("mspaint.exe")
        time.sleep(secs)
    def taskmgr() -> None:
        pyautogui.hotkey("ctrl", "shift", "esc")
    def explorer() -> None:
        pyautogui.hotkey("winleft", "e")
    def cmd(secs: float) -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("cmd.exe")
        time.sleep(secs)
        pyautogui.press("Enter")
    def settings(secs: float) -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("ms-settings:")
        sleep(0.5)
        pyautogui.press("Enter")
    def ms_store(secs: float) -> None:
        def check_microsoft_store():
            try:
                app = Application(backend='uia').start("ms-windows-store://")
                app.kill()
                return True
            except Exception:
                return False

        if check_microsoft_store():
            pyautogui.hotkey("winleft", "r")
            pyautogui.typewrite("ms-windows-store://")
            sleep(0.5)
            pyautogui.press("Enter")
        else:
            messagebox.showerror("Error not found", "Microsoft store not found.")