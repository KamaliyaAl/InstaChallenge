# Шаг 1: Используем функцию `input`, чтобы получить ввод от пользователя и сохраняем его в переменную `wether`.
# Пользователь должен ввести текст, который описывает погоду (например, "sunny", "rainy" и т. д.).
wether = input()

# Шаг 2: Проверяем, соответствует ли введённое значение переменной `wether` строке "sunny".
# Если `wether` равно "sunny", выполняется код в блоке `if`, который выводит сообщение "Go for a walk!".
if wether == "sunny":
    print("Go for a walk!")  # Если погода солнечная, предлагаем пойти на прогулку

# Шаг 3: Если первое условие не выполнено, проверяется второе условие `elif`,
# чтобы узнать, равно ли значение переменной `wether` строке "rainy".
# Если `wether` равно "rainy", выполняется код в блоке `elif`, который выводит сообщение "Stay home!".
elif wether == "rainy":
    print("Stay home!")  # Если погода дождливая, предлагаем остаться дома

# Шаг 4: Если ни одно из предыдущих условий не выполнено, выполняется код в блоке `else`.
# Этот блок выполняется, если `wether` имеет значение, отличное от "sunny" или "rainy".
# В данном случае выводится сообщение "Go to a cafe!".
else:
    print("Go to a cafe!")  # Для всех других случаев предлагаем сходить в кафе
