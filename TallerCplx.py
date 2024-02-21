import numpy as np

# Adición de vectores complejos
vec1 = np.array([complex(input("Ingrese la parte real del vector 1: "), input("Ingrese la parte imaginaria del vector 1: "))])
vec2 = np.array([complex(input("Ingrese la parte real del vector 2: "), input("Ingrese la parte imaginaria del vector 2: "))])
resultado = np.add(vec1, vec2)
print("Suma de vectores complejos:", resultado)

# Inverso (aditivo) de un vector complejo
vec = np.array([complex(input("Ingrese la parte real del vector: "), input("Ingrese la parte imaginaria del vector: "))])
resultado_inverso = np.negative(vec)
print("Inverso del vector complejo:", resultado_inverso)

# Multiplicación de un escalar por un vector complejo
escalar = complex(input("Ingrese el escalar (parte real): "), input("Ingrese el escalar (parte imaginaria): "))
resultado_multiplicacion = np.multiply(escalar, vec)
print("Producto del escalar y el vector complejo:", resultado_multiplicacion)

# Adición de matrices complejas
mat1 = np.array([[complex(input("Ingrese la parte real de la matriz 1, fila 1: "), input("Ingrese la parte imaginaria de la matriz 1, fila 1: "))],
                  [complex(input("Ingrese la parte real de la matriz 1, fila 2: "), input("Ingrese la parte imaginaria de la matriz 1, fila 2: "))]])
mat2 = np.array([[complex(input("Ingrese la parte real de la matriz 2, fila 1: "), input("Ingrese la parte imaginaria de la matriz 2, fila 1: "))],
                  [complex(input("Ingrese la parte real de la matriz 2, fila 2: "), input("Ingrese la parte imaginaria de la matriz 2, fila 2: "))]])
resultado_suma_matrices = np.add(mat1, mat2)
print("Suma de matrices complejas:", resultado_suma_matrices)

# Inversa (aditiva) de una matriz compleja
mat = np.array([[complex(input("Ingrese la parte real de la matriz, fila 1: "), input("Ingrese la parte imaginaria de la matriz, fila 1: "))],
                [complex(input("Ingrese la parte real de la matriz, fila 2: "), input("Ingrese la parte imaginaria de la matriz, fila 2: "))]])
resultado_inverso_matriz = np.negative(mat)
print("Inversa de la matriz compleja:", resultado_inverso_matriz)

# Multiplicación de un escalar por una matriz compleja
escalar_matriz = complex(input("Ingrese el escalar para la matriz (parte real): "), input("Ingrese el escalar para la matriz (parte imaginaria): "))
resultado_multiplicacion_matriz = np.multiply(escalar_matriz, mat)
print("Producto del escalar y la matriz compleja:", resultado_multiplicacion_matriz)

# Transpuesta de una matriz/vector
mat = np.array([[complex(input("Ingrese la parte real de la matriz, fila 1: "), input("Ingrese la parte imaginaria de la matriz, fila 1: "))],
                [complex(input("Ingrese la parte real de la matriz, fila 2: "), input("Ingrese la parte imaginaria de la matriz, fila 2: "))]])
resultado_transpuesta = np.transpose(mat)
print("Transpuesta de la matriz/vector:", resultado_transpuesta)

# Conjugada de una matriz/vector
resultado_conjugado = np.conj(mat)
print("Conjugada de la matriz/vector:", resultado_conjugado)

# Adjunta (daga) de una matriz/vector
resultado_adyacente = np.conj(np.transpose(mat))
print("Adjunta de la matriz/vector:", resultado_adyacente)

# Producto de dos matrices (de tamaños compatibles)
def producto_matrices():
    matriz1 = np.array([complex(input("Ingrese la parte real e imaginaria de la primera matriz, separadas por espacio: ")) for _ in range(int(input("Ingrese el número de filas de la primera matriz: ")))])
    matriz2 = np.array([complex(input("Ingrese la parte real e imaginaria de la segunda matriz, separadas por espacio: ")) for _ in range(int(input("Ingrese el número de filas de la segunda matriz: ")))])
    return np.dot(matriz1, matriz2)

# Función para calcular la "acción" de una matriz sobre un vector
def accion_matriz_vector():
    matriz = np.array([complex(input("Ingrese la parte real e imaginaria de la matriz, separadas por espacio: ")) for _ in range(int(input("Ingrese el número de filas de la matriz: ")))])
    vector = np.array([complex(input("Ingrese la parte real e imaginaria del vector, separadas por espacio: "))])
    return np.dot(matriz, vector)

# Producto interno de dos vectores
def producto_interno():
    vector1 = np.array([complex(input("Ingrese la parte real e imaginaria del primer vector, separadas por espacio: "))])
    vector2 = np.array([complex(input("Ingrese la parte real e imaginaria del segundo vector, separadas por espacio: "))])
    return np.dot(vector1, vector2)

# Norma de un vector
def vector_norma():
    vector = np.array([complex(input("Ingrese la parte real e imaginaria del vector, separadas por espacio: "))])
    return np.linalg.norm(vector)

# Distancia entre dos vectores
def distancia_vectores():
    vector1 = np.array([complex(input("Ingrese la parte real e imaginaria del primer vector, separadas por espacio: "))])
    vector2 = np.array([complex(input("Ingrese la parte real e imaginaria del segundo vector, separadas por espacio: "))])
    return np.linalg.norm(vector1 - vector2)

# Valores y vectores propios de una matriz
def valores_vectores_propios():
    matriz = np.array([complex(input("Ingrese la parte real e imaginaria de la matriz, separadas por espacio: ")) for _ in range(int(input("Ingrese el tamaño de la matriz (número de filas): ")))])
    return np.linalg.eig(matriz)

# Revisar si una matriz es unitaria
def es_unitaria():
    matriz = np.array([complex(input("Ingrese la parte real e imaginaria de la matriz, separadas por espacio: ")) for _ in range(int(input("Ingrese el tamaño de la matriz (número de filas): ")))])
    return np.allclose(np.dot(matriz, matriz.T.conj()), np.eye(matriz.shape[0]))

# Revisar si una matriz es Hermitiana
def es_hermitiana():
    matriz = np.array([complex(input("Ingrese la parte real e imaginaria de la matriz, separadas por espacio: ")) for _ in range(int(input("Ingrese el tamaño de la matriz (número de filas): ")))])
    return np.allclose(matriz, matriz.T.conj())

# Producto tensor de dos matrices/vectores
def producto_tensor():
    matriz1 = np.array([complex(input("Ingrese la parte real e imaginaria de la primera matriz/vector, separadas por espacio: ")) for _ in range(int(input("Ingrese el tamaño de la primera matriz/vector (número de filas): ")))])
    matriz2 = np.array([complex(input("Ingrese la parte real e imaginaria de la segunda matriz/vector, separadas por espacio: ")) for _ in range(int(input("Ingrese el tamaño de la segunda matriz/vector (número de filas): ")))])
    return np.kron(matriz1, matriz2)