shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

totalPrice = 0
totalCount = 0

detailName = input("Название детали: ")
detailCount = int(input("Количество деталей: "))

for detail in shop:
    if detail[0] == detailName and totalCount < detailCount:
        totalCount += 1
        totalPrice += detail[1]

print(f"Общая стоимость: {totalPrice}")
