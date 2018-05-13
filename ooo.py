'''
a={}
a[0]='##'*2
a[1]='2134'
print(a.values(),type(a))
'''


'''
num_s=
if num_s <= 0:
    print('Лестница не может состоять из отрицательных ступенек или не иметь ступенек вовсе, введите большее количество ступенек')
if num_s=={}:
    print('Вы ничего не ввели, введите пожалуйста количество ступенек')
for i in range(1,num_s+1):
    print(' '*(num_s-i),'#'*i)
'''


'''
a = 7
b = 3
c = 2

import math
D = b**2-4*a*c
if D > 0:
    print('x1 = ', (-b+D**(1/2))/(2*a))
    print('x2 = ', (-b-D**(1/2))/(2*a))
elif D < 0:
    NewD=(math.fabs(D)**(1/2))
    #the same
    #NewD = D.__abs__()**(1/2)
    print('Мнимые корни')
    print('x1 = ', (-b+1j*NewD)/(2*a))
    print('x2 = ', (-b-1j*NewD)/(2*a))
'''

from collections import OrderedDict


ordered= OrderedDict()
for number in range(10):
    ordered[number]=str(number)
for key in ordered:
    print(key)
