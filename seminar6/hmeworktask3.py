#  Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# получаем данные от пользователя
lst = list(map(int, input("Введите список чисел через пробел: ").split()))
mn = int(input("Введите минимум: "))
mx = int(input("Введите максимум: "))

# ищем индексы элементов, значение которых входит в заданный диапазон
indices = [i for i in range(len(lst)) if mn <= lst[i] <= mx]

# выводим результат
print(f"Индексы элементов, значение которых входит в диапазон от {mn} до {mx}: {indices}")

