class Complex():
	def __init__(self,x,y):
		self.set(x,y)

	def set(self,x,y):
		self.x = x
		self.y = y

	def __str__(self):
		if self.x != 0:
			if self.y == 1:
				return '{}+i'.format(self.x)
			elif self.y == -1:
				return '{}-i'.format(self.x)
			elif self.y > 0:
				return '{}+{}i'.format(self.x,self.y)
			elif self.y < 0:
				return '{}{}i'.format(self.x,self.y)
			else:
				return '{}'.format(self.x)
		else:
			if self.y == 1:
				return 'i'
			elif self.y == -1:
				return '-i'
			elif self.y == 0:
				return '0'
			else:
				return '{}i'.format(self.y)

	def __add__(self,other):
		return Complex(self.x + other.x, self.y + other.y)

	def __sub__(self,other):
		return Complex(self.x - other.x, self.y - other.y)

	def __mul__(self,other):
		return Complex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)

if __name__=='__main__':
	a = Complex(1,1)
	b = Complex(1,-1)
	c = Complex(1,2)
	d = Complex(1,-2)
	e = Complex(1,0)
	f = Complex(0,1)
	g = Complex(0,-1)
	h = Complex(0,0)
	i = Complex(0,2)

	print a
	print b
	print c
	print d
	print e
	print f
	print g
	print h
	print i

	print (a+c)
	print (a-c)
	print (a*c)