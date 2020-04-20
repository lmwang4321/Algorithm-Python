import numpy as np 

im1 = np.random.randn(500,600)
im2 = np.random.randn(500,600)

def score_func(im1, im2):
	return np.sum((im1 - im2) ** 2)

print(score_func(im1, im2))