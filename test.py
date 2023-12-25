import numpy as np
print(5 + 6 + 8 + 7 + 9 + 8 + 10 + 11)
print(2 + 4 + 4 + 6 + 6 + 7 + 9 + 10)

a = np.array([
    [-3, -2, 0, -1, 1, 0, 2, 3],
    [-4, -2, -2, 0, 0, 1, 3, 4]
])
print(np.dot(a, a.T) / 8)

print(np.dot(np.array([0.59, 0.81]), np.array([-0.81, 0.59])))
print(float(9.34 / (9.34 + 0.41)))