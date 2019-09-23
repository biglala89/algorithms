def permute(nums):
	perms, res = [], []
	def impl(i):
		if i == len(nums):
			res.append(perms[:])
			return 
		for n in nums:
			if n not in perms:
				perms.append(n)
				impl(i+1)
				perms.pop()
	impl(0)
	return res

test = [1,2,3]
result = permute(test)
print result
