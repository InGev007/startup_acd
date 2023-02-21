def decrement_print(number: int):
    number -= 1
    print(number)
    if number == 0:
        return
    else:
        decrement_print(number)


if __name__ == "__main__":
    decrement_print(int(input("Введите число для декриментации: ")))