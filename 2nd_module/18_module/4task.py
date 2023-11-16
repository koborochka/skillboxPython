import re

def check_phone_numbers(numbers):
    for number in numbers:
        if re.match(r'^[89]\d{9}$', number):
            print(f'{number}: всё в порядке')
        else:
            print(f'{number}: не подходит')

# Пример списка номеров
phone_numbers = ['9999999999', '999999-999', '99999x9999']

# Проверка номеров
check_phone_numbers(phone_numbers)
