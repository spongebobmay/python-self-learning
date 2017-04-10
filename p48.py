width =input('please enter width:')
more_width=width*2
price_width=10
item_width = width - price_width
header_format = '%-*s%*s'
format='%-*s%*.2f'
print '='*width
print header_format %(item_width,'item',price_width,'price')
print'-'*more_width
print format % (item_width,'apples',price_width,0.4)
print format % (item_width,'pears',price_width,0.5)
print format % (item_width,'cantaloupes',price_width,1.92)
print format % (item_width,'dried apricots(16 oz.)',price_width,8)
print format % (item_width,'prunes(4 lbs.)',price_width,12)
print '='*width
