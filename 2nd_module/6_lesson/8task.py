string = input("Введите строку: ")
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

odd_count = 0
for count in char_count.values():
    if count % 2 != 0:
        odd_count += 1
    if odd_count > 1:
        print("Нельзя сделать палиндромом.")
        break
else:
    print("Можно сделать палиндромом.")