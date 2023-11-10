def tpl_sort(tpl_for_sort):
	lst = list(tpl_for_sort)
	c = 0
	k = 1
	sz = len(lst)
	while True:
		c = 0
		for i in range(sz - k):
			if lst[i] > lst[i + 1]:
				lst[i], lst[i + 1] = lst[i + 1], lst[i]
				c += 1
		if c == 0:
			return tuple(lst)
		k += 1


tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))