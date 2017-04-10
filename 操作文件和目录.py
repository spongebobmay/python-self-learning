import os
def search(s, dir = os.path.abspath('.')):
    m = 0
    for x in os.listdir(dir):
        current_dir = os.path.join(dir,x)
        if os.path.isdir(current_dir):
            m = m + search(s, dir=os.path.abspath(current_dir))
        if os.path.isfile(current_dir) and s in x:
            print current_dir
            m = m + 1
    return m 

str = raw_input('Input the keys you want to search:')
x = search(str)
print 'Totally %d files matched.' % x
