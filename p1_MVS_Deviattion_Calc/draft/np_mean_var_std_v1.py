# np_mean_var_std.py v1
# https://www.freecodecamp.org/news/how-to-analyze-data-with-python-pandas/


import numpy as np


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


# print(calculate([0,1,2,3,4,5,6,7,8]))
# try:
#     print(calculate([1,2,3,4,5,6,7]))
# except ValueError as e:
#     print('\n PERFECT! ValueError raised:', e, '\n')



