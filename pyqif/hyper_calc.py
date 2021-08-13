import numpy as np
import sys
from fractions import Fraction
from .latex_converter import *
np.seterr(divide='ignore', invalid='ignore')

help_flag = "pyqif flags:\n--help,-h\tprint this\n--verbose,-v\trun in verbose mode\n--latex,-l\toutput in latexformat\n"
help_file = "Execution from file redirection is highly recommended.\n\n pyqif < PATH/TO/FILE\n\n File format:\n<channel-label>\n<x-prior-lenght> <y-output-lenght>\n<prior-array>\n<x-by-y-channel-matrix>"
help = f"pyqif help:\n{help_flag}\n{help_file}"
verbose = False
latex = False
def set_verbose():
    global verbose
    verbose = True
def set_latex():
    global latex
    latex = True
def helper():
    print(help)

flags = {
    "--help": helper,
    "-h": helper,
    "--verbose": set_verbose,
    "-v": set_verbose,
    "--latex": set_latex,
    "-l": set_latex,
}

def print_header(x: int, y: int):
    if latex:
        latex_header(x,y)
    else:
        print(f"|X| = {x}")
        print(f"|Y| = {y}")
        
def print_prior(prior: np.ndarray):
    if latex:
        latex_array(prior,"\\pi")
    else:
        print(f"Prior distribution:\n{prior}\n")
    
def print_channel(cmatrix: np.ndarray, clabel: str):
    if latex:
        to_latex(f"Channel {clabel} matrix", clabel, cmatrix)
    else:
        print(f"Channel matrix:\n{cmatrix}\n")

def print_joint(jmatrix: np.ndarray):
    if latex:
        to_latex(f"Joint matrix", "J", jmatrix)
    else:
        print(f"Joint matrix:\n{jmatrix}\n")

def print_yprob(py: np.ndarray):
    if latex:
        latex_array(py,"p_\\mathsf{Y}")
    else:
        print(f"P[Y]:\n{py}\n")

def print_posterior(pmatrix: np.ndarray):
    if latex:
        to_latex(f"Posterior matrix", "", pmatrix, type="posterior")
    else:
        print(f"Posterior distribuition(xi,Pxi|Y):\n{pmatrix}\n")

def print_hyper(hmatrix: np.ndarray, pyn: np.ndarray, clabel: str):
    if latex:
        to_latex(f"Hyper Distribution", clabel, hmatrix, type="hyper", Y=pyn)
    else:
        print(f"PHyper[Y]:\n{pyn}\n")
        print(f"Hyper distribuition(xi,PX|yi):\n{hmatrix}\n")    

def hyper(clabel: str, x: int, y: int, prior: np.ndarray, cmatrix: np.ndarray):

    print_header(x,y)

    print_prior(prior)

    #makes the prior a column vector instead of a simple array
    prior.shape = (prior.size,1) 

    print_channel(cmatrix, clabel)


    #calculate joint probability matrix
    joint = cmatrix*prior
    print_joint(joint)

    #from joint matrix calculate output probability distribution
    py = np.sum(joint,axis=0) #summing columns result in an array of y elements representing the probability of each output happening
    print_yprob(py)
    
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
    print_posterior(posterior)

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
    print_hyper(hyper, pyn, clabel)
    return
    print(f"PHyper[Y]:\n{pyn}\n")
    print(f"Hyper distribuition(xi,PX|yi):\n{hyper}\n")
    # latex_converter.to_latex("hyper","H",hyper, type="hyper", Y=np.around(pyn,3) )


def main():
    # parsing argument
    args = sys.argv[1:]
    for arg in args:
        if arg not in flags:
            helper()
            return
        func = flags[arg]
        func()
        if arg == "-h" or arg == "--help":
            return

    if verbose: print("Channel label (ex: C):", end=" ")
    chan_label = input()

    if verbose: print("[space separated] Prior lenght, Output lenght (ex: 3 4):", end=" ")
    x,y =  [int(x) for x in input().split()]

    if verbose: print("[space separated] Prior distribution (ex: 1/3 1/3 1/3):", end=" ")
    prior = [float(Fraction(x)) for x in input().split()]
    
    # Prior verification
    if len(prior) != x:
        print(f"Prior distribution should have {x} terms, it has {len(prior)}")
        return

    prior = np.array(prior, dtype=float)
    if sum(prior) != 1.0: #validating that the prior configures a probability distribution
        print(f"Prior distribution must add up to 1, provided prior adds up to {sum(prior)}")
        return
    
    if verbose: 
        print("[space separated] Channel lines ex:")
        print("1/4 1/4 1/4 1/4")
        print("1/4 1/4 1/4 1/4")
        print("1/4 1/4 1/4 1/4")
        print()

    cmatrix = np.ndarray(shape=(x,y),dtype=float) #allocating space according to declared size
    for i in range(x):
        #line by line matrix is read and separated by commas, Fractions allows user to write probabilities in 'n/d' notation
        cmatrix[i] = [float(Fraction(x)) for x in input().split()]
    
    #rows are added together resulting in an array with x elements
    partialdist = np.sum(a=cmatrix,axis=1)  
    #each of these elements represents the sum of a probability distribuition of outputs given an input
    for i in range(x): 
        # validating that all rows configure probability distribuitions
        if abs(1.0 - partialdist[i]) > 0.0001: # treshold of 1/100%
            print(f"Every distribuition of y's for a given x shoud add up 1, for x{i} it adds up to: {partialdist[i]:.3f}\n")
            return
    
    hyper(chan_label,x,y,prior,cmatrix)

if __name__ == "__main__":
    main()