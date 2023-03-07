# np_mean_var_std.py v0
# https://www.freecodecamp.org/news/how-to-analyze-data-with-python-pandas/

# import only necesary modules
import numpy as np


# Create a function named calculate() in mean_var_std.py that uses Numpy to output
# the mean, variance, standard deviation, max, min, and sum of the rows, columns,
# and elements in a 3 x 3 matrix.  --NOW only w/numpy
def calculate (lst):
    if len(lst) != 9:
        raise ValueError ('List must contain nine numbers.')
    
    a = np.reshape(lst, (3,3))
    
    dic = {'mean': [], 'variance': [], 'standard deviation': [],
           'max': [], 'min': [], 'sum': []}
    
    # Adding calculated values (mean-var-stf) along axes to dic
    for ax in (0, 1):
        dic['mean'].append(list(a.mean(axis=ax)))
        dic['variance'].append(list(a.var(axis=ax)))
        dic['standard deviation'].append(list(a.std(axis=ax)))
        dic['max'].append(list(a.max(axis=ax)))
        dic['min'].append(list(a.min(axis=ax)))
        dic['sum'].append(list(a.sum(axis=ax)))

    # Adding calculated flattened values (mean-var-stf) to dic
    dic['mean'].append(a.mean())
    dic['variance'].append(a.var())
    dic['standard deviation'].append(a.std())
    dic['max'].append(a.max())
    dic['min'].append(a.min())
    dic['sum'].append(a.sum())

    return dic

# The input of the function should be a list containing 9 digits. The function
# should convert the list into a 3 x 3 Numpy array, and then return a dictionary
# containing the mean, variance, standard deviation, max, min, and sum along
# both axes and for the flattened matrix.

#print(calculate([0,1,2,3,6,7,8]))
print(calculate([0,1,2,3,4,5,6,7,8]))
try:
    print(calculate([1,2,3,4,5,6,7]))
except ValueError as e:
    print('\n PERFECT! ValueError raised:', e, '\n')

# If a list containing less than 9 elements is passed into the function, it
# should raise a ValueError exception with the message: "List must contain nine
# numbers." The values in the returned dictionary should be lists and not
# Numpy arrays.

### EXTRA: extra:
np.reshape([0, 0, 1, 1, 2, 2, 3, 3], (4, 2)).T
# array([[0, 1, 2, 3],
#        [0, 1, 2, 3]])

np.reshape([0, 0, 1, 1, 2, 2, 3, 3], (2, 4))
# array([[0, 0, 1, 1],
#        [2, 2, 3, 3]])


