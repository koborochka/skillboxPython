array_1 = {1, 5, 10, 20, 40, 80, 100}
array_2 = {6, 7, 20, 80, 100}
array_3 = {3, 4, 15, 20, 30, 70, 80, 120}

# При помощи множеств
print(array_1 & array_2 & array_3)
print((array_1 - array_3) & (array_1 - array_2))

# Без помощи множеств
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

common_elements = []
for element in array_1:
    if element in array_2 and element in array_3:
        common_elements.append(element)
print(common_elements)

unique_elements = []
for element in array_1:
    if element not in array_2 and element not in array_3:
        unique_elements.append(element)
print(unique_elements)