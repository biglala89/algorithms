def hashmap(nums):
	freq = {}
	for num in nums:
		if num in freq:
			freq[num] += 1
		else:
			freq[num] = 1
	return freq

def top_k_maxheap(nums, k):
	arr = hashmap(nums)
	freq_heap = []
	for key in arr.keys():
		heapq.heappush(freq_heap, (-arr[key], key))
		# print freq_heap
	top_kk = []
	for i in range(k):
		top_kk.append(heapq.heappop(freq_heap)[1])
	return top_kk

def top_k_minheap(nums, k):
	arr = hashmap(nums)
	freq_heap = []
	for key in arr.keys():
		heapq.heappush(freq_heap, (arr[key], key))
		print 'after push: ', freq_heap
		if len(freq_heap) > k:
			heapq.heappop(freq_heap)
			print 'after pop: ', freq_heap
	top_kk = []
	for i in range(k):
		top_kk.append(heapq.heappop(freq_heap)[1])
	top_kk.reverse()
	return top_kk


import heapq
nums = ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'e', 'e', 'e', 'e', 'e']
print top_k_minheap(nums, 2)
