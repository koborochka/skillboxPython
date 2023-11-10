def countUppercaseLowercase(text):
    uppercaseCount = len([char for char in text if char.isupper()])
    lowercaseCount = len([char for char in text if char.islower()])
    return uppercaseCount, lowercaseCount

userText = input("Введите строку для анализа: ")

uppercase, lowercase = countUppercaseLowercase(userText)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
