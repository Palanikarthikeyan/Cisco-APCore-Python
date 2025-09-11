'''Avoid race condition '''
import threading
counter = 0
def f1():
    global counter
    for var in range(100000000):
        with lock: 
            counter += 1 # Only one thread updates the counter value at a time

lock = threading.Lock()

for var in range(5):
    t1 = threading.Thread(target=f1)
    t2 = threading.Thread(target=f1)
    t1.start()
    t2.start()
    

print('Counter value:',counter)
