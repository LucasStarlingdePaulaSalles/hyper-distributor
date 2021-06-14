from os import close
from re import S
import pandas as pd
import numpy as np
import sys
from fractions import Fraction
np.seterr(divide='ignore', invalid='ignore')

help = "File format:\n<x-prior-lenght>,<y-output-lenght>\n<prior-array>\n<x-by-y-channel-matrix>"

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print("hyper-distributor expects a file path as argument: `hyper-distributor <file-path>")
        print(help)
        return
    file_name = args[0]
    file = open(file_name,"r")
    x,y = [int(x) for x in file.readline().split(',')]
    prior = [float(Fraction(x)) for x in file.readline().split(',')]
    prior = np.array(prior, dtype=float)
    prior.shape = (prior.size,1)
    print(f"|X| = {x}")
    print(f"|Y| = {y}")
    if sum(prior) != 1.0:
        print("prior distribution should sum to 1")
        return
    print(f"Prior distribution:\n{prior}\n")
    cmatrix = np.ndarray(shape=(x,y),dtype=float)
    for i in range(x):
        cmatrix[i] = [float(Fraction(x)) for x in file.readline().split(',')] 
    partialdist = np.sum(a=cmatrix,axis=1)
    print(f"Partial channel distributions:\n{partialdist}\n")
    for i in range(x):
        if 1.0 - partialdist[i] > 0.0001: # treshold a 1/100%
            print(f"ERROR: every distribuition of y's for a given x shoud sum to 1, for x{i} it is:{partialdist[i]}\n")
            return
    print(f"Channel matrix:\n{cmatrix}\n")
    joint = cmatrix*prior
    print(f"Joint matrix:\n{joint}\n")
    py = np.sum(joint,axis=0)
    joint = np.delete(joint,np.where(py == np.array([0.0])),1)
    py = py[np.where(py != np.array([0.0]))]
    py.shape = (py.size,1)
    print(f"Py:\n{py}\n")
    posterior = joint.T/py
    posterior = posterior.T
    print(f"Posterior distribuition(xi,PX|yi):\n{posterior}\n")
    hyper, unique, inverse = np.unique(posterior,
                                 return_index=True,
                                 return_inverse=True,
                                 axis=1)
    pyn = np.ndarray(shape=(unique.size,1))
    for i in unique:
        if i < unique.size:
            pyn[i] = sum(py[np.where(inverse == i)])
    print(f"P[X|Y]:\n{pyn}\n")
    print(f"Hyper distribuition(xi,PX|yi):\n{hyper}\n")

main()