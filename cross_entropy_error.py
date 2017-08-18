import gradient_descent

gradient_descent.function_2("float")



import numpy as np

def cross_entropy_error(y,t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

t = [0,0,1]
y = [0.1,0.05,0.6]

print(cross_entropy_error(np.array(y),np.array(t)))

