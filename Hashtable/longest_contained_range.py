def Largest_Contained_Range(arr):
	hashset = set(arr)
	range_ = 0
	while hashset:
		random = hashset.pop()
		print 'number popped: ', random
		
		upper = random + 1
		while upper in hashset:
			print 'current upper: ', upper
			hashset.remove(upper)
			print 'upper removed: ', upper
			upper += 1
		
		lower = random - 1
		while lower in hashset:
			print 'current lower: ', lower
			hashset.remove(lower)
			print 'lower removed: ', lower
			lower -= 1
		range_ = max(range_, upper - lower - 1)
	
	return range_

array = [3,-2,7,9,8,1,2,0,-1,5,8]
print Largest_Contained_Range(array)

