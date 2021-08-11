import numpy as np

def to_latex(title: str, label: str, matrix: np.ndarray, type: str = "channel",Y=[]):
    print(f"## {title}")
    print("$$") # Init math block on typora
    print("\\begin{array}{|c|",end="")

    for _ in range(matrix.shape[1]):
        print("c",end="")
        if type == "hyper" or type == "posterior":
            print("|",end="")
    if type != "hyper" and type != "posterior":
        print("|",end="")

    print("}")
    print("\\hline")

    if type == "hyper":
        print("[\\pi \\vartriangleright \\mathsf{%s}] & " % label, end="")
    elif type == "posterior":
        print("\\ & ", end="")
    else:
        print("\\mathsf{%s} & " % label, end="")

    if Y == []:
        if type != "hyper" and type != "posterior":
            Y = [f"y_{y}" for y in range(1, matrix.shape[1]+1)]
        else:
            Y = ["P[ \\mathcal{X} | y_{%s}]" % y for y in range(1, matrix.shape[1]+1)]
    else:
        Y = np.around(Y, 3)

    jc = 0
    for j in Y:
        print(f"{j} ",end="")
        if jc != matrix.shape[1]-1:
            print("& ", end="")
        jc += 1

    print("\\\\ \\hline")

    for i in range(matrix.shape[0]):
        print(f"x_{i+1} & ", end="")
        for j in range(matrix.shape[1]):
            print(f"{np.around(matrix[i,j],4)} ",end="")
            if j != matrix.shape[1]-1:
                print("& ",end="")
        print("\\\\")
    print("\\hline")
    print("\\end{array}")
    print("$$")
    print()

def latex_header(x: int, y: int):
    print("# Quantitative Information Flow Hyper Distribution Calculator")
    print("$$")
    print("|\\mathcal{X}| = %s" % x)
    print("$$")
    print("$$")
    print("|\\mathcal{Y}| = %s" % y)
    print("$$")
    print()

def latex_array(arr: np.ndarray, label: str):
    arr = np.around(arr,5)
    print("$$")
    print("%s = \\{" % label, end="")
    valc = 1
    for val in arr:
        print(f"{val}", end="")
        if valc < arr.size:
            print(", ", end="")
    print("\\}")
    print("$$")
    print()
