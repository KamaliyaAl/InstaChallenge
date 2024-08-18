# Шаг 1: Используем функцию `input`, чтобы получить строку от пользователя и сохраняем её в переменную `name`.
# `input()` считывает введённый пользователем текст и возвращает его в виде строки.
name = input()  # считываем строку

# Шаг 2: Используем функцию `input`, чтобы получить текст от пользователя, но так как это должно быть число, мы оборачиваем вызов `input()` в `int()`.
# `int()` преобразует введённую строку в целое число. Если пользователь введёт не число, программа выдаст ошибку.
age = int(input())  # считываем число

# Шаг 3: Используем функцию `input` снова, чтобы получить ещё одну строку от пользователя и сохраняем её в переменную `friend`.
friend = input()  # считываем строку

# Шаг 4: Используем функцию `print`, чтобы вывести приветственное сообщение с использованием переменной `name`.
# Для объединения строк в одно сообщение мы используем оператор `+`, который объединяет (конкатенирует) строки.
print("Hi, my name is " + name)

# Шаг 5: Выводим сообщение о возрасте с использованием переменной `age`.
# Так как `age` — это целое число, его нужно преобразовать в строку с помощью `str()` для корректного объединения с другими строками.
print("I am " + str(age) + " years old")

# Шаг 6: Выводим сообщение о друге с использованием переменной `friend`.
# Строка, введенная пользователем для переменной `friend`, будет объединена с остальной частью строки для вывода.
print("My friend is " + friend)