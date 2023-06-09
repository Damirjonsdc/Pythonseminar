# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

# Вводим элементы первого множества
set1 = set()
for i in range(n):
    x = int(input("Введите элемент {}-го множества: ".format(i+1)))
    set1.add(x)

# Вводим элементы второго множества
set2 = set()
for i in range(m):
    x = int(input("Введите элемент {}-го множества: ".format(i+1)))
    set2.add(x)

# Находим пересечение множеств
intersection = set1.intersection(set2)
sorted_intersection = sorted(intersection)

# Выводим результат
print("Числа, которые встречаются в обоих множествах: ", sorted_intersection)