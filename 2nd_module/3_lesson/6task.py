count = 0

n = int(input("Количество роликов: "))
rollerSizes = []
for i in range(n):
    size = int(input("Размер пары {}: ".format(i + 1)))
    rollerSizes.append(size)

k = int(input("Количество людей: "))
footSizes = []
for i in range(k):
    size = int(input("Размер ноги человека {}: ".format(i + 1)))
    footSizes.append(size)

for i in footSizes:
    if i in rollerSizes:
        count += 1
        rollerSizes.remove(i)

print("Наибольшее количество людей, которые могут взять ролики:", count)
