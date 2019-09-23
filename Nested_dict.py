def nest_dict(data):
	if type(data) is not dict:
		return [str(data)]
	else:
		res = []
		for key in data.keys():
			tmp = nest_dict(data[key])
			# print tmp
			for elm in tmp:
				res.append(str(key) + '->' + elm)
		return res


test = {
		'one': {'label': 'this is shot 001', 'start': 1, 'end': 10},
		'two': {'label': 'this is shot 002', 'start': 11, 'end': 25},
		'three': 'this is shot 3'
		}

print nest_dict(test)
