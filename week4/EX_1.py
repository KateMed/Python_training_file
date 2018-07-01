import random
class NoisiInt:
    def __init__(self, value):
        self.value = value
    def __add__(self, obj):
        #noise = random.uniform(-1, 1)
        return self.value + obj.value

a = NoisiInt(10)
b = NoisiInt(20)
print(a+b)