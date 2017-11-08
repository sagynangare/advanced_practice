import threading
import time

def sleeper(n, name):
    print("Hi, I'm {} going to sleep for 5 sec. \n".format(name))
    time.sleep(n)
    print("{} has woken up from sleep \n".format(name))
th = threading.Thread(target = sleeper, name='thread1',
                      args = (5, 'thread1'))
th.start()
th.join()

print('Hello')
print('Hello')

