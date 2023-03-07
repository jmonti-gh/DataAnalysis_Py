# pd_mean_var_std.py v0
# https://www.freecodecamp.org/news/how-to-analyze-data-with-python-pandas/

# import only necesary modules
import pandas as pd


# Create a function named calculate() in mean_var_std.py that uses Numpy to output
# the mean, variance, standard deviation, max, min, and sum of the rows, columns,
# and elements in a 3 x 3 matrix.  --NOW only w/pandas
def calculate (lst):
    if len(lst) != 9:
        raise ValueError ('List must contain nine numbers.')
    ## more to analyse, lets continue with numpy only..
    s = pd.Series(lst)
    s1 = s.reshape
    pd.DataFrame.reshape(lst, (3,3))
    return a



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

# Typical ValuError
a = float('pto5')
#raise ValueError

# If a list containing less than 9 elements is passed into the function, it
# should raise a ValueError exception with the message: "List must contain nine
# numbers." The values in the returned dictionary should be lists and not
# Numpy arrays.