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
				new_lists.append(alist[:])
				print 'this round: ', new_lists
				print 
				l += 1
				r -= 1
			j = i + 1
	return new_lists

test = arrayOfArrays[0]
lst = mergeK(test)
print 'input list: ', lst
print 
ans = swap_duplicates(lst)
print 'final results:\n', ans
