# -*- coding: utf8 -*-
import os
#directory = 'tmp'  # вложенная папка с файлами
files = os.listdir()
text_file = open('Список папок.txt', 'w')
j = 0
for i in files:
    if os.path.isdir(i):
        j += 1
        text_file.write(str(j) + '\t' + i.rstrip('.dxf') + '\n')
text_file.close()