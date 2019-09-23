# def nearest_repeat(arr):
# 	freq = {}
# 	# dist = float('inf')
# 	for idx, item in enumerate(arr):
# 		if item in freq:
# 			dist = idx - freq[item][0]
# 			if dist < freq[item][1]:
# 				freq[item] = (idx, dist)
# 		else:
# 			freq[item] = (idx, float('inf'))
# 	return freq

def nearest_repeat_BetterSolution(arr):
	freq = {}
	dist = float('inf')
	for idx, item in enumerate(arr):
		if item in freq:
			dist = min(idx - freq[item], dist)
		freq[item] = idx
	return dist

string = 'all work and no play makes for no work no fun and no results'
array = [i for i in string.split()]
print array
print nearest_repeat_BetterSolution(array)
