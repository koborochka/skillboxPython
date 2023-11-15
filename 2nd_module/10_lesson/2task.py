import random

sum_of_numbers = 0
with open('out_file.txt', 'w') as file:
    file.write("")

try:
    with open('out_file.txt', 'a') as file:
        while sum_of_numbers < 777:
            user_input = int(input('Введите число: '))

            if random.randint(1, 13) == 1:
                raise Exception('Вас постигла неудача!')

            file.write(str(user_input) + '\n')
            sum_of_numbers += user_input

        print('Вы успешно выполнили условие для выхода из порочного цикла!')

except Exception as e:
    raise

finally:
    with open('out_file.txt', 'r') as file:
        print('\nСодержимое файла out_file.txt:')
        print(file.read())