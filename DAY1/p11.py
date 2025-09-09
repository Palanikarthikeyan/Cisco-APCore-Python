devices = [] # empty list
count = 0
while(count < 5):
    device_input = input('Enter a device name:')
    if(device_input):
        devices.append(device_input) # adding input device to an existing list
    else:
        print('Sorry your input is missing')
    count = count + 1


if(devices):
    for var in devices:
        print(f'device name:{var}')
else:
    print('Empty list')

print(f'\nTotal no.of devices:{len(devices)}')