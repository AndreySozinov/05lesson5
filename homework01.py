# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

from typing import Any


def file_path(link: str) -> tuple[str, Any, Any]:
    *path, file = link.split('/')
    file_name, file_ext = file.split('.')
    path_comm = '/'.join(path)
    return path_comm, file_name, file_ext


print(file_path('https://www.site.ru/pics/post/some_file.txt'))
