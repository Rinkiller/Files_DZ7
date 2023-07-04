# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с цифрами и именами
# перемножте пары чисел.  В новый фаил сохраните имя и произведение
# если результат перемножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат перемножения положительный, сохраните имя прописными буквами и произведение округленное до целого
# в результирующем файле должно быть столько же строк, сколько и в более длинном
# При достижении конца более короткого файла, возвращайтесь в его начало 

def get_lines_in_file(file:open) -> int:
    lenght = len(list(file))
    file.seek(0,0)
    return lenght

def write_data_of_dat_and_txt_files(file_dat_name:str,file_txt_name:str,result_file_name:str) -> None:
    with (open(file_dat_name,'r',encoding='utf-8') as file_dat ,
          open(file_txt_name,'r',encoding='utf-8') as file_txt,
          open(result_file_name,'w',encoding='utf-8') as file_result):
        line_in_dat = get_lines_in_file(file_dat)
        line_in_txt = get_lines_in_file(file_txt)
        if line_in_dat > line_in_txt: 
            counts = line_in_dat
        else: 
            counts = line_in_txt
        for index in range(counts):
            if index + 1> line_in_dat: file_dat.seek(0,0)
            if index + 1> line_in_txt: file_txt.seek(0,0)
            num1 , num2 = file_dat.readline()[:-1].split('|')
            if (int(num1) * float(num2)) > 0: file_result.write(f'{file_txt.readline()[:-1].upper()}  {int(int(num1) * float(num2))}\n')
            else: file_result.write(f'{file_txt.readline()[:-1].lower()}  {(-int(num1)) * float(num2)}\n')



write_data_of_dat_and_txt_files('int_float.dat','psevdo_names.txt','rezult.dat')