# Создать функцию которая создает бинарные файлы с указанным расширением
#Функция принимает следующие параметры: расширение, мин длинна случ. сгенерированного имени(по умолчанию 6),
#максимальния длинна имени(30),  минимальное колличество рандомно сгенерированное колличество байт (256),
#максилальное число байт(по умолч 4096), кол-во файлов по умолчанию 42


from pathlib import Path
from random import randbytes, randint, sample,choice
from string import ascii_letters
import os  
def get_extension(list_of_extensions:list[str])->str:
    return choice(list_of_extensions)
def create_bfiles(list_of_extensions:list[str] ,dir:str, min_name:int = 6 , max_name:int = 30 , min_bite:int = 256 , max_bite:int = 4096, count:int = 42):    
    for _ in range(count):
        end = False
        while not end:
            name_size = randint(min_name , max_name)
            file_name = ''.join(sample(ascii_letters , name_size)) + '.' + get_extension(list_of_extensions)
            if not os.path.exists(file_name): end = True
        if not os.path.exists(dir):
            os.mkdir(dir)
        file_name = os.path.join(os.getcwd(),dir , file_name)     
        #file_name = Path().cwd()/'Data'/file_name
        with open(file_name,'ab') as file:
            size = randint(min_bite,max_bite)
            result = randbytes(size)
            file.write(result)

create_bfiles(['txt','doc','md','rtf','ogg','avi','mp4','jpg','png','bmp','mov','mp3'],'Data',count=50)
