def fact(num):
	if num == 0:
		return 1
	elif num == 1:
		return num
	else:
		return num*fact(num-1)

def inverse(num):
	return 1.0 / num

def ExpApproximate():
	e = 0

	for i in range(0,100):
		e = e + inverse(fact(i))
	
	return e


if __name__ == '__main__':
	print ExpApproximate()
	