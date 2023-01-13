# -*- coding: utf8 -*-
import os
import re
from operator import itemgetter

def get_str_thickness(file_name):
    """
    Функция вычленяет из имени файла числовое значение (str) по паттерну (толщина изделия).
    """
    pattern = re.compile('-(\d,?\.?\d?)[^-\d]')                     # ищем: 'дефис (цифра {одна} запятая {0 или одна} точка {0 или одна} цифра {0 или одна}) не_дефис_не_цифра {одна}   - берём то что в скобках
    if len(pattern.findall(file_name)) != 0:                        # если паттерн найден
        str_thickness = pattern.findall(file_name)[0].rstrip('.')   # убираем точку в конце на случай, когда толщина указана в конце имени файла перед расшерением
    else:                                                           # если паттерн не найден
        str_thickness = ''
    return str_thickness

def natural_sort(file_name): 
    """
    функция учитывает при сортировке числовые значения (как в файловом менджере Windows)
    """
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)] 
    return sorted(file_name, key=alphanum_key)

files = os.listdir()
files = natural_sort(files)      # сортируем список файлов

text_file = open('!_Список файлов DXF.txt', 'w')
j = 0                            # счётчик для нумерации строк в файле
for i in files:
    if i[-4:].lower() == '.dxf':
        j += 1
        text_file.write(str(j) + '\t' + i.rstrip('.dxf') + '\t' + '\t' + '\t' + get_str_thickness(i) + '\n')
text_file.close()