AUTHOR = 'Runkang'
COPYRIGHT = '© Copyright 2023 Informatic365 - SmartSoft - MicroSoftware'

import subprocess
import platform
from customtkinter import *
from tkinter import messagebox
import sys

def turn_off(time: float) -> None:
    '''
    Shutdown pc directly without gui graphics.
    '''
    if time is None or 0:
        subprocess.run(['shutdown', '-s', '-t', '0'])
    else:
        subprocess.run(['shutdown', '-s', '-t', f'{time}'])
def restart(time: float) -> None:
    '''
    Restart pc with or without time
    '''
    if time is None or 0:
        subprocess.run(['shutdown', '-r', '-t', '0'])
    else:
        subprocess.run(['shutdown', '-r', '-t', f'{time}'])
def restart_with_advancedmode(time: float) -> None:
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
        pass
    else:
        subprocess.run(['slidetoshutdown'])
def copyright_view(year, company):
    '''
    Enter the copyright text that will be displayed with the name that you can customize and the year using the attribute 'company' for the name and 'year' for the year.
    Example if i write copyright_view(year='2022 - 2023', company= 'Informatic365')
    then displays "© Copyright 2022 - 2023 Informatic365".
    '''
    get = f'© Copyright {year} {company}'
    return get
class close():
    def __init__(self) -> None:
        sys.exit()