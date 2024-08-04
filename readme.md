El cifrado Hill es un tipo de cifrado por bloques basado en álgebra lineal. Fue inventado por Lester S. Hill en 1929. Utiliza matrices y vectores para cifrar y descifrar mensajes. Aquí tienes una descripción general de cómo funciona:

### Cifrado Hill

1. **Clave**: Se elige una matriz cuadrada \( K \) de tamaño \( n \times n \) como clave. Esta matriz debe ser invertible en el módulo del tamaño del alfabeto (por ejemplo, 26 para el alfabeto inglés).

2. **Texto en claro**: El mensaje se divide en bloques de tamaño \( n \). Si el último bloque es más pequeño que \( n \), se puede rellenar con caracteres adicionales.

3. **Cifrado**:
   - Cada bloque de texto en claro se convierte en un vector de números usando un diccionario de letras a índices.
   - Se multiplica el vector por la matriz clave \( K \) y se toma el resultado módulo 26.
   - El vector resultante se convierte de nuevo en letras usando el diccionario de índices a letras.

4. **Descifrado**:
   - Se calcula la inversa de la matriz clave \( K \) en módulo 26.
   - Cada bloque cifrado se convierte en un vector de números.
   - Se multiplica el vector por la matriz inversa y se toma el resultado módulo 26.
   - El vector resultante se convierte de nuevo en letras.

### Ejemplo de Cifrado Hill en Python

Voy a mostrarte un ejemplo simple de cifrado y descifrado Hill en Python:

#### Pseudocódigo:
1. Definir la matriz clave y su inversa.
2. Crear funciones para convertir texto a vectores y viceversa.
3. Implementar las funciones de cifrado y descifrado.

#### Código:
```python
import numpy as np

# Diccionario de letras a índices para inglés
letras_en = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
    'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17,
    's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
}

# Diccionario inverso
indices_en = {v: k for k, v in letras_en.items()}

# Matriz clave (debe ser invertible en módulo 26)
K = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
K_inv = np.linalg.inv(K).astype(int) % 26

def text_to_vector(text, alphabet):
    return [alphabet[char] for char in text]

def vector_to_text(vector, alphabet):
    return ''.join([alphabet[num] for num in vector])

def encrypt(text, K, alphabet):
    vector = text_to_vector(text, alphabet)
    encrypted_vector = np.dot(K, vector) % 26
    return vector_to_text(encrypted_vector, indices_en)

def decrypt(cipher, K_inv, alphabet):
    vector = text_to_vector(cipher, alphabet)
    decrypted_vector = np.dot(K_inv, vector) % 26
    return vector_to_text(decrypted_vector, indices_en)

# Ejemplo de uso
texto = "act"
cifrado = encrypt(texto, K, letras_en)
descifrado = decrypt(cifrado, K_inv, letras_en)

print(f"Texto original: {texto}")
print(f"Texto cifrado: {cifrado}")
print(f"Texto descifrado: {descifrado}")
```

Este código muestra cómo cifrar y descifrar un mensaje usando el cifrado Hill con una matriz clave de 3x3. Asegúrate de que la matriz clave sea invertible en módulo 26 para que el descifrado funcione correctamente.