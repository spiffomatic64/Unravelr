#! python3

import threading
import random
import datetime
import time
import signal
import sys
import os

num_threads = 15
min_log = 3
max_log = 20

logginglock = threading.Lock()
threadidlock = threading.Lock()
threadid =  random.randint(123456789,999999999)
loglevel = ["DEBUG","INFO","WARNING","ERROR"]
cpp = ["aaaaa","bbbbb","ccccc","ddddd","eeeee","fffff","ggggg","hhhhh"]


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    os._exit(0)
    
def worker(num):
    global threadid
    time.sleep(random.randint(1,1000)/1000.0)
    
    
    
    threadidlock.acquire()
    threadid += random.randint(1000,100000)
    thisthread = threadid
    threadidlock.release()
    
    for x in range(min_log,max_log):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        file = random.choice(cpp)
        line = random.randint(20,1000)
        loglevelstring = random.choice(loglevel)
        logginglock.acquire()
        print ('%s thread: %d (%s) %s.cpp:%d THIS IS A LOG MESSAGE %d' % (timestamp, threadid, loglevelstring, file, line, num))
        logginglock.release()
        time.sleep(random.randint(1,1000)/1000.0)
    return

threads = []
signal.signal(signal.SIGINT, signal_handler)
for i in range(num_threads):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
    
for thread in threads:
    thread.join()
