number = input("Введите трехзначное число: ")
sum = 0
for digit in number:
    sum += int(digit)
print("Сумма цифр введенного числа равна:", sum)

# В коде я  прошу пользователя ввести трехзначное число с помощью функции `input()`. 
# Затем мы создаем переменную `sum` и устанавливаем ее значение равным 0.
# Далее мы использовали цикл `for` для прохода через каждую цифру введенного числа, преобразовывая каждую цифру в целое число с помощью функции `int()` и добавляя его к переменной `sum`. 
# Наконец, мы выводим результат с помощью функции `print()`.