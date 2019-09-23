# one-liner
def sumofadded3(alist):
	return sum(list(map(lambda x: x+3, [elm for idx, elm in enumerate(alist) if idx % 2 == 0])))

import random
test = [random.randint(1,10) for _ in xrange(10)]
print 'ans:', sumofadded3(test)

# validation - normal approach
validate = []
for k, v in enumerate(test):
	if k % 2 == 0:
		print v, v+3
		validate.append(v+3)
print 'validated sum:', sum(validate)
