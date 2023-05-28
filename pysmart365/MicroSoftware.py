from datetime import *
import datetime
from datetime import *
import time
def view_time():
    view_time = datetime.now().strftime("%H:%M:%S")
    return view_time
def view_date():
    view_date = datetime.now().strftime("%d/%m/%Y")
    return view_date