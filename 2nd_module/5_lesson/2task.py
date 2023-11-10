inputString = input("Введите строку: ").replace(".", "").split()
maxLength = 0
for word in inputString:
    if len(word) > maxLength:
        maxLength = len(word)
        longestWord = word
print('Самое длинное слово: "{}"'.format(longestWord))
print("Длина этого слова: {}.".format(maxLength))
