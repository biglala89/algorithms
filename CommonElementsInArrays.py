def common_element(arr1, arr2, arr3):
	x = y = z = 0
	res = []
	while x < len(arr1) and y < len(arr2) and z < len(arr3):
		first_num = arr1[x]
		second_num = arr2[y]
		third_num = arr3[z]
		if first_num == second_num == third_num:
			res.append(arr1[x])
			x += 1
			y += 1
			z += 1
		else:
			if min(first_num, second_num, third_num) == first_num:
				x += 1
				print 'x: ', x
			elif min(first_num, second_num, third_num) == second_num:
				y += 1
				print 'y: ', y
			elif min(first_num, second_num, third_num) == third_num:
				z += 1
				print 'z: ', z
	return res

arr1 = [2,6,9,11,13,13,17]
arr2 = [3,6,7,10,13,13,18]
arr3 = [4,5,6,9,11,13,13]

print set(arr1) & set(arr2) & set (arr3)
print common_element(arr1, arr2, arr3)
