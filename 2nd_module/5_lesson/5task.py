while True:
    password = input("Придумайте пароль: ")
    length = len(password)
    capitalizedLetter = any(char.isupper() for char in password)
    digitCount = sum(char.isdigit() for char in password)

    if length >= 8 and capitalizedLetter and digitCount >= 3:
        print("Это надёжный пароль.")
        break
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")
