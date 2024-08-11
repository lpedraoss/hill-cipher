import numpy as np

def mod_inverse(a, m):
    # Función para encontrar el inverso modular de a bajo m
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1

def matrix_mod_inverse(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = mod_inverse(det, mod)
    
    matrix_mod_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % mod
    return matrix_mod_inv

# Matriz de ejemplo
matrix = np.array([
    [17, 13, 19],
    [20, 24, 18],
    [0, 4, 21]
])

# Vector proporcionado
vector = np.array([[10], [23], [21]])

mod = 27
inverse_matrix = matrix_mod_inverse(matrix, mod)

# Multiplicar la matriz inversa por el vector
result_vector = np.dot(inverse_matrix, vector) % mod
print(result_vector)