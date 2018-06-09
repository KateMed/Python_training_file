import sys
import argparse

def decorator():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', '--val')
    namespace = parser.parse_args()
    a = namespace.key
    return a
print('lala')
print('key: ', a)
'''''
def storage():
    tot=[]
    while True:
        value=yield tot
        if not value: break
        tot+=value

test=storage.send()
'''''