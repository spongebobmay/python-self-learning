import hashlib
def login(user,password):
    if db.get(user) and password==db[user]:
        return True
    else:
        return False
db={
    'michael':'e10adc3949ba59abbe56e057f20f883e',
    'bob':'878ef96e86145580c38c87f0410ad153',
    'alice':'99b1c2188db85afee403b1536010c2c9'
}    
user=raw_input('please enter your username:')
password=raw_input('please enter your password:')
md5=hashlib.md5()
md5.update(password)
passwordmd5=md5.hexdigest
print login(user,passwordmd5)
