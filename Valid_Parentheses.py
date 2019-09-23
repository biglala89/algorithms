def isvalid(input):
	# print len(input)
	if len(input) % 2 != 0 or len(input) < 1:
		# print 'inside first loop'
		return False
	else:
		# print 'inside else condition'
		mathches = {'(':')', '[':']', '{':'}'}
		stack = []
		for ch in input:
			# print ch
			if ch in mathches:
				stack.append(mathches[ch])
				# print 'current stack holds: ', stack
			elif ch in [')', ']', '}']:
				if len(stack) > 0 and ch == stack[-1]:
					stack.pop()
					continue
				else:
					return False
			else:
				return False
		# if stack:
		# 	return False #in case contains only left brackets
		return not stack


test_cases = [
['(', '[', '{', '}', ']', ')'], 
['(', ')', '(', ')', '(', ')'], 
[], 
['[]])'], 
['[{']
]

for t in test_cases:
	print isvalid(t)
	print 
