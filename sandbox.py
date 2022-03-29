import threading
from threading import Thread, Lock
from time import sleep

result = []
value = 0
locker = threading.Lock()

def add_value():
    global result
    global value
    while True:
        locker.acquire()
        result.append(value)
        value += 1
        print(result)
        locker.release()
        sleep(4)

for _ in range(5):
    th = threading.Thread(target=add_value)
    th.start()

th.join()