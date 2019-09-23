def sift_up(array, index):
	parent = (index - 1) / 2
	child = index
	if array[index] > array[parent]:
		return array
	elif array[index] <= array[parent] and index > 0:
		array[index], array[parent] = array[parent], array[index]
		print 'mid steps: ', array
		index = parent
		sift_up(array, index)
	return array


arrOfArrays = [[0,1,5,6,8,4], [2,2,3,3,3,4,1], [10,3,4,2,6,13,0], [10,3,4,2,6,13,0,45], [0]]
for i in range(len(arrOfArrays)):
	res = sift_up(arrOfArrays[i], len(arrOfArrays[i])-1)
	print 'final result: ', res
	print
