name = raw_input('what is your name?')
if name.endswith('Gumby'):
    if name.startswith('Mr.'):
        print'hello,Mr.Gumby'
    elif name.startswith('Mrs.'):
        print'hello,Mrs.Gumby'
    else:
        print'hello,Gumby'
else:
    print 'hello,stranger'
