count = int(input("Введите количество элементов"))
list = []
i = 0
el = 0
while i < count:
    list.append(input("Введите следующее значение"))
    i += 1

for elem in range(int(len(list)/2)):
        list[el], list[el + 1] = list [el + 1], list[el]
        el += 2
print(list)