import numpy as np

def round_mantissa(x, n):
    m = np.round(np.log2(x)) - n
    return np.round(2**-m * x) * 2**m
