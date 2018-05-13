# СЛОВАРИ!
empty_dict=dict()
empty_dict={}
collections_map={
                 'mutable':['list','set','dict'],
                 'immutable':['tuple','frozenset']
}

print(collections_map('immutable')

# del, .update ({'a':'b'})- добавление .pop('')-уданение\возвращенине, .setdefault('a','b')-добавление
# он же почему то при повторном желании записать значение в ключь(т.е. перезаписать) выдает старое значение

# итерируемся по ключам!!

# возможность получать ключи в том порядке, в котором они записывались
#то что ниже почему то не работает в этом коде, в общем и целом это рабочий кусок
'''
from collections import OrderedDict


ordered= OrderedDict()
for number in range(10):
    ordered[number]=str(number)
for key in ordered:
    print(key)
'''