class Nary():
	def __init__(self,N):
		if 1 < N <= 10 and type(N) is int:
			self.N = N
			self.num = 0
		else :
			print 'N must be 2~10. Treated as 10-ary'
			self.N = 10
			self.num = 0
	
	def __str__(self):
		return '{}({})'.format(self.num,self.N)
	
	def set_num(self,num):
		if type(num) is int and num >= 0:
			count = 0
		
			while num != 0:
				self.num += (10**count)*(num%self.N)
				num = num / self.N
				count += 1
		
		else:
			raise TypeError('Type Error:num must be positive integer.')

if __name__ == '__main__':
	try:
		x = Nary(2.1)
		x.set_num(-1)
		print x
	except TypeError as e:
		print e