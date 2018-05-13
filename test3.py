# encode/decode
ex_str="hi pig"
byte_ex_str = ex_str.encode(encoding="utf-8")
print(byte_ex_str)
print(type(byte_ex_str))

for less in byte_ex_str:
    print(less)

#the bin work just for numbers
#print(bin(j))
print(bin(8))

#we can get reverse code  i.e. decode str
ex_str_reverse=byte_ex_str.decode()
print(ex_str)

