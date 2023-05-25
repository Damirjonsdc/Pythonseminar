n = int(input("Введите количество арбузов: "))
masses = [int(input()) for _ in range(n)]
# или можно ввести все массы на одной строке и разделить их с помощью метода split:
# masses = list(map(int, input("Введите массы арбузов: ").split()))

min_mass = min(masses)
max_mass = max(masses)

print("Самый легкий арбуз весит {} кг".format(min_mass))
print("Самый тяжелый арбуз весит {} кг".format(max_mass))