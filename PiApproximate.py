from random import *
from Calculation import *

NUM_OF_POINTS = 1000000

count = 0
for i in range(NUM_OF_POINTS):
	x = random()
	y = random()

	if pow(x,2) + pow(y,2) <= 1:
		count += 1

print '4 * {} / {} = {}'.format(count,NUM_OF_POINTS,4.0*count/NUM_OF_POINTS)