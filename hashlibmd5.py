import hashlib
def calc_md5(password):
    md5=hashlib.md5()
    md5.update(password)
    print md5.hexdigest()
password= raw_input('please enter your password:')
calc_md5(password)
    
