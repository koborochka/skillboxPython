def myzip(a, b):
	return ((a[i], b[i]) for i in range(min(len(a), len(b))))


string = "abcd"
tuple_numbers = (10, 20, 30, 40)
new_zip = myzip(string, tuple_numbers)

print(new_zip)
print(*new_zip, sep='\n')