database=[
	['albert','1234'],
	['dilbert','4242'],
	['smith','7524'],
	['jones','9843']
        ]
username = raw_input('user name:')
pin = raw_input('pin code:')
if [username,pin] in database: print'access granted'
        
