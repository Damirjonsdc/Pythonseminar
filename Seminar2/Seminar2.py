# По данному целому неотрицательному n вычислите 
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех 
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл 
# while
# Input: 5
# Output: 120

n = int(input("Введите число, для которого нужно вычислить факториал: "))
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("Факториал числа", n, "равен", fact)