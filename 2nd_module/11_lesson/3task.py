class Parent:
    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def info(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет. У меня {len(self.children)} детей.")

    def add_child(self, child):
        self.children.append(child)
        print(f"{self.name} добавил ребёнка {child.name}.")

    def calm_child(self, child):
        if child in self.children:
            child.state_of_calm = True
            print(f"{self.name} успокаивает ребёнка {child.name}.")
        else:
            print(f"{self.name} не может успокоить ребёнка {child.name}, так как он не его ребёнок.")

    def feed_child(self, child):
        if child in self.children:
            child.state_of_hunger = False
            print(f"{self.name} кормит ребёнка {child.name}.")
        else:
            print(f"{self.name} не может покормить ребёнка {child.name}, так как он не его ребёнок.")


class Child:
    def __init__(self, name, age, state_of_calm, state_of_hunger):
        self.name = name
        self.age = age
        self.state_of_calm = state_of_calm
        self.state_of_hunger = state_of_hunger


parent1 = Parent("Ваня", 36, [])
child1 = Child("Карина", 9, True, True)
parent1.info()

parent1.add_child(child1)

parent1.info()
parent1.calm_child(child1)
parent1.feed_child(child1)