### System of linear equations solution using Cramer's rule
# v7 more refactor w np.array slicing

### TO-DO:
# 1. refactor one funct for the user inputs   - DONE!
# 2. Obtain the actual equations format separated for 2D graph.
# 3. mk 3D graph
# 4. to analyze refactor 2D image construction

import numpy as np
import itertools as it
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show

### Functions

def bld_generic_vect(letter, n):
    ''' Build Generic Vector of strings numbered. Return 1D list
    letter: letter of the elements. n: number elements of the vectors'''
    return [letter + str(i) for i in range(1, n + 1)]


def ask_nums(side):
    ''' Ask user to enter valid coeficients and independent terms nums.
    global vars used: ukns_num, gCM, guv, grv. return two 1D-list 
    (0-strings, 1-floats) or (False, False) if invalid data was entered'''

    if not (side == 'coeficients' or side == 'independent terms'):
        print('ERROOOORRR!! -internal error-')
        return 'ERROR, ask_nums() incorrect argument'

    if side == 'coeficients':
        print('\n---> In a case of a Linear Equations System of', ukns_num, 'unknows...')
        print(drw_sys(gCM, guv, grv))   # Display generic LE system of ukns_num unknowns
        print('* c: coeficients, x: unknowns, r: independent terms')

    print('\nPlease enter the ' + side + ' with sign, separated by one space each other:')

    if side == 'coeficients':
        for i, j in it.product(range(ukns_num), range(ukns_num)):
            print(gCM[i,j], end=' ')
    elif side == 'independent terms':
        for i in range(ukns_num):
            print(grv[i], end=' ')
    print()

    nums = input().strip()
    lst = nums.split(' ')

    # check nums entered correspond in number + if all are valid decimals
    err_msg = ''
    if (side == 'coeficients' and len(lst) != ukns_num * ukns_num) or \
        (side == 'independent terms' and len(lst) != ukns_num):
        err_msg = 'Incorrect number of ' + side
 
    try:
        lft = list(map(lambda x: eval(x), lst))
    except:
        err_msg = 'Invalid data entered'

    if err_msg:
        print('\n' + '*****  ERROR! ' + err_msg + ', try again...')
        return (False, False)       # tuple cause funct retrun two objects.    
    # in red to stderr!!.. or an own objet error (pass error beetween functions).

    return lst, lft      # strings for presentation, float for display and calcs.
        

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
print("\n ~~~~ Linear Equation System Resolver  - using Cramer's rule - ~~~~\n")

### Ask user to enter a valid number of unknowns (ukns_num)
while True: 
    try:
        ukns_num = int(input('How many unknows does your system have? '))
        assert ukns_num >= 1 and ukns_num <= 16
        break
    except:
        print('You must enter a postive integer number lesser than 16')
        print('   - We took lesser than 16 only to set an upper limit')


### Ask user to enter coeficients & independent terms (resutls)
## To display generic systems of 'ukns_num' linear equations:

# 1. Build base Matrix (bM) for later use
bfM = np.empty([ukns_num, ukns_num], dtype= float)
bsM = bfM.astype('<U16')

#bsM = np.empty([ukns_num, ukns_num], dtype= '<U16')

# 2. Build generic coeficients Matrix (gCM) [c11, c12 ... c21, c22, ... cN1, cNN]
#gCM = bfM.astype('<U16').copy()                     
gCM = bsM.copy()                                    # like deepcopy 
for i, j in it.product(range(ukns_num), range(ukns_num)):
    gCM[i,j] = 'c' + str(i+1) + str(j+1)

# 3. Build generic unknowns vector (guv) [x1, x2, ..., xi, ..., xN] AND
# 4. Build generic idependent terms (results) vector(grv) [r1, r2, .. ri,... rN]
guv = np.array(bld_generic_vect('x', ukns_num))
grv = np.array(bld_generic_vect('r', ukns_num), dtype='<U16')

## Ask the user to enter valids coeficients an indep. terms (results)
coef_s, coef_f = ask_nums('coeficients')            # two 1D lst (strings & floats), 
while coef_s == False:                              # valid coeficients
    coef_s, coef_f = ask_nums('coeficients')

res_s, res_f = ask_nums('independent terms')        # two 1D lst (strings & floats),
while res_s == False:                               # valid independent terms (resutls)
    res_s, res_f = ask_nums('independent terms')

### Show data entered, build strings coef-Matrix and string result-vector
# Build Coeficients float & strings Matrixs (CM & CsM)
CsM = bsM.copy()                # like deepcopy
CM = bfM.copy()                         
for i in range(ukns_num):
    k = i * ukns_num
    for j in range(ukns_num):
        CsM[i,j] = coef_s[k]
        CM[i,j] = coef_f[k]
        k += 1    

# Build results string & float vector (rs & r)
rs = np.array(res_s, dtype='<U16')
r = np.array(res_f, dtype=float)

# Display the actual LE System 
print('\n ---> Actual System of Linear Equations:')
print(drw_sys(CsM, guv, rs))

### NOT REALLY necesary only to have other view - later
print('\n ---> Linear Algebra representation::')
print(CM, '*', guv, '=', r)

### CALCULATE: Unknowns for the system -  I have CM an r as float
# 1st check if det(CM) == 0 => can't apply Cramer´s rule
detCM = np.linalg.det(CM)
if detCM == 0:
    print('\nCoeficients Matrix Det:', detCM, type(detCM))
    print('Sorry can not resolve this System, goodbye!\n')
    quit()

# Build the unknowns matrixs AND calc each unknown (store ukns in ulst list)
ulst = [0. for i in range(len(guv))]    # empty List for unknows values
for uk in range(len(guv)):              # for every unknown [x1, ..., xN]
    UKM = CM.copy()                     # born base uknown matrix
    UKM[:, uk] = r      # replace values of uk col by r vector (real uk matrix, Cramer)
    ulst[uk] = round(np.linalg.det(UKM) / detCM, 4)     # Cramer's rule

print('\n ---> Solution of the System:')
print(guv)
print(ulst)      # solution list

cont = input('\nPress return see graphs of the system...')

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





