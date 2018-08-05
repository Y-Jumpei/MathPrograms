from Calculation import *

def NapirsApproximate():
	e = 0

	for i in range(0,100):
		e = e + inverse(fact(i))
	
	return e


if __name__ == '__main__':
	print NapirsApproximate()
	