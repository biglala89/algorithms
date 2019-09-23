def map_brackets(seq):
	stack =[]
	for s in seq:
		if not stack:
			stack.append(s)
		