orders_count = int(input("Введите количество заказов: "))
orders = dict()

for order_number in range(1, orders_count+1):
    order = input("{}-й заказ: ".format(order_number)).split()
    if order[0] in orders:
        if order[1] in orders[order[0]]:
            orders[order[0]][order[1]] += order[2]
        else:
            orders[order[0]][order[1]] = order[2]
    else:
        orders[order[0]] = {order[1]: order[2]}

print("Итоговый заказ:")

for name in orders.keys():
    print(name, ":")
    for order in orders[name]:
        print(order, ":", orders[name][order])
    print("")