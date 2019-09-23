def sift_down(array, index):
	left = index * 2 + 1
	right = index * 2 + 2
	small = index
	if left < len(array) and array[small] > array[left]:
		small = left
	if right < len(array) and array[small] > array[right]:
		small = right
	if small != index:
		array[small], array[index] = array[index], array[small]
		print array
		sift_down(array, small)
	return array


# arrOfArrays = [[0,1,5,6,8,4], [2,2,3,3,3,4,1], [10,3,4,2,6,13,0], [0]]
# for i in range(len(arrOfArrays)):
# 	res = sift_down(arrOfArrays[i], 0)
# 	print 'final result: ', res
# 	print

array = [5,4,3,2,1]

def build_heap(arr):
	for i in range(len(arr)/2-1, -1, -1):
		sift_down(arr, i)

build_heap(array)
