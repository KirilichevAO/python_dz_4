# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

a = [1, 2, 3, 2, 5, 1]
found = set()
found_again = set()

for i in a:
    if i in found_again:
        continue
    if i in found:
        found.remove(i)
        found_again.add(i)
    else:
        found.add(i)

print(list(found))
