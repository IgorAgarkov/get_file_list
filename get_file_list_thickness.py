# -*- coding: utf8 -*-
import os
import re
files = os.listdir()
text_file = open('Список файлов DXF.txt', 'w')
j = 0
for i in files:
    if i[-4:].lower() == '.dxf':
        j += 1
        pattern = re.compile('-(\d,?\.?\d?)[^-\d]')         # ищем: 'дефис (цифра {одна} запятая {0 или одна} точка {0 или одна} цифра {0 или одна}) не_дефис_не_цифра {одна}   - берём то что в скобках
        if len(pattern.findall(i)) != 0:                    # если паттерн найден
            thickness = pattern.findall(i)[0].rstrip('.')   # убираем точку в конце на случай, когда толщина указана в конце имени файла перед расшерением
        else:                                               # если паттерн не найден
            thickness = ''
        text_file.write(str(j) + '\t' + i.rstrip('.dxf') + '\t' + '\t' + '\t' + thickness + '\n')
text_file.close()
