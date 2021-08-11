from os import close
from re import S
import pandas as pd
import numpy as np
import sys
from fractions import Fraction
import latex_converter
np.seterr(divide='ignore', invalid='ignore')

help = "File format:\n<x-prior-lenght>,<y-output-lenght>\n<prior-array>\n<x-by-y-channel-matrix>"

def main():
    # parsing argument
    args = sys.argv[1:]
    if len(args) != 1:
        print("hyper-distributor expects a file path as argument: `hyper-distributor <file-path>")
        print(help)
        return
    
    # opening file
    file_name = args[0]
    file = open(file_name,"r")

    #reading problem instance:
    #1-problem's size
    x,y = [int(x) for x in file.readline().split(',')] 
    print(f"|X| = {x}")
    print(f"|Y| = {y}")

    #2-problem's prior
    prior = [float(Fraction(x)) for x in file.readline().split(',')] 
    prior = np.array(prior, dtype=float)
    if sum(prior) != 1.0: #validating that the prior configures a probability distribution
        print("prior distribution should sum to 1")
        return
    print(f"Prior distribution:\n{prior}\n")
    prior.shape = (prior.size,1) #makes the prior a column vector instead of a simple array

    #3-problem's channel matrix
    cmatrix = np.ndarray(shape=(x,y),dtype=float) #allocating space according to declared size
    for i in range(x):
        cmatrix[i] = [float(Fraction(x)) for x in file.readline().split(',')] #line by line matrix is read and separated by commas, Fractions allows user to write probabilities in 'n/d' notation 
    partialdist = np.sum(a=cmatrix,axis=1)  #rows are added together resulting in an array with x elements
    print(f"Partial channel distributions:\n{partialdist}\n") #each of these elements represents the sum of a probability distribuition of outputs given an input
    for i in range(x): # validating that all rows configure probability distribuitions
        if abs(1.0 - partialdist[i]) > 0.0001: # treshold of 1/100%
            print(f"ERROR: every distribuition of y's for a given x shoud sum to 1, for x{i} it is:{partialdist[i]}\n")
            return
    print(f"Channel matrix:\n{cmatrix}\n")

    #calculate joint probability matrix
    joint = cmatrix*prior
    print(f"Joint matrix:\n{joint}\n")

    #from joint matrix calculate output probability distribution
    py = np.sum(joint,axis=0) #summing columns result in an array of y elements representing the probability of each output happening
    print(f"P[Y]:\n{py}\n")
    
    #cleaning problem by discarting outputs that have probability 0 and their respectives columns on the joint matrix
    if np.where(py == np.array([0.0]))[0].size > 0:
        print("Cleaning P[Y] and Joint matrix:\n")
        joint = np.delete(joint,np.where(py == np.array([0.0])),1)
        py = py[np.where(py != np.array([0.0]))]
        print(f"P[Y]:\n{py}\n")
        print(f"Joint matrix:\n{joint}\n")

    py.shape = (py.size,1) #makes the output distribuition a column vector instead of a simple array
    #calculate postrior distribution matrix
    posterior = joint/py.T
    print(f"Posterior distribuition(xi,Pxi|Y):\n{posterior}\n")

    #calculate hyper distribuiton matrix by discarting non unique colums and adding their respective probabilities together
    hyper, unique, inverse = np.unique(posterior,
                                 return_index=True,
                                 return_inverse=True,
                                 axis=1)
    pyn = np.ndarray(shape=(unique.size,1))
    for i in unique:
        if i < unique.size: #this eliminates problems related to corner cases of the unique method from numpy library
            pyn[i] = sum(py[np.where(inverse == i)])
    pyn.shape = (pyn.size) #makes pyn from colum vector to simple array for improved readability
    print(f"PHyper[Y]:\n{pyn}\n")
    print(f"Hyper distribuition(xi,PX|yi):\n{hyper}\n")

if __name__ == "__main__":
    main()