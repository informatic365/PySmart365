AUTHOR = 'Runkang'
COPYRIGHT = '© Copyright 2023 Informatic365 - SmartSoft - MicroSoftware'

import subprocess
import platform
from customtkinter import *
from tkinter import messagebox

def turn_off(time):
    '''
    Shutdown pc directly without gui graphics.
    '''
    if time is None or 0:
        subprocess.run(['shutdown', '-s', '-t', '0'])
    else:
        subprocess.run(['shutdown', '-s', '-t', f'{time}'])
def restart(time):
    '''
    Restart pc with or without time
    '''
    if time is None or 0:
        subprocess.run(['shutdown', '-r', '-t', '0'])
    else:
        subprocess.run(['shutdown', '-r', '-t', f'{time}'])
def restart_with_advancedmode(time):
    '''
    Restart pc to advanced mode available on WIndows 10 and 11 or successive version.
    '''
    if time is None or 0:
        subprocess.run(['shutdown', '-r', '-o', '-t', '0'])
    else:
        subprocess.run(['shutdown', '-r', '-o', '-t', f'{time}'])
def turn_off_with_gui():
    '''
    Turn Off pc with gui available on Windows 10 and 11 or successive version.
    '''
    check_windows_version = platform.win32_ver()[0]
    if check_windows_version == '7' or '8':
        shutdowngui = CTk()
        width = 200
        height = 100
        x = (shutdowngui.winfo_screenwidth() - width) // 2
        y = (shutdowngui.winfo_screenheight() - height) // 2
        shutdowngui.geometry(f"{width}x{height}+{x}+{y}")
        shutdowngui.title("Turn Off pc in gui mode")
        shutdown = CTkButton(shutdowngui, text="Turn Off", command=lambda: turn_off(time=0))
        shutdown.place(relx=0.5, rely=0.5, anchor='center')
        shutdowngui.mainloop()
    else:
        subprocess.run(['slidetoshutdown'])