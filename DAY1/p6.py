'''
Write a python program:
- read a app name from <STDIN>
   - test input app name is Flask (or) flask  - initialize port number is 5000
						config file flask.conf

   - test input app name is fastApi  - initialize port number is 5500
				       config file fastApi.conf

   - test input app name is prometheus - initialize port number is 9090
					 config file prometheus.yaml

   |->default app name - testApp ; port number: 8080 ; config file is:test.conf

- display app name,port number and config filename

'''
app = input('Enter your app name:')
if(app == 'Flask' or app == 'flask'):
    port = 5000
    fname = 'flask.conf'
elif(app == 'fastApi'):
    port = 5500
    fname = 'fastApi.conf'
elif(app == 'prometheus'):
    port = 9090
    fname = 'prometheus.yaml'
else:
    app = 'testApp'
    port = 8080
    fname = 'test.conf'

print(f'''App name:{app}
-----------------------------------------------------
Running port number:{port}  Config filename:{fname}
-----------------------------------------------------''')
    
