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

    # findval method to compare the id_node with nodes
    def findval(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return str(find_val) + " Not Found"
            return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return str(find_val) + " Not Found"
            return self.right.findval(find_val)
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
        # Найдем крайний левый лист
        while self.right is not None:
            self = self.right
        print(str(self))

    # Удаление узла
    def delete_node(self, id):
        # Возвращаем, если дерево пустое
        if self is None:
            return self
        # Найдем узел, который нужно удалить
        if id < self.id_node:
            self.left = self.delete_node(id)
        elif id > self.id_node:
            self.right = self.delete_node(id)
        else:
            # Если у узла только один дочерний узел или вообще их нет        
            if self.left is None:
                temp = self.right
                self = None
                return temp

            elif self.right is None:
                temp = self.left
                self = None
                return temp

            # Если у узла два дочерних узла,
            # помещаем центрированного преемника
            # на место узла, который нужно удалить
            temp = self.min_value(self.right)

            self.id_node = temp.id_node

            # Удаляем inorder-преемниа
            self.right = self.delete_node(self.right, temp.id_node)
        return self



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
trees.insert(8)
trees.print_tree()

trees.min_value()
trees.max_value()
print(str(trees[]))
