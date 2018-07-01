# в моем коде проблема в том, что я не понимаю, как читать файлы из пути '/tmp/file.txt', как указано в задании
# т.е. если указать полный реаьный путь с существующим файлом, то программа работает, если же сокращенный,
# то программа не находит такую директорию. Я не понимаю как этого избежать

#я конечно сделала так, чтобы этот запрос работал. Но он работает только в том случае, если в папка temp находится
# в той же папке что и код и в ней есть вызываемый файл

# есть вероятность, что заказчик имел ввиду не это, а то, что вызываемый файл должен сам создаться при зупуске класса
# в общем, я, конечно, могу организовать и это

#в итоге имеем программу, которая, если что, создаст файл сама, если его не существует по выбранному направлению

# работать не будет только в том случае, если файл все-таки будет искаться по какому-то другому пути, где-то далеко на диске, без указания полного пути к диску

import tempfile
import os
import random
import string

class File:

    def __init__(self, link):
        self.current = 0
        self.linkstart = link

        name = link.split('/')[-1]

        s_path = os.path.join(tempfile.gettempdir(), name)
        try:
            f = open(s_path)
        except IOError as e:
            with open(s_path, 'w') as f:
                chars = string.ascii_uppercase + string.digits
                f.write(''.join(random.choice(chars) for _ in range(5)) + '\n' ''.join(random.choice(chars) for _ in range(4)) + '\n' ''.join(random.choice(chars) for _ in range(3)) + '\n')
                f.close()
        else:
            pass

        '''
        #код на случай какой-то другой обработки пути к файлу, но он тоже не для всех вариантов работает
        
        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = "temp/first.txt"
        link = os.path.join(script_dir, rel_path)
'''
        self.link = s_path
        link = s_path
        with open(link) as f:
            self.text_inside = f.read()
        with open(link) as f:
            self.text_inside = f.read()
        with open(link) as f:
            self.end = len(f.readlines())
        with open(link) as f:
            self.list = list(f)

    def __str__(self):
        return self.linkstart

    def write(self, text):
        with open(self.link, 'a') as f:
            return f.write(text)
        f.close()
    def __add__(self, obj):
        storage_path = os.path.join(tempfile.gettempdir(), 'temprorary_week4.data')
        with open(storage_path, 'w') as f:
            f.write(self.text_inside + obj.text_inside)
            f.close()
        with open(storage_path) as f:
            print(f.read())

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.list[self.current]
        self.current += 1
        return result



a = File('tmp/file.txt')
print(a.text_inside)
for line in File('/tmp/file.txt'):
    print(line)
