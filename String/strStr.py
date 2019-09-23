
def strStr(haystack, needle):
	if not needle:
		return -1
	for h in xrange(len(haystack) - len(needle) + 1):
		for n in xrange(len(needle)):
			if haystack[h+n] != needle[n]:
				break
		else:
			return h
	return -1


haystack = 'hello'
needle = 'll'
print haystack
print needle
print strStr(haystack, needle)
