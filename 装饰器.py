import functools

def log(obj):
    if isinstance(obj,str):
        text=obj
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print 'begin %s %s():' % (text,func.__name__)
                func(*args, **kw)
                print 'end %s %s():' % (text,func.__name__)
            return wrapper
        return decorator

    else:
        func=obj
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print 'begin call %s():' % (func.__name__)
            func(*args, **kw)
            print 'end call %s():' % (func.__name__)
        return wrapper

@log
def now():
    print 'now is \'2017-01-19\''

now()
@log('execute')
def now():
    print 'now is \'2017-01-19\''

now()


    
