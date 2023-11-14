def sum(*nums):
	res = 0
	for num in nums:
		try:
			res += sum(*num)
		except TypeError:
			res += num
	return res


print(sum([[1, 2, [3]], [1], 3]))
print(sum(1, 2, 3, 4, 5))