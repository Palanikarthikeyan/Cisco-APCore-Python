'''
app_name = 'demoApp'
app_version = 2.46
app_code = 562
app_status = True
'''

app_name = input('Enter an app name:')
app_version = input(f'Enter {app_name} version:')
app_code = input(f'Enter {app_name} code Number:')
app_status = input(f'Enter {app_name} installation status:')

print(f''' About {app_name} details:-
------------------------------------------------
App name is:{app_name}   Code Number:{app_code}
------------------------------------------------
{app_name} version is:{app_version}
------------------------------------------------
open status:{app_status}
------------------------------------------------''')
