a = [["d","a","c","b","d","a","b","b","a","d","d","a","d"],2]


def topK(combo, k):
	new_dict = {}
	for i in combo:
		if new_dict.get(i):
			new_dict[i] += 1
		else:
			new_dict[i] = 1

	alist = []
	benmark = None
	for key, v in new_dict.items():
		while k > 0:
			if v >= benmark:
				benmark = v
				print benmark
				alist.append(key)
				new_dict.pop(key)
			k -= 1
	return alist

print topK(a[0], a[1])
