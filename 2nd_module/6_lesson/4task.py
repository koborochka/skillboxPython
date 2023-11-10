users_text = input("Введите текст: ")
pre_final = dict()
final = dict()

for char in users_text:
    if char in pre_final:
        pre_final[char] += 1
    else:
        pre_final[char] = 1

print("Оригинальный словарь частот: ")
for char in pre_final:
    print(char, ":", pre_final[char])

for char in pre_final.keys():
    if pre_final[char] in final:
        final[pre_final[char]].append(char)
    else:
        final[pre_final[char]] = [char]

print("Инвертированный словарь частот:")
for final_invert in final:
    print(final_invert, ":", final[final_invert])