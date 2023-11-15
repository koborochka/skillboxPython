def validate_registration(registration):
    fields = registration.split()
    if len(fields) != 3:
        raise IndexError('НЕ присутствуют все три поля')

    name = fields[0]
    email = fields[1]
    age = fields[2]

    if not name.isalpha():
        raise NameError('Поле «Имя» содержит НЕ только буквы')

    if '@' not in email or '.' not in email:
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и точку')

    try:
        age = int(age)
        if age < 10 or age > 99:
            raise ValueError('Поле «Возраст» НЕ представляет число от 10 до 99')
    except ValueError:
        raise ValueError('Поле «Возраст» НЕ представляет число от 10 до 99')


with open('registrations.txt', 'r', encoding="utf-8") as file:
    good_log = open('registrations_good.log', 'a', encoding="utf-8")
    bad_log = open('registrations_bad.log', 'a', encoding="utf-8")

    for line in file:
        try:
            validate_registration(line)
            good_log.write(line)
        except (IndexError, NameError, SyntaxError, ValueError) as e:
            bad_log.write(f'{line.rstrip()}        {e}\n')

    good_log.close()
    bad_log.close()