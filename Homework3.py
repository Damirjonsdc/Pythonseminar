# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
ticket_number = input("Введите номер билета: ")

# Проверяем, что номер содержит 6 цифр
if len(ticket_number) != 6:
    print("Некорректный номер билета")
else:
    # Преобразуем номер билета в список цифр
    digits = [int(d) for d in ticket_number]

    # Считаем сумму первых трех цифр и последних трех цифр
    first_sum = sum(digits[:3])
    last_sum = sum(digits[3:])

    # Проверяем, является ли билет счастливым
    if first_sum == last_sum:
        print("Билет счастливый!")
    else:
        print("Билет не является счастливым")