# создать функцию, сортирующую файлы в указанной директории и 
# перемещающую их в различные папки по критерим( видео, музыка, картинки, документы)
# неотсортированные файлы остаются в указанной директории

import os
def sorted_chadge_directory(dir_name:str):
    os.chdir(dir_name)
    for folder in ['video','audio','docs','pictures']:
        if not os.path.exists(folder):
            os.makedirs(folder)
    for file in os.listdir():
        if os.path.isfile(file):
            extension = file.split('.')[1]
            if extension in ['txt','doc','rtf']:
                os.replace(file,os.path.join('docs',file))
            if extension in ['md','ogg','mp3']:
                os.replace(file,os.path.join('audio',file))
            if extension in ['mp4','mov','avi']:
                os.replace(file,os.path.join('video',file))
            if extension in ['jpg','png','bmp']:
                os.replace(file,os.path.join('pictures',file))

    
    
sorted_chadge_directory('Data')

