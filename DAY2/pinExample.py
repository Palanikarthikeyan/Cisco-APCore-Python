import time
'''This is pin Number validation code'''
def pinTest():
    '''pinTest - simple function call'''
    Wobj = open('pinHistory.log','a')
    pin = 1234
    count = 0
    while(count < 3):
        p = input('Enter a pinNumber:')
        count = count + 1
        if(int(p) == pin):
            Wobj.write(f'Success - matched - {count} - Input date/time:{time.ctime()}\n')
            print(f'Success - matched - {count} - Input date/time:{time.ctime()}')
            break
        else:
            Wobj.write(f'Failed - User input pinNumber:{p} - Input date/time:{time.ctime()}\n')
    if(int(p) != pin):
        Wobj.write(f'Pin is Blocked - Entry time is:{time.ctime()}\n')
        print(f'Pin is Blocked')
    Wobj.close()
