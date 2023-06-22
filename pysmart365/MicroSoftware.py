from datetime import datetime
import os
import sys
import time
from tkinter import messagebox, Tk
from pywinauto import Application
import pyautogui

def view_time():
    view_time = datetime.now().strftime("%H:%M:%S")
    return view_time

def view_date():
    view_date = datetime.now().strftime("%d/%m/%Y")
    return view_date

def sleep(delay):
    if delay == '0' or delay is None:
        time.sleep(0)
    elif delay:
        time.sleep(delay)
    else:
        print("Error")

class center_screen():
    def __init__(self, width: int = None, height: int = None):
        screen_width = Tk().winfo_screenwidth()
        screen_height = Tk().winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry = f"{width}x{height}+{x}+{y}"

class EXIT():
    def __init__(self):
        sys.exit()

class wintools():
    def mrt(self, secs: float) -> None:
        if os.path.exists(r"C:\Windows\System32\mrt.exe"):
            pyautogui.hotkey("winleft", "r")
            pyautogui.typewrite("mrt.exe")
            sleep(0.5)
            pyautogui.press("Enter")
        else:
            messagebox.showerror("Error not found", f"Program `mrt.exe` not found.")

    def diskmgmt(self, secs: float) -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("diskmgmt.msc")
        sleep(secs)
        pyautogui.press("Enter")

    def computermgmt(self, secs: float) -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("compmgmt.msc")
        sleep(secs)
        pyautogui.press("Enter")

    def notepad(self, secs: float) -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("notepad.exe")
        sleep(secs)
        pyautogui.press("Enter")

    def calculator(self, secs: float) -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("calc.exe")
        sleep(secs)
        pyautogui.press("Enter")

    def paint(self, secs: float) -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("mspaint.exe")
        sleep(secs)

    def taskmgr(self) -> None:
        pyautogui.hotkey("ctrl", "shift", "esc")

    def explorer(self) -> None:
        pyautogui.hotkey("winleft", "e")

    def cmd(self, secs: float) -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("cmd.exe")
        sleep(secs)
        pyautogui.press("Enter")

    def settings(self, secs: float) -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("ms-settings:")
        sleep(0.5)
        pyautogui.press("Enter")

    def ms_store(self, secs: float) -> None:
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
            messagebox.showerror("Error not found", "Microsoft Store not found.")
    def runner(command) -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite(command)
        time.sleep(0.5)
        pyautogui.press("Enter")
