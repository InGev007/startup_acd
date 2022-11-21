class MyTypeError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'MyTypeError, {0} '.format(self.message)
        else:
            return 'MyTypeError has been raised'

def month(number):
    dict_month = {1: 'Січень', 2: 'Лютий', 3: 'Березень',
                  4: 'Квітень', 5: 'Травень', 6: 'Червень',
                  7: 'Липень', 8: 'Серпень', 9: 'Вересень',
                  10: 'Жовтень', 11: 'Листопад', 12: 'Грудень'}
    try:
        return dict_month[number]
    except ValueError:
        print('Необхідно ввести номер місяця!')
        return month(int(input('Введіть коректне значення: ')))
    except KeyError:
        print('Такого місяця не існує!')
        return month(int(input('Введіть коректне значення: ')))

print(month(12))


def unique_list(t_list):
    try:
        if isinstance(t_list, list):
            if len(t_list) == len(set(t_list)):
                return True
            else:
                return False
        else:
            raise MyTypeError("Type must be list")
    except Exception as ex:
        print("Непредвиденная ошибка")

my_list = [1,2,3,20]
print(unique_list(my_list))





# Call of MyError
# raise MyError('We have a problem')