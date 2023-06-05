#  Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_indexes(arr, min_val, max_val):
    indexes = []
    for i in range(len(arr)):
        if arr[i] >= min_val and arr[i] <= max_val:
            indexes.append(i)
    return indexes

