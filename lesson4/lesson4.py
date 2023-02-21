# 1. Напишіть функцію, яка приймає номер місяця та повертає рядок з назвою пори року, до якої цей місяць відноситься.
def season(num_month):
    if 1 <= num_month <= 3:
        return "Winter"
    elif 4 <= num_month <= 6:
        return "Spring"
    elif 7 <= num_month <= 9:
        return "Summer"
    elif 10 <= num_month <= 12:
        return "Autumn"
    return "Error. No months from this number"


print(season(12))


# 2. Напишіть функцію, яка приймає довільну кількість словників, збирає їх в один словник та повертає його.
def dict_add(*arg):
    dict_temp = {}
    for i in arg:
        dict_temp = {**dict_temp, **i}
    return dict_temp


print(dict_add({"a":1, "b":2}, {"a":"aaa", "d":"bbbb"}))


# 3. Напишіть функцію, яка перевіряє, чи є слово паліндромом та повертає відповідно True чи False.
# Паліндром - це слово, яке однаково читається зліва направо та справа наліво. Наприклад, “випив”.
def if_palindrome(temp_str):
    if temp_str.lower() == temp_str[::-1].lower():
        return True
    return False


print(if_palindrome("випиВ"))


# 4. Напишіть функцію, яка приймає ціле число та повертає суму всіх його цифр. Наприклад, 437. 4+3+7=14.
def sum_in_number(num=int):
    temp = 0
    for i in str(num):
        temp += int(i)
    return temp


print(sum_in_number(89622))


# 5. Напишіть функцію, яка приймає рядок та повертає літеру, яка зустрічається в ньому найчастіше.
def rating_str(my_str=str):
    rating_coll = 0
    rating = ""
    for i in set(my_str.lower()):
        if my_str.lower().count(i) > rating_coll:
            rating = i
            rating_coll = my_str.lower().count(i)
    return rating


print(rating_str("aaaabbbbfdgdfgvcjtrgfhdgfafghcvnb"))