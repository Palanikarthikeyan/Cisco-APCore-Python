import os
import threading
import time
def f1():
    print(f'PID:{os.getpid()} Parent PID:{os.getppid()}')
    print("Thread ID:",threading.get_ident())
    print('Exit from f1 block')

def f2():
    print(f'PID:{os.getpid()} Parent PID:{os.getppid()}')
    print("Thread ID:",threading.get_ident())
    print('Exit from f2 block')

print(f'Main Code block - PID:{os.getpid()}  PPID:{os.getppid()}')
print("Thread ID:",threading.get_ident())
#f1()
#f2()
t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)
t1.start()
time.sleep(1)
t2.start()
t1.join()
t2.join()
print(f'Exit from main block with PID:{os.getpid()} PPID:{os.getppid()}')
