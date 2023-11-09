containersCount = int(input("Количество контейнеров: "))

containers = []
count = 0
while count < containersCount:
    containerWeight = int(input("Введите вес контейнера: "))
    if 0 <= containerWeight <= 200:
        containers.append(containerWeight)
        count += 1

containers.sort(reverse=True)
newContainer = int(input("Введите вес нового контейнера: "))

for number in range(len(containers)):
    if containers[number] < newContainer:
        print(f"Номер, который получит новый контейнер: {number + 1}")
        break
else:
    print(f"Номер, который получит новый контейнер: {containersCount + 1}")
