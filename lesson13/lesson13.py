from random_words import RandomWords
import random
import time

int_list = []
float_list = []
str_list = []
w = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(w.random_word())


def test_time(data, iteration: int):
    start_time = time.time()
    for i in range(0, iteration):
        bubble_sort(data)  # любой алгоритм
    return (time.time() - start_time) / iteration


def bubble_sort(data):
    length = len(data)
    for iIndex in range(length):
        swapped = False
        for jIndex in range(0, length - iIndex - 1):
            if data[jIndex] > data[jIndex + 1]:
                data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
                swapped = True
        if not swapped:
            break
    return data


print("Time sorting:" + str(test_time(str_list, 10)))
