from datetime import *
import datetime
from datetime import *
import subprocess
import time
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
class center_screen():
    def init(width, height):
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