import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

import math
D=b**2-4*a*c
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
print('Это решение уравнения ', a, 'x^2 + ',b,'x + ',c)
