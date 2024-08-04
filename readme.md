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

