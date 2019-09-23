def largest_range(array):

	hashset = set(array)

	max_len = 0
	while hashset:
		random = hashset.pop()
		print random
		print hashset
		
		lower = random - 1
		while lower in hashset:
			hashset.remove(lower)
			lower -= 1
		
		upper = random + 1
		while upper in hashset:
			hashset.remove(upper)
			upper += 1

		max_len = max(max_len, upper - lower - 1)

	return max_len

array = [3,-2,7,9,8,1,2,-1,5,8,-3,4,6]
print largest_range(array)
