#Импорт пакета
#"""""
import mypackage
#если импортирование модуля происходит напрямую из интерпретатора python (если запускать из консоли) либо запускается напрямую здесь,
# то условие снизу срабатывает. Если же  снначала зайти в пайтон, а потом запустить, то условие не сработает
if __name__=='__main__':
    print('marta')
#"""""

#Импортирование  конкретной функции из конкретного модуля
#"""""
import mypackage.untils
print('martauntils')
print(mypackage.untils.multiply(2,3))
#"""
# THE SAME
#"""""
from mypackage.untils import multiply
print('martamultiply')
print(multiply(2,3))
#"""""

#Имортирование всех функций из конкретного модуля (не рекомеднуется)
from mypackage.untils import *
print('martall')
print(multiply(2,3),laptop(2,3,4))
