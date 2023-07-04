# напишите функцию, которая генерирует псевдоимена
#имя должно начинаться с заглавной буквы  и состоять из 4-7 букв, среди которых обязательно должны быть глассные
# полученные имена сохраните в фаил

import random

def get_psevdo_name() -> str:
    length_of_name = random.randint(3,7)
    counts = 'ауоеёийыюяцкнгшщзхфвпрлджэчсмтб' #всего  31 гласс - 10
    result_string = counts[random.randint(0,30)].title()
    for index in range(length_of_name):
        if index % 2 == 0:
            result_string = f'{result_string}{counts[random.randint(10,30)]}'
        else:
            result_string = f'{result_string}{counts[random.randint(0,9)]}'
    return result_string

def write_of_file_psevdo_names(list_of_name:list,file_name:str):
    with open(file_name,'w',encoding='utf-8') as file:
        for name in list_of_name:
            file.write(f'{name}\n')


num = int(input('Введите кол-во генерируемых имен: '))
list_of_name = []
for _ in range(num):
    list_of_name.append(get_psevdo_name())
write_of_file_psevdo_names(list_of_name,'psevdo_names.txt')

