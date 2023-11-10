firstString = input("Введите первую строку: ")
secondString = input("Введите вторую строку: ")

if len(firstString) != len(secondString):
    print("Строки разной длины, невозможно получить первую строку из второй с помощью циклического сдвига.")
else:
    for i in range(len(firstString)):
        if firstString == secondString:
            print("Первая строка получается из второй со сдвигом", i)
            break
        secondString = secondString[1:] + secondString[0]
    else:
        print("Первую строку нельзя получить из второй с помощью циклического сдвига.")