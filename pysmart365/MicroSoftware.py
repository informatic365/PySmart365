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

def sleep(delay: str) -> None:
    if delay == '0' or delay is None:
        time.sleep(0)
    elif delay:
        time.sleep(delay)

class wintools():
    def mrt() -> None:
        if os.path.exists(r"C:\Windows\System32\mrt.exe"):
            pyautogui.hotkey("winleft", "r")
            pyautogui.typewrite("mrt.exe")
            sleep(0.5)
            pyautogui.press("Enter")
        else:
            messagebox.showerror("Error not found", f"Program `mrt.exe` not found.")

    def diskmgmt() -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("diskmgmt.msc")
        sleep(0.5)
        pyautogui.press("Enter")

    def computermgmt() -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("compmgmt.msc")
        sleep(0.5)
        pyautogui.press("Enter")

    def notepad() -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("notepad.exe")
        sleep(0.5)
        pyautogui.press("Enter")

    def calculator() -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("calc.exe")
        sleep(0.5)
        pyautogui.press("Enter")

    def paint() -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("mspaint.exe")
        sleep(0.5)
        pyautogui.press("Enter")

    def taskmgr() -> None:
        pyautogui.hotkey("ctrl", "shift", "esc")

    def explorer() -> None:
        pyautogui.hotkey("winleft", "e")

    def cmd() -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("cmd.exe")
        sleep()
        pyautogui.press("Enter")

    def settings() -> None:
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("ms-settings:")
        sleep(0.5)
        pyautogui.press("Enter")

    def ms_store() -> None:
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
    def clenmgr():
        pyautogui.hotkey("Winleft", "r")
        pyautogui.typewrite("cleanmgr")
        time.sleep(0.5)
        pyautogui.press("Enter")