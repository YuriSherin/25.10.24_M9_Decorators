def is_prime(func):
    """Функция декоратор в качестве аргумента принимает ссылку на функцию"""
    def wrapper(*args):
        """Функция обертка, позволяющая выполнить некие команды до вызова функции func
        и некие команды после вызова функции func"""

        """До вызова функции func проверим, что все аргументы имеют тип int"""
        for i in args:
            if not isinstance(i, int):
                raise ValueError('Аргументами функции могут быть только целые числа')

        num = func(*args)       # выполним функцию

        """После вызова функции func определим, является ли результат выполнения функции
        числом простым или составным"""
        simple = 'Простое'
        for x in range(2, num):
            if not num % x:
                simple = 'Составное'
                break

        return f'{simple}\n{num}'   # возвращаем результат выполнения функции декоратор
    return wrapper

@is_prime
def sum_three(*args):
    """Функция возвращает сумму переданных ей аргументов"""
    return sum(args)

# Пример:
try:
    result = sum_three(2, 3, 6)
except ValueError as e:
    print(e)
else:
    print(result)
