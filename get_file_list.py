# -*- coding: utf8 -*-
import os
files = os.listdir()
text_file = open('Список файлов DXF.txt', 'w')
j = 0
for i in files:
    if i[-4:].lower() == '.dxf':
        j += 1
        text_file.write(str(j) + '\t' + i.rstrip('.dxf') + '\n')
text_file.close()