import heapq
def k_smallest(array, k):
	if not array:
		return []
	heapq.heapify(array)
	res = [heapq.heappop(array) for _ in range(k)]
	return res

array = [1,2,3,4,5,5,5,6,3,7,2,4,9,10,8,20]
print k_smallest(array, 5)
