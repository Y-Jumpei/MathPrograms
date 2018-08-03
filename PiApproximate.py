from random import *

NUM_OF_POINTS = 1000000

count = 0
for i in range(NUM_OF_POINTS):
	x = random()
	y = random()

	if x*x + y*y <= 1:
		count += 1

print '4 * {} / {} = {}'.format(count,NUM_OF_POINTS,4.0*count/NUM_OF_POINTS)