def prod(numbers):
	return reduce(lambda x,y: x*y,numbers)
numbers=[1,2,3,4,4]
print prod(numbers)
