import numpy as np
from scipy import interpolate
from scipy.constants import hbar,pi, c, elementary_charge, epsilon_0, Boltzmann, m_e

# Spline interpolation for a data set (x,y) on new points xnew
def spline_interpolate(xnew,x,y):
    arr1inds = x.argsort()
    xs = x[arr1inds]
    ys = y[arr1inds]
    tck  = interpolate.splrep(map_to_zero_one(xs), ys, s=0)
    ynew = interpolate.splev(map_to_zero_one(xnew), tck, der=0)
    return ynew

def map_to_zero_one(x):
    return (x-np.amin(x)/np.amax(x))

def lambda_to_unit(l, unit = 'nm'):
    if unit == 'eV':
        return 2*pi*c*hbar/l/elementary_charge*1e9
    elif unit == 'cm-1':
        return 1e-2/l/1e-9
    else:
        return l