import os
def f1():
    print(f'PID:{os.getpid()} Parent PID:{os.getppid()}')
    print('Exit from f1 block')

def f2():
    print(f'PID:{os.getpid()} Parent PID:{os.getppid()}')
    print('Exit from f2 block')

print(f'Main Code block - PID:{os.getpid()}  PPID:{os.getppid()}')
f1()
f2()
print(f'Exit from main block with PID:{os.getpid()} PPID:{os.getppid()}')
