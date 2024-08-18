# Шаг 1: Определяем функцию `sum_a_b`, которая принимает два параметра: `a` и `b`.
# Эта функция складывает значения параметров `a` и `b` и возвращает результат.
def sum_a_b(a, b):
    return a + b  # Возвращаем сумму a и b

# Шаг 2: Используем функцию `input`, чтобы получить число от пользователя.
# Ввод пользователя всегда возвращается как строка, поэтому мы используем `int()` для преобразования введенной строки в целое число.
a = int(input("a: "))  # Запрашиваем у пользователя первое число и преобразуем его в целое число

# Шаг 3: Повторяем процесс для второго числа.
b = int(input("b: "))  # Запрашиваем у пользователя второе число и преобразуем его в целое число

# Шаг 4: Вызываем функцию `sum_a_b`, передавая в неё переменные `a` и `b`.
# Функция возвращает сумму этих двух чисел, и результат передается функции `print` для вывода на экран.
print(sum_a_b(a, b))  # Выводим результат суммы a и b