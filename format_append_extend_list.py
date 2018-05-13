collections=['list','tuple','dict','set']
for collection in collections:
    #.format вставляет значения в {}!! (аналогичным образом действует  оператор %. называтся это все форматирование строк!)
    print('Learning {} ...'.format(collection))


#enumerate позволяет выводить индексы вместе с содержимым list(список)
for idx,collection in enumerate(collections):
    print('#{} {}'.format(idx,collection))

collections.append('marta')
print(collections)

collections.extend(['ponyset','unicornset'])
print(collections)


collections.extend(collections)
print(collections)

collections += [None]
print(collections)

del collections[4]
print(collections)


num=[4,17,19,9,2,6,10,13]
print(min(num))
      #max
      #sum

li=['python','course','coursera']
print(' appbetween '.join(li))

#списки!!
list1=['a','b','c','d']
lis=list('sfgh')