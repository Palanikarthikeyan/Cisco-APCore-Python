'''
Write a python program:
 - read a port number from <STDIN>
 - test - input port number 501-599 -- initialize an app name is: testApp
	  -------------------------
				|------initialize an app name is: demoApp

 - display - App name and running port number.

'''
port = input('Enter a port number:')

if(int(port) >500 and int(port) <600):
    app = 'testApp'
else:
    app = 'demoApp'

print(f'App name is:{app} running port number is:{port}')
