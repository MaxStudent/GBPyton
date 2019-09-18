
'''name = input('введите свое имя')
age = int(input('введите свой возраст'))
location = input('введите адрес проживания')

for name1, age1, location1 in zip (name, age, location):
    print (name1, age1, location1)'''

#Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

'''name = input('введите свое имя ')
age = input('введите свой возраст ')
city = input('введите город проживания ')

def user_info (name, age, city):
    result = '{}, {} год(а), проживанет в городе {}'.format(name, age, city)
    return result
print (user_info (name, age, city))'''

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

'''one = int(input('введите первое число '))
two = int(input('введите второе число '))
three = int(input('введите третье число '))
def my_filter (one, two, three):
    if one>two>three:
        print (one)
    elif one<two>three:
                print(two)
    elif one<two<three:
                print(three)
print (my_filter(one,two,three))'''


# решение 2
'''one = int(input('Введите значение первого числа: '))
two = int(input('Введите значение второго числа: '))
three = int(input('Введите значение третьего числа: '))

def max_number(one, two, three):
    num_list = [one, two, three]
    max_num= (max(num_list))
    return max_num

result = max_number(one, two, three)
print('Максимальное число из введеных вами: {}'.format(result))'''

# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.

'''names = [ "Николай", 'Евгений', 'Василий', 'Енот' ]
money= [ 100000, 80000, 10000, 250000 ]
names_money = dict(zip(names, money))
print(names_money)

# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000

file = open('salary.txt', 'w', encoding='UTF-8')
for line in names_money:
    file.write(str(line))
    file.write(' - ')
    file.write(str(names_money.get(line)))
    file.write('\n')
file.close()

file = open('salary.txt', 'r', encoding='UTF-8')
for i in file:
    names, money = i.strip().split(' - ')
    if int(money) < 500000:
        print('{} - {}'.format(names.upper(), int(money)*0.87))
file.close()
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),

# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.'''





