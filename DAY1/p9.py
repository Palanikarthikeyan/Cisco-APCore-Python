pin_history = [] # empty list

pin = 1234
count = 0
while(count <3):
    p = input('Enter a pinNumber:')
    count = count+1
    if(int(p) == pin):
        pin_history.append(f'Success pin is matched - {count}') # adding new data to an existing list
        print(f'Success pin is matched - {count}')
        break
    else:
        pin_history.append(f'Error - Sorry input pin:{p} is not valid')

if(int(p) != pin):
    print('Sorry your pin is blocked')
    pin_history.append('Sorry your pin blocked')

Choice = input('Wish to see pin history:(Yes | No):')
if(Choice == 'Yes' or Choice == 'YES'):
    for var in pin_history: # iterate a list
        print(var)
        print('') # emptyline

