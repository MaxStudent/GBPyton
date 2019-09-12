#Задача 1
'''fruits = ['Яблоко ', 'Груша ', 'Маракуйа ', 'Банан ', 'Апельсин ', 'Мандарин ']
for index, value in enumerate(fruits, 1):
    print("{}. {}".format(index, value))'''
#Задача 2
'''mega_list = [7, 10, 4, 5, 6, 15]
super_mega_list = [10, 3, 5, 4, 6, 7, 9]
for item in super_mega_list:
    if item in mega_list:
        mega_list.remove(item)
print(mega_list)
print(super_mega_list)'''

#Задача 3

'''mega_list = [2, 7, 5, 6, 9, 15]
super_list = []
last_name = len(mega_list)
for i in range(last_name):
    if mega_list[i] % 2 == 0:
        super_list.append(mega_list[i] / 4)
else:
    super_list.append(mega_list[i] * 2)

print(super_list)'''

#Normal
#Задача 1


'''numb = [7, -10, 6, 4, -30, 30, 25]
result = [int(i) for i in range(max(numb)) if int(i) ** 2 in numb]
print(result)'''

#задачу 2 не сделал( получаются какие то длинные оч решения, в задаче 3 почему то не раотает функция, которую просили использовать

# Задача-4:

# Решение a
'''mega_list = [1, 2, 4, 5, 6, 2, 5, 2]
super_list = set(mega_list)
print(super_list)
# Решение б
super_mega__list = []
for item in mega_list:
    if mega_list.count(item) == 1:
        super_mega_list.appens(item)

print(super_mega_list)'''

