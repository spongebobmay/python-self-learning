try:
	print 'try...'
	r = 10/int('a')
	print 'result:',r
except ValueError,e:
	print 'ValueError.',e
except ZeroDivisionError,e:
	print 'ZeroDivisionError.',e
finally:
	print 'finally...'
print 'END'
