class FileReader:
    def __init__(self, link):
        try:
            f = open(link)
            self.read = f.read
        except IOError:
            return print("")


#обработаем исключение:
'''
try:
    with open("test.txt") as file_handler:
    for line in file_handler:
        print(line)
except IOError:
    print("error")
'''
reader = FileReader("example.txt")
print(reader.read())

'''
f = open('example.txt')
print(f.read())
'''