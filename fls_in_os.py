import os
import time, datetime
# Для уменьшения кол-ва выбираемых ф-лов ограничимся файлами Python, которые
#  не начинаются на символы нижнего подчеркивания (_ и  __)
# if file.endswith('.py') and file.title()[:1] != '_':

root = r'e:\Python\lesson'
# directory = r'e:\Python\lesson'
directory = '.'
# print(os.listdir(directory))

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.py') and file.title()[:1] != '_':
            filepath = os.path.join(dirs[0]+'\\'+ file)
            # filepath = os.getcwd() + file) # можно и так
            filetime = os.path.getmtime(file)
            formatted_time = time.strftime("%d.%m.%Y %H:%M",
                                                time.localtime(filetime))
            filesize = os.path.getsize(file)
            parent_dir = os.path.dirname(filepath)
            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер:'
                   f' {filesize} байт, Время изменения: {formatted_time}, '
                  f'Родительская директория: {parent_dir}')