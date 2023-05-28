# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input())
a = list(map(int, input().split()))
x = int(input())

closest = a[0]  # принимаем первый элемент как ближайший

for elem in a:
    if abs(elem - x) < abs(closest - x):
        closest = elem  # если нашли более близкий элемент, то сохраняем его

print(closest)