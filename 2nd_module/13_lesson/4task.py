class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def get(self, index):
        current_node = self.head
        for _ in range(index):
            if current_node is None:
                raise IndexError("Index out of range")
            current_node = current_node.next_node
        return current_node.data

    def remove(self, index):
        if index == 0:
            self.head = self.head.next_node
        else:
            current_node = self.head
            for _ in range(index - 1):
                if current_node is None or current_node.next_node is None:
                    raise IndexError("Index out of range")
                current_node = current_node.next_node
            current_node.next_node = current_node.next_node.next_node

    def __str__(self):
        result = []
        current_node = self.head
        while current_node:
            result.append(str(current_node.data))
            current_node = current_node.next_node
        return "[" + " ".join(result) + "]"


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)

print("Текущий список:", my_list)
print("Получение третьего элемента:", my_list.get(2))

print("Удаление второго элемента.")
my_list.remove(1)
print("Новый список:", my_list)