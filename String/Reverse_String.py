def reverse_helper(lst, left, right):
	while left < right:
		lst[left], lst[right] = lst[right], lst[left]
		left += 1
		right -= 1
		print left, right

def reverse_string(string):
	lst = list(string)
	print lst
	reverse_helper(lst, 0, len(lst) - 1)
	print lst
	print 
	i = 0
	left, right = i, i
	while i < len(lst):
		if i == len(lst) - 1 or lst[i+1] == ' ':
			right = i
			print lst[left:right+1]
			reverse_helper(lst, left, right)
			left = i + 2
		i += 1
	return ''.join(lst)


test_str = 'I love    starbucks'  
print reverse_string(test_str)
