class File:
    def __init__(self, link):
        self.link = link
    def write(self, text):
        with open(self.link, 'a') as f:
            return f.write(text)
        f.close()
file = File('example.txt')
file.write('lalaMo')