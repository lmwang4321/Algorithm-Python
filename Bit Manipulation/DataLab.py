def isLessOrEqual(x, y):
	ysign = (y >> 31) & 1
	xsign = (x >> 31) & 1
	z = (not (ysign^xsign)) & (((x + ~y) >> 31) & 1)
	return z | ((not ysign)&xsign)

def isAsciiDigit(x):
	neg_0x30 = ~(0x30) + 1
	x_minus_0x30 = x + neg_0x30
	neg_0x3a = ~(0x3a) + 1
	x_minus_0x3a = x + neg_0x3a
	lower_bound_mask = not(x_minus_0x30 >> 31)
	upper_bound_mask = not(not(x_minus_0x3a >> 31))
	return lower_bound_mask & upper_bound_mask

def conditional(x, y, z):
	# x ? y : z
	x = not(not x)
	x = ~x + 1
	return (x & y) | (~x & z)

def isLessorEqual(x, y):
	neg_x = ~x + 1
	y_minus_x = y + neg_x
	return not(y_minus_x >> 31) 

def howmanyBits(x):
	return 1	


#### Draft #####
x = [2]
print(x[:0])