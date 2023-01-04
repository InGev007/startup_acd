import random


class Tree:

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.id_node)

    # Insert method to create nodes
    def insert(self, id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node

    def list_insert(self, lst):
        for n in lst:
            self.insert(n)

    # findval method to compare the id_node with nodes
    def find_value(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return print(str(find_val) + " Not Found")
            return self.left.find_value(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return print(str(find_val) + " Not Found")

            return self.right.find_value(find_val)
        else:
            print(str(self.id_node) + ' is found')

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node),
        if self.right:
            self.right.print_tree()

    def min_value(self):
        # Найдем крайний левый лист
        while self.left is not None:
            self = self.left
        print(str(self))

    def max_value(self):
        # Найдем крайний правый лист
        while self.right is not None:
            self = self.right
        print(str(self))

    # Удаление узла
    def delete_node(self, id_node):

        if self.id_node is None:
            return None

        if id_node < self.id_node:
            self.left = self.left.delete_node(id_node)
            return self

        elif id_node > self.id_node:
            self.right = self.right.delete_node(id_node)
            return self

        if self.left is None:
            return self.right

        elif self.right is None:
            return self.left

        else:
            min_key = self.right.min_value()
            self.id_node = min_key
            self.right = self.right.delete_node(min_key)
            return self


print("Наполняем рандомно древо и выводим")
trees = Tree(random.randint(1,50))
trees.insert(random.randint(1,50))
trees.insert(random.randint(1,50))
trees.insert(random.randint(1,50))
trees.insert(random.randint(1,50))
trees.insert(random.randint(1,50))
trees.insert(random.randint(1,50))
trees.insert(random.randint(1,50))
trees.insert(random.randint(1,50))
trees.insert(random.randint(1,50))
trees.insert(random.randint(1,50))
trees.insert(random.randint(1,50))
trees.print_tree()
print("___________")
print("Добавляем список и выводим древо")
trees.list_insert([8,10,12])
trees.print_tree()
print("___________")
print("Поиск элементов в древе")
trees.find_value(0)
trees.find_value(8)
print("___________")
print("Поиск минимального значения в древе")
trees.min_value()
print("___________")
print("Поиск максимального значения в древе")
trees.max_value()
print("___________")
print("Удаление элемента в древе и вывод древа для проверки")
trees.delete_node(8)
trees.print_tree()


