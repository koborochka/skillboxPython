def lastPersonStanding(N, K):
    people = list(range(1, N + 1))
    index = 0

    while len(people) > 1:
        index = (index + K - 1) % len(people)
        removed_person = people.pop(index)
        print(f"Выбывает человек под номером {removed_person}")
        print(f"Текущий круг людей: {people}")

    return people[0]


N = int(input("Количество человек: "))
K = int(input("Какое число в считалке? "))

lastPerson = lastPersonStanding(N, K)
print(f"\nОстался человек под номером {lastPerson}")
