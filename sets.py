# множества!!!
empty_set=set()
number_set={1,2,3,3,4,5}
#множество выведет только одну тройку, т.к. в множествах хранятся только уникальные элементы!

odd_set=set()
even_set=set()

for number in range(10):
    if number % 2:
        odd_set.add(number)
    else:
        even-set.add(number)
print(odd_set)
print(even_set)

#логические (математические) операции над множителями!!

# объединение
union_set=odd_set | even_set
# the same
union_set=odd_set.union(even_set)

# перечесчение
intersection_set=odd_set & even_set
# the same
intersection_set=odd_set.intersection(even_set)

# разность
difference_set= odd_set-even_set
# the same
difference_set= odd_set.difference(even_set)

# симметричсекая разность (symmetric_difference)
# аналогично

#.remove(2) - удаление, add - добавление

# frozenset - неизменяемые множества!!!



