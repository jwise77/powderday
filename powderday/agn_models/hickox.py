from __future__ import print_function
import numpy as np
'''
    Vary the instantaneous BH luminosity by sampling the probability distribution from Hickox et al (2014) for short and long-scale time variations.
    - Ray Sharma
'''
def Hickox2014(L_cut=100, alpha=0.2):
    L = np.logspace(-5, 3, 100)
    p0 = pow(L / L_cut, -alpha) * np.exp(-L / L_cut)
    t0 = 0.00854
    return t0 * p0, L

def vary_bhluminosity(L_avg):
    PDF, L_frac = Hickox2014()
    CDF = np.cumsum(PDF) / sum(PDF)
    choice = np.random.random()
    return L_avg * L_frac[np.argmin(abs(CDF - choice))]
