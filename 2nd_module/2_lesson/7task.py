string = input("Введите слово: ")

if string == string[::-1]:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")