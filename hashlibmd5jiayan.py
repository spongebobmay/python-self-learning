import hashlib
def get_md5(str):
    md5=hashlib.md5()
    md5.update(str) 
    return md5.hexdigest()
db={'bob': 'ab3c191f9da06b3980202c1400f2c476',
'michael': 'b72105ea74b52f07b842b6c6f6c1fb6f',
'mabel': '8e4772abc7972b5915c1f8239baa9687'}
def register(username,password):
    db[username]=get_md5(password+username+'the-salt')
    print 'register successfully'
def login(user,password):
    if get_md5(password+user+'the-salt')==db[user]:
        print 'login successfully'
    else:
        print 'password wrong'
if __name__ == '__main__':
    user=raw_input('please enter your username:')
    password=raw_input('please enter your password:')
    if user in db:
        login(user,password)
    else:
        register(user,password)

