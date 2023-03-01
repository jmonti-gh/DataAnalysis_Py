### System of linear equations solution using Cramer's rule
# v3 twoo LE sytem graphs

import copy
import numpy as np
import matplotlib.pyplot as plt

def build_gen_vector(letter, n):
    ''' Build Generic Vector: e.g. u_lst por unknowns vector. Return 1D list
    letter: letter of the elements. ukn: number elements of the vectos'''
    lst = []
    for i in range(1, n + 1):
        i_str = str(i)
        lst.append(letter + i_str)
    return lst

def drw_sys(M, vu, vr):
    ''' Return a string of the whole system of LE
    M: coef. Matrix, vu: unknows vector, vr: indep. terms vector'''
    ret_str = ''
    for i in range(ukns_num):
    #print(eq_tab, end='')
        for j in range(ukns_num):
            #print(gCM[i,j] + '.' + u[j], end='')
            ret_str += str(M[i,j]) + '.' + str(vu[j])
            if j < ukns_num - 1: ret_str += ' + '
        ret_str += ' = ' + str(vr[i] + '\n')
    return ret_str.strip()


### --- main --- ###
print('\n ~~~ Linear Equation System Resolver ~~~\n')

## Ask user to enter a valid unknows number
ukns_num = 0
while not ukns_num: 
    try:
        ukns_num = int(input('How many unknows does your system have? '))
        assert ukns_num >= 1 and ukns_num <= 16
    except:
        print('You must enter a postive integer number lesser than 16')
        print('   - We took lesser than 16 for computational hardware limitations')


## I known numbers of unknowns (ukns_num), then i can build:

# 1. Build base Matrix (bM): base to be fill w/ actual values and create CM, X1M, ... XNM
bM = [[0 for i in range(ukns_num)] for j in range(ukns_num)]

# 2. Build generic coeficients Matrix (gCM) [c11, c12 ... c21, c22, ... cN1, cNN]
gCM_lst = copy.deepcopy(bM)
for i in range(ukns_num):
    i_str = str(i+1)
    for j in range(ukns_num):
        j_str = str(j+1)
        gCM_lst[i][j] = 'c' + i_str + j_str
gCM = np.array(gCM_lst)
#print(gCM, type(gCM))

# 3. Build generic unknowns vector (guv) [x1, x2, ..., xi, ..., xN]
guv = np.array(build_gen_vector('x', ukns_num))
#print(u, type(u))
        
# 4. Build generic idependent terms (results) vector(grv) [r1, r2, .. ri,... rN]
grv = np.array(build_gen_vector('r', ukns_num))
#print(r, type(r))


## Ask the user to enter valids coeficients
while True:
    print('\n---> In a case of a Linear Equations System of', ukns_num, 'unknows:\n')
    # Display generic system of LE of unkws number entered
    print(drw_sys(gCM, guv, grv))
    print('* c: coeficients, x: unknowns, r: independent terms')
    # Enter valids coeficients (numbers and quantity):
    print('\nPlease enter the coeficients seseparated by one space each other:')
    for i in range(ukns_num):
        for j in range(ukns_num):
            print(gCM[i,j], end=' ')
    print()
    coefs_inp = input().strip()
    coefs = coefs_inp.split(' ')
    if len(coefs) == ukns_num * ukns_num:
        #print(coefs, 'ok!')
        break
    else:
        print(coefs, 'wrong!')
        print('ERROR! -> Incorrect numbers of coeficients, try again:')          
    # Also I should check if coeficients al all numbers - later

## Ask the user to enter valids independient terms (r)
while True:
    print('\nPlease enter the independient terms separated by one space each other:')
    for i in range(ukns_num):
        print(grv[i], end=' ')
    print()
    res_inp = input().strip()
    res = res_inp.split(' ')
    if len(res) == ukns_num:
        #print(res, 'ok!')
        break
    else:
        print(res, 'wrong!')
        print('ERROR! -> Incorrect numbers of independient terms, try again:')          
    # Also I should check if coeficients al all numbers - later


## Build de Matrixs
# Build coeficients String Matrix (CsM) - str to make a display of actual system
CM_lst = copy.deepcopy(bM)
for i in range(ukns_num):
    k = i * ukns_num
    for j in range(ukns_num):
        CM_lst[i][j] = coefs[k]
        k += 1
CsM = np.array(CM_lst)       # CM Matrix Ready

# Build results string vector (r)
r_lst = []
for i in range(ukns_num):
    r_lst.append(res[i])
rs = np.array(r_lst, dtype='<U9')       

# Display the actual LE System 
print('\n ---> Actual System of Linear Equations:')
print(drw_sys(CsM, guv, rs))


## Calc Unknowns for the system -  I have CM now i need Unknowns Matrix
# 1st i nedd numbers elements (no string) - convert CsM to CM (dtype=float) an rs
CM = CsM.astype(float)
r = rs.astype(float)

# Build the unknowns matrixs - store e/Matrix in a list Mlst
# coud be a dict of the form {'x1M': x1M, .., 'xNM': xNM}
Mlst = ['' for i in range(len(guv))]
for uk in range(len(guv)):      # for every unknown [x1, ..., xN]
    # e/element of Mlst is a numpy array (the unknown array of uknown uk)
    Mlst[uk] = copy.deepcopy(CM)
    for i in range(len(r)):
        Mlst[uk][i,uk] = r[i]

# calc of uknows - the same store uknowns in a list
ulst = ['' for i in range(len(guv))]
for uk in range(len(guv)):      # for every unknown [x1, ..., xN]
    ulst[uk] = round(np.linalg.det(Mlst[uk]) / np.linalg.det(CM), 4)
### refactor up cause one loop.

print()
print(guv)
print(ulst)

cont = input('Press return to continue...')


## 2D Sys GRAPS -- to make grhaps nee dd x2 = f(x1)
# esy to discover de unknown ¿?  divide every eq , every line
# eq1: c11.x1 + c12.x2 = r1  => x2 = -c11/c12 * x1 + r1/c12
# eq2: c21.x1 + c22.x2 = r2  => x2 = -c21/c22 * x1 + r1/c22

# x axis - the part of interest to see the intersecction (ulst[0] -/+ 2)
xis = np.linspace(ulst[0] - 2, ulst[0] + 2, 50)

x2eq1 = -(CM[0,0] / CM[0,1]) * xis + r[0] / CM[0,1]
x2eq2 = -(CM[1,0] / CM[1,1]) * xis + r[1] / CM[1,1]

plt.title('System of two linear equations: two rects')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.plot(xis, x2eq1, color = "red", linewidth = 1.5, label = "Equation 1")
plt.plot(xis, x2eq2, color = "green", linewidth = 1.5, label = "Equation 2")

plt.axvline(x= ulst[0],linewidth= .5, linestyle= '-.')
plt.axhline(y= ulst[1],linewidth= .5, linestyle= '-.')
#ax.hlines(y=0.2, xmin=4, xmax=20, linewidth=2, color='r')
#plt.hlines(y= y, xmin= 1, xmax= 3, linewidth= .5)

plt.legend(loc= 'upper left')

plt.show()





