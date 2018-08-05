def sum(a,b):
	return a+b

def diff(a,b):
	return a-b

def times(a,b):
	return a*b

def pow(a,b):
	return a**b

def divide(a,b):
	if b == 0:
		if a > 0:
			return float('inf')
		elif a < 0:
			return -1 * float('inf')
		else:
			return 1
	else:
		return a/b

def surplus(a,b):
	if b == 0:
		return a
	else:
		return a%b

def fact(num):
	if num == 0:
		return 1
	elif num == 1:
		return num
	else:
		return num * fact(num-1)

def inverse(num):
	if num == 0:
		return float('inf')
	else:
		return 1.0/num

if __name__ == '__main__':
	print sum(-5,2)
	print diff(3,9)
	print times(2,0.3)
	print divide(4,0)
	print fact(5)
	print pow(4,0.5)
	print surplus(5,2)