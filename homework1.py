number = input("Введите трехзначное число: ")
sum = 0
for digit in number:
    sum += int(digit)
print("Сумма цифр введенного числа равна:", sum)