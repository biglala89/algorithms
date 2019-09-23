from Merge_K_Sorted_Arrays import *

def swap_duplicates(alist):
	new_lists = [alist]
	i = j = l = r = 0
	while j < len(alist) - 1:
		if alist[j][0] != alist[j+1][0]:
			j += 1
		else:
			l = j
			i = j + 1
			# alist.append('pad')
			while alist[i+1][0] == alist[i][0] and i < len(alist) - 1:
				i += 1
			r = i
			while l <= r:
				alist[l], alist[r] = alist[r], alist[l]
				# alist.pop()
				new_lists.append(alist)
				print 'this round: ', new_lists
				print 
				l += 1
				r -= 1
			j = i + 1
	return new_lists

def output_format(lst):
	values = map(lambda x: x[0], lst)
	arr_idx = map(lambda x: x[1], lst)
	return values, arr_idx

def candidate_scan(array):
	candidates = []
	flatten_arr = mergeK(array)
	lists = swap_duplicates(flatten_arr)
	for lst in lists:
		k = 0
		values, arr_idx = output_format(lst)
		while k + 4 - 1 < len(arr_idx):
			window = arr_idx[k:k + 4]
			if set(window) == set([0,1,2,3]):
				candidates.append(values[k:k + 4])
			k += 1
	return candidates

test = arrayOfArrays[0]
print candidate_scan(test)
