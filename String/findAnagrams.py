def findAnagrams(s, p):
	res = []
	if not s or not p:
		return res
	target = {}
	for char in p:
		target[char] = target.get(char, 0) + 1
	slow, fast = 0, 0
	counter = 0
	while fast < len(s):
		cur = s[fast]
		if cur in target:
			if target[cur] == 1:
				counter += 1
			target[cur] -= 1
		fast += 1
		if counter == len(target):
			res.append(slow)
		if fast - slow == len(p):
			cur = s[slow]
			if cur in target:
				if target[cur] == 0:
					counter -= 1
				target[cur] += 1
			slow += 1
	return res

p = 'aabc'
s = 'cabcayywwwwbcaa'
print findAnagrams(s, p)

# O(k) + O(n)
