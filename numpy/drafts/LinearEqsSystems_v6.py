### System of linear equations solution using Cramer's rule
# v4 refactor cuple of pieces & dinamic graphs (w/)

import numpy as np
import itertools as it
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show

### Functions

def bld_generic_vect(letter, n):
    ''' Build Generic Vector of strings numbered. Return 1D list
    letter: letter of the elements. n: number elements of the vectors'''
    return [letter + str(i) for i in range(1, n + 1)]

def drw_sys(M, vu, vr):
    ''' Return a string of the whole system of LE
    M: coef. Matrix, vu: unknows vector, vr: indep. terms vector'''
    ret_str = ''
    for i in range(ukns_num):
        for j in range(ukns_num):
            ret_str += str(M[i,j]) + '.' + str(vu[j])
            if j < ukns_num - 1: ret_str += ' + '
        ret_str += ' = ' + str(vr[i] + '\n')
    return ret_str.strip()


##### ----- main ----- #####
print('\n ~~~ Linear Equation System Resolver ~~~\n')

### Ask user to enter a valid number of unknowns (ukns_num)
while True: 
    try:
        ukns_num = int(input('How many unknows does your system have? '))
        assert ukns_num >= 1 and ukns_num <= 10
        break
    except:
        print('You must enter a postive integer number lesser than 10')
        print('   - We took lesser than 16 for computational hardware limitations')


### Ask user to enter coeficients & independent terms (resutls)
## To display generic systems of 'ukns_num' linear equations:

# 1. Build base Matrix (bM) for later use
bM = np.empty([ukns_num, ukns_num], dtype= '<U16')

# 2. Build generic coeficients Matrix (gCM) [c11, c12 ... c21, c22, ... cN1, cNN]
gCM = bM.copy()                                                 # like deepcopy 
for i, j in it.product(range(ukns_num), range(ukns_num)):
    gCM[i,j] = 'c' + str(i+1) + str(j+1)

# 3. Build generic unknowns vector (guv) [x1, x2, ..., xi, ..., xN] AND
# 4. Build generic idependent terms (results) vector(grv) [r1, r2, .. ri,... rN]
guv = np.array(bld_generic_vect('x', ukns_num))
grv = np.array(bld_generic_vect('r', ukns_num), dtype='<U16')

## Ask the user to enter valids coeficients
while True:
    print('\n---> In a case of a Linear Equations System of', ukns_num, 'unknows...')
    print(drw_sys(gCM, guv, grv))   # Display generic LE system of ukns_num unknowns
    print('* c: coeficients, x: unknowns, r: independent terms')
    
    # Enter valids coeficients (numbers and quantity):
    print('\nPlease enter the coeficients seseparated by one space each other:')
    for i, j in it.product(range(ukns_num), range(ukns_num)):
        print(gCM[i,j], end=' ')
    print()
    coefs_inp = input().strip()
    coefs = coefs_inp.split(' ')            # Make a 1D list of coeficients (str)
    
    # check num of coeficients correspond unknowns number enterd
    if len(coefs) == ukns_num * ukns_num: 
        break
    else:
        print(coefs, 'wrong!')
        print('ERROR! -> Incorrect numbers of coeficients, try again:')          
    # Also I should check if coeficients are all numbers - later

## Ask the user to enter valids independient terms (r)
while True:
    print('\nPlease enter the independient terms separated by one space each other:')
    for i in range(ukns_num):
        print(grv[i], end=' ')
    print()
    res_inp = input().strip()
    res = res_inp.split(' ')
    if len(res) == ukns_num:
        break
    else:
        print(res, 'wrong!')
        print('ERROR! -> Incorrect numbers of independient terms, try again:')          
    # Also I should check if coeficients al all numbers - later


### Show data entered, build strings coef-Matrix and string result-vector
# Build Coeficients string Matrix (CsM) - str to make a display of actual system
CsM = bM.copy()
for i in range(ukns_num):
    k = i * ukns_num
    for j in range(ukns_num):
        CsM[i,j] = coefs[k]
        k += 1

# Build results string vector (r)
rs = np.array(res, dtype='<U16')       

# Display the actual LE System 
print('\n ---> Actual System of Linear Equations:')
print(drw_sys(CsM, guv, rs))


### CALCULATE: Unknowns for the system -  I have CM now i need Unknowns Matrix
# 1st i nedd numbers elements (no string) - convert CsM to CM (dtype=float) an rs
CM = CsM.astype(float)
r = rs.astype(float)

## Build the unknowns matrixs (store each Matrix in a Mlst list) AND
# calc each unknown (store ukns in ulst list) -- ver 7
Mlst = ['' for i in range(len(guv))]    # empty List of 2D-arrays
for uk in range(len(guv)):              # for every unknown [x1, ..., xN]
    Mlst[uk] = CM.copy()        # born w/ CM matrix
    Mlst[uk][:, uk] = r         # replace values of uk col by r vector             

# calc of unknows - store uknowns in ulst list
ulst = ['' for i in range(len(guv))]
for uk in range(len(guv)):      # for every unknown [x1, ..., xN]
    ulst[uk] = round(np.linalg.det(Mlst[uk]) / np.linalg.det(CM), 4)
### refactor up cause one loop.

print()
print(guv)
print(ulst)

cont = input('Press return see graphs of the system...')

if ukns_num == 2:
    ## 2D Sys GRAPHS -- to make grhaps nee dd x2 = f(x1)
    # esy to discover de unknown ¿?  divide every eq , every line
    # eq1: c11.x1 + c12.x2 = r1  => x2 = -c11/c12 * x1 + r1/c12
    # eq2: c21.x1 + c22.x2 = r2  => x2 = -c21/c22 * x1 + r1/c22

    # x axis - the part of interest to see the intersecction (ulst[0] -/+ 3)
    xis = np.linspace(ulst[0] - 3, ulst[0] + 3, 50)

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

    cont = input('Press return to interective graph...')

    p = figure(width=700, height=400, title='System of two linear equations: two rects')

    # add a line renderer
    p.line(xis, x2eq1, line_width=2, color='red')
    p.line(xis, x2eq2, line_width=2, color='green')

    show(p)

else:
    print('# --> No graphs available..., bye')





