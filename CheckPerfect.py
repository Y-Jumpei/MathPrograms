def isPerfect(num):
	sum = 0
	for i in range(1,num+1):
		if num % i == 0:
			sum += i
	
	if sum == 2 * num and num != 0:
		return True
	else:
		return False


if __name__=='__main__':
	for num in range(100):
		if isPerfect(num):
			print '{} is Perfect Number!'.format(num)
		else:
			print '{} is not Perfect Number...'.format(num)
