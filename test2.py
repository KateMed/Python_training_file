template= "%s lala %s bla-bla"  % ("mama", "papa")
print(template)

print("{} lala  {} bla-bla".format('mama','papa'))
s="mama"
l='papa'

b=f'{s} lala {l} bla-bla'
print(b)
num=2/3
print(f'{num:.3f}')
#identically
n=f'{num:.3f}'
print(n)


print(bool(0.000001))
print(bool(0.0))
n='privet'
print(n[0:1])

pi=3.1415926
pi=f'{pi:#0.2f}'
print(type(pi))