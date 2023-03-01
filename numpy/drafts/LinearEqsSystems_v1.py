# System of linear equations solution using Cramer's rule

import copy
import numpy as np
import matplotlib.pyplot as plt

def ask_sys(n):
    ''' Display an example of Linear Eq. Sys. for the case user entered
    n -> ukns_num (unknows' number), AND ask coeficients.
    ret_str: string to return'''

    # Check invalid n values (unknows numbers) expected
    if n < 1 and n > 16: return 'Invalid function argument'

    sub_sep = ' ' * 4
    print(sub_sep + 'In a case of a Linear Equations System of', n, 'unknows:')

    ret_str = ''
    eq_sep = ' ' * 8
    base1 = eq_sep + 'a.x1 + b.x2'
    base2 = eq_sep + 'f.x1 + g.x2'
    base3 = eq_sep + 'm.x1 + n.x2 + o.x3'
    qbegin = sub_sep + 'Please enter the coeficients:'
    qend = ', separated by one space each other\n' + sub_sep

    if n == 3:
        print(base1 + ' + c.x3 = d')
        print(base2 + ' + h.x3 = i')
        print(base3 + ' = p')
        ret_str = input(qbegin + ' a b c d f g h i m n o p' + qend)
    elif n == 2:
        print(base1 + ' = d')
        print(base2 + ' = i')
        ret_str = input(qbegin + ' a b d f g i' + qend)
    elif n == 1:
        print(' LINE: not a sytem.. -> later')
    else:
        print(' to try "a11, a12....')

    #if ret_str == '': ret_str = '3 2 9 1 5 13'
    if ret_str == '': ret_str = '3 2 1 9 5 13 4 75 1 2 3 5'
    return ret_str.strip()


### --- main --- ###

print('\n ~~~ Linear Equation System Resolver ~~~\n')

# User must enter a valid unknows number
ukns_num = 0
while not ukns_num: 
    try:
        ukns_num = int(input('How many unknows does your system have? '))
        assert ukns_num >= 1 and ukns_num <= 16
    except:
        print('You must enter a postive integer number lesser than 16')
        print('   - We took lesser than 16 for computational hardware limitations')

## I known numbers of unknowns (ukns_num), then i can build:
# 3. generic coef, Matrix (gcm), and 4. generic results vector(grv)
# 1. Build base Matrix (bM): base to be fill w/ actual values
bM = [[0 for i in range(ukns_num)] for j in range(ukns_num)]
# 2. Build unknowns vector (u) [x1, x2, ..., xi, ..., xN]
u_lst = []
for i in range(1, ukns_num + 1):
    i_str = str(i)
    u_lst.append('x' + i_str)
u = np.array(u_lst)
# 3. Build generic coeficients Matrix [c11, c12 ... c21, c22, ... cN1, cNN]
pass
# 4. Build generic results vector(grv) [r1, r2, .. ri,... rN]



# To obtain valids coeficients
while True:
    coefs = ask_sys(ukns_num).split(' ')
    if len(coefs) == ukns_num * ukns_num + ukns_num:
        break
    # Also I should check if coeficients al all numbers - later

## Build de Matrixs
# Build unknowns coeficients Matrix (CM)
CM_lst = copy.deepcopy(bM)
for i in range(ukns_num):
    k = i * ukns_num
    if i > 0: k = k + 1
    for j in range(ukns_num):
        CM_lst[i][j] = coefs[k]
        k += 1
CM = np.array(CM_lst)       # CM Matrix Ready             

# Build results vector (r)
r_lst = []
for ri in range(ukns_num, len(coefs), ukns_num):
    if ri > ukns_num: ri += 1
    r_lst.append(coefs[ri])
r = np.array(r_lst)

## Build unknowns vector [x1, x2, ..., xi, ..., xN]
u_lst = []
for i in range(1, ukns_num + 1):
    i_str = str(i)
    u_lst.append('x' + i_str)
u = np.array(u_lst)

## Display the Lin Eq. System entered
print()
for i in range(ukns_num):
    for j in range(ukns_num):
        print(CM[i,j] + '.' + u[j], end='')
        if j < ukns_num - 1: print(' + ', end='')
    print(' =', r[i])


## Build 








    