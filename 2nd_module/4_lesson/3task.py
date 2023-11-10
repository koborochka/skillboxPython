import random

first_athletes = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_athletes = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [max(first_athletes[index], second_athletes[index]) for index in range(20)]

print(f"Первая команда: {first_athletes}")
print(f"Вторая команда: {second_athletes}")
print(f"Победители тура: {winners}")