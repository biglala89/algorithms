import heapq

def mergeK(arrays):
	if not arrays:
		return None
	container = []
	for i in range(len(arrays)):
		if len(arrays[i]):
			container.append((arrays[i][0], i, 0))
	heapq.heapify(container)
	# print container
	res = []
	while container:
		num = heapq.heappop(container)
		arr_idx = num[1] # which array the popped item is from
		k = num[2] # element index, starting from 1
		res.append((num[0], num[1]))
		if k < len(arrays[arr_idx]) - 1:
			heapq.heappush(container, (arrays[arr_idx][k + 1], arr_idx, k + 1))
			# print container
	return res

arrayOfArrays = [
					[[4,10,11], [1,3,7,11], [6,9,16], [4,10]],
					# [[3],[1,2,3,4,5]],
					# [[0], [0], [1], [1]],
					# [[],[0]]
				]

if __name__ == '__main__':
	for arrays in arrayOfArrays:
		print mergeK(arrays)
		print
