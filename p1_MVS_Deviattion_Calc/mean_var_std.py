# np_mean_var_std.py v2

import numpy as np


def calculate(lst):
    if len(lst) != 9:
        raise ValueError('List must contain nine numbers.')

    a = np.reshape(lst, (3, 3))

    calculations = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    # Adding calculated values (mean-var-stf) along axes to dic
    for ax in (0, 1):
        calculations['mean'].append(list(a.mean(axis=ax)))
        calculations['variance'].append(list(a.var(axis=ax)))
        calculations['standard deviation'].append(list(a.std(axis=ax)))
        calculations['max'].append(list(a.max(axis=ax)))
        calculations['min'].append(list(a.min(axis=ax)))
        calculations['sum'].append(list(a.sum(axis=ax)))

    # Adding calculated flattened values (mean-var-stf) to dic
    calculations['mean'].append(a.mean())
    calculations['variance'].append(a.var())
    calculations['standard deviation'].append(a.std())
    calculations['max'].append(a.max())
    calculations['min'].append(a.min())
    calculations['sum'].append(a.sum())

    return calculations

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))


