class Solution(object):
	def reverseWords(self, string):
		# Pad the string with spaces to account for index out of range error.
		# Some strings do not have leading or trailing spaces, so when look 
		# for word bounds, errors could occur
		lst = list(' ' + string[0] + ' ')
		self.reverse_helper(lst, 0, len(lst) - 1)
		print lst
		i = 0
		j = 0
		left = i
		right = j
		new_str = ''
		while j < len(lst):
			# j as right word boundary locator, i as left boundary locator
			# When j is non-space and j+1 is space, that's a right boundary
			if lst[j] != ' ' and lst[j + 1] == ' ':
				while i <= j:
					# Same logic here. If i is space and i+1 is non-space, that's a left boundary
					if lst[i - 1] == ' ' and lst[i] != ' ':
						left = i
						right = j
						self.reverse_helper(lst, left, right)
						# add a space after each word
						new_str += ''.join(lst[left:right + 1]) + ' '
					i += 1
			j += 1
		# strip the trailing space as a result of last concatenation
		return new_str.strip()

	def reverse_helper(self, lst, left, right):
		while left < right:
			lst[left], lst[right] = lst[right], lst[left]
			left += 1
			right -= 1

# test = ['']
test = [' I love dog ']
s = Solution()
print s.reverseWords(test)
