#списки! изменяемые!!

import random

numbers = []
# ниже стоит _ , что говорит о том, что там не важно, что присваивается при итерации, а важно, сколько всего итераций
# (обычно мы пишем for i in range(1,20), имея в виду присвоение этих значений i, нам это не нужно, поэтому мы ставим _)
for _ in range(10):
    numbers.append(random.randint(1,20))
print('только что созданный список',numbers)
# сортировка!!

# возвращает новый список!!!
print('сортированный, но не перезаписанный',sorted(numbers))
# меняет старый список!!
numbers.sort()
print('сортированный и перезаписанный',numbers)

# сортировка в обратном порядке
print(numbers[::-1])
# the same
print(sorted(numbers,reverse=True))
#numbers.sort(reverse=True)