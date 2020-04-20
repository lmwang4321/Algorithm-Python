import numpy as np

def FFT(X):
    X = np.asarray(X)
    N = X.shape[0]
    w = np.exp(-2j)
    return N

X = np.random.random(1024)
res = FFT(X)