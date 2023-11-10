import random

original_list = [random.randint(1, 10) for _ in range(10)]
print(original_list)

new_list = []
for x in range(0, 10, 2):
	new_list.append(tuple([original_list[x], original_list[x+1]]))

print(new_list)


new_list = [tuple([original_list[x], original_list[x+1]]) for x in range(0, 10, 2)]
print(new_list)