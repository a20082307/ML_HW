import numpy as np

test = np.array([i for i in range(10)])
print(test)

n = 10
idx = np.random.permutation(n)
print(idx)
print(test[idx])