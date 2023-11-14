def print_num(n):
	if n > 0:
		print_num(n-1)
		print(n)


num = int(input("Введите num: "))
print_num(num)