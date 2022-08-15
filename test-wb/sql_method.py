import datetime
import time
from threading import Timer
import schedule
import sched

def time_pron():
    now = datetime.datetime.now()
    ts = now.strftime("%Y-%m-%d %H:%M:%S")
    print(ts)
    initialization_token()

def initialization_token(name=None):

    a = sched.scheduler(time.time, time.sleep)
    a.enter(5,1,time_pron())
    a.run()



initialization_token()
