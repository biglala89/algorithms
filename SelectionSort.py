def selection_sort(array):
	for j in range(len(array)):
		bigindex = 0
		for i in range(len(array) - j):
			if array[i] >= array[bigindex]:
				bigindex = i
		array[bigindex], array[i] = array[i], array[bigindex]
	return array

alist = [10, 8, 3, 6, 2, 0, 5, 4, 9, 7]
print selection_sort(alist)
