#Напишите функцию, которая заполняет фаил случайными парами чисел
# первое - int, второе - float разделены вертикальной чертой
#минимальное число -1000 , максимальное +1000
# колличество строк и имя файла передаются как параметры функции
import random

def file_writer_of_int_and_float_random_number(lines:int , file_name:str):
    with open(file_name, 'a', encoding='utf-8') as file:
        for _ in range(lines):
            file.write(f'{random.randint(-1000,1001)}|{random.uniform(-1000,1001)}\n')

file_writer_of_int_and_float_random_number(2,'int_float.dat')