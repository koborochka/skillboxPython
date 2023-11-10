def printGuests(guestList):
    print(f"Сейчас на вечеринке {len(guestList)} человек: {guestList}")

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

printGuests(guests)

while True:
    action = input("Гость пришёл или ушёл? ").lower()

    if action == 'пора спать':
        print("Вечеринка закончилась, все легли спать.")
        break

    if action == 'пришёл':
        if len(guests) < 6:
            newGuest = input("Имя гостя: ")
            guests.append(newGuest)
            print(f"Привет, {newGuest}!")
        else:
            print("Прости, но мест нет.")
    elif action == 'ушёл':
        if guests:
            departedGuest = input("Имя гостя: ")
            if departedGuest in guests:
                guests.remove(departedGuest)
                print(f"Пока, {departedGuest}!")
            else:
                print(f"{departedGuest} не было в списке гостей.")
        else:
            print("Некого провожать, вечеринка пуста.")
    else:
        print("Некорректное действие. Пожалуйста, введите 'пришёл', 'ушёл' или 'пора спать'.")

    printGuests(guests)
