from random import randint
from scipy.stats import norm
import numpy as np

#initializes a seed for the brownian function
def seeds(size=512):
    seeds = []
    seeds.append((randint(0,size),randint(0,size)))
    return seeds[0]


#function that takes an input position, position step size, and time step size and outputs a position
def brownian(seed=(256,256) ,delt =1.5,deetee=0.05): 
    x0 = np.asarray(seed)
    delta = float(delt)
    dt = float(deetee)
    x0 = x0 + (norm.rvs(scale=delta**2*dt),norm.rvs(scale=delta**2*dt))
    return tuple(x0)