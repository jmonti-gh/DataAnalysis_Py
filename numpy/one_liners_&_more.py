## one_liners & more 

import numpy as np
import decimal as dc
import sys


s1 = np.array(range(4))
s2 = np.array([chr(i) for i in range(97, 97 + 5)])
print('s2:', s2)

### swap onjects 
s1, s2 = s2, s1
print('s2:', s2)

div = 4 / 3
dc_div = dc.Decimal(4) / dc.Decimal(3)
print('div:', div, type(div))
print('dc_div:', dc_div, type(dc_div))
print(s2[0], type(s2[0]))

### reverse string
tring1 = 'was it a car or a cat i saw'
print(tring1, ' - ', tring1[::-1])
# palindrom
tring2 = 'Madam'
print(tring2, ' - ', tring2[::-1])

### factorial - !! PEP8 lambdas
fact = lambda n: [1,0] [n>1] or fact(n-1)*n
for i in range(9):
    print(fact(i), end=' ')
print()

### fibonacci - !! PEP8 lambdas
fib = lambda x: x if x <= 1 else fib(x-1) + fib(x-2)
for i in range(9):
    print(fib(i), end=' ')
print()

### ioerror - errno list
# jm task

### list comprehension

### generatosr (i for i in rang(5))

### asign variables values if ..else (like fibo)

### np.array from list - strings - set - dicts - sys.getsiszeof

print('\n---> np.array from lists - sys.getsiszeof()')

def prts(obj):
    print(obj, type(obj), type(obj[np.random.randint(0, len(obj))]))
    print(sys.getsizeof(obj), '  -  ', end='')
    for el in obj:
        print(sys.getsizeof(el), end=' ')
    try:
        print(' - ', type(el), obj.dtype, obj.itemsize, obj.nbytes)
    except:
        print(type(obj), "obj. has no attribute 'dtype'")
    print()

lista = [str(i) for i in range(10)] + [chr(i) for i in range(65, 71)]
prts(lista)

vectora = np.array(lista)
prts(vectora)

vectorb = np.array(lista, dtype= '<U2')
prts(vectorb)

trin = ''.join(lista)
prts(trin)

tri2 = ''.join(vectora)
prts(tri2)

listi = [i for i in range(10)]
prts(listi)

vectori = np.array(listi)
prts(vectori)

vector8 = np.array(listi, dtype= np.int8)
prts(vector8)

vector6 = np.array(listi, dtype= 'int16')
prts(vector6)


# lst = [str(i) for i in range(10) if i < 10 else chr(i) for i in range(65, 72)]
# print(lst)