# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]

nums = [1, 1, 2, 0, -1, 3, 4, 4]
unique_nums = set(nums)
count = len(unique_nums)
print(count)