# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


'''b = [i ** 2 for i in [1, 2, 4, 0]]
print('Новый список: {}'.format(b))

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruts_1 = ['apple', 'pineapple']
fruts_2 = ['pen', 'pineapple']

# fruts_3=[]
# for i in fruts_1:
#     for j in fruts_2:
#         if i == j:
#             fruts_3.append(i)
# print(fruts_3)

fruts_3 = [i for i in fruts_1 if i in fruts_2]
print('Список фруктов в обоих списках: {}'.format(fruts_3)'''


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
'''import random

my_list = [random.randint(-100, 100) for _ in range(10)]
print('Исходный список: {}'.format(my_list))
my_list1 = [element for element in my_list if element % 3 == 0]  # Список из кратных 3-м
my_list2 = [element for element in my_list if element > 0]  # Список из положительных элементов
my_list3 = [element for element in my_list if element % 4 != 0]  # список из некртанх 4-м
print('кратные 3-м: {}'.format(my_list1))
print('положительные: {}'.format(my_list_2))
print('кратные 4-м: {}'.format(my_list3))'''

