import random


class Unit:
    hp = 100
    name = "Воин"

    def info(self):
        print("Оставшееся здоровье: {}".format(self.hp))

    def take_damage(self):
        self.hp -= 20
        self.info()


first_unit = Unit()
second_unit = Unit()
while first_unit.hp != 0 and second_unit.hp != 0:
    who_take_damage = random.randint(1, 2)
    if who_take_damage == 1:
        print("Атаковал unit1:")
        second_unit.take_damage()
    else:
        print("Атаковал unit2:")
        first_unit.take_damage()
if first_unit.hp > second_unit.hp:
    print("Победу одержал unit1")
else:
    print("Победу одержал unit2")