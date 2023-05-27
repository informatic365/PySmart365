AUTHOR = 'Runkang'
COPYRIGHT = '© Copyright 2023 Informatic365 - SmartSoft - MicroSoftware'

import subprocess
import platform

def turn_off(time):
    '''
    Shut down pc directly without gui graphics
    '''
    if time is None or 0:
        subprocess.run(['shutdown', '-s', '-t', '0'])
    else:
        subprocess.run(['shutdown', '-s', '-t', time])
def restart(time):
    if time is None or 0:
        subprocess.run(['shutdown', '-r', '-t', '0'])
    else:
        subprocess.run(['shutdown', '-r', '-t', time])
def restart_with_advancedmode(time):
    if time is None or 0:
        subprocess.run(['shutdown', '-r', '-o', '-t', '0'])
    else:
        subprocess.run(['shutdown', '-r', '-o', '-t', time])
def turn_off_with_gui():
    if platform.