#Использование sys.argv[1]...sys.argv[n] позволяет вводить аргументы в этот модуль прямо из терминала.
# Пример вызова прогрммы: "python summtest.py 123"

import sys
print(sys.argv[0])
s_s=sys.argv[1]
l=len(sys.argv[1])
sum=0
for i in range(0,l):
    sum=sum+int(s_s[i])
print('Summa= ',sum)

'''
l2=('564')
print(type(l2),l2[2])
#не получилось понять, как обращаться поэлементно к интеджер. Это вообще возможно? к(2)?
k=int(l2)
print('int',k,type(k))
'''