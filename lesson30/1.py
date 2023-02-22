class HashTable:
    # Конструктор, який приймає розмір хеш-таблиці та ініціалізує порожню таблицю.
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Функція, яка повертає рядок, що представляє хеш-таблицю у вигляді списку.
    def __str__(self):
        return str(self.table)

    # Приватна функція, яка приймає ключ та повертає індекс у таблиці для зберігання елемента.
    def _hash_function(self, key):
        return key % self.size

    # Функція для додавання нового елемента до хеш-таблиці за допомогою ключа та значення.
    def insert(self, key, value):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    # Функція для пошуку значення за ключем.
    def search(self, key):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        raise KeyError("Key not found")

    # Функція для видалення елемента за ключем.
    def delete(self, key):
        index = self._hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return
        raise KeyError("Key not found")

    # Функція для виправлення коллізій
    def fix_collisions(self):
        new_table = [[] for _ in range(self.size)]
        for index in range(self.size):
            for item in self.table[index]:
                new_index = self._hash_function(item[0])
                new_table[new_index].append(item)
        self.table = new_table
