import numpy as np

class HillCipher():
    def __init__(self):
        self.text_plain = None
        self.cipher_txt = None
        self.decrypted_txt = None
        self.n = None
        self.modulus = None
        self.key_matrix = None
        self.key_matrix_inver = None
        self.text_blocks = None
        self.p = None
        self.c = None
        self.p_decipher = None
        self.alphabet = None

    def set_alphabet(self, alphabet=None, especial=False):
        """
        Sets the alphabet for the Hill Cipher encryption.
        Parameters:
        - alphabet (str): The alphabet to be used. Valid options are 'en' for English alphabet and 'es' for Spanish alphabet. If not provided, the default is the Spanish alphabet.
        - especial (bool): Whether to include special characters and numbers in the alphabet. Default is False.
        Returns:
        None
        """
        alphabet_en = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        alphabet_es = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'ñ': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
        especial_en = {
            "!": 26, "@": 27, "#": 28, "$": 29, "%": 30, "^": 31, "&": 32, "*": 33,
            "(": 34, ")": 35, "-": 36, "_": 37, "+": 38, "=": 39, "{": 40, "}": 41,
            "[": 42, "]": 43, ":": 44, ";": 45, "'": 46, "\"": 47, "<": 48, ">": 49,
            ",": 50, ".": 51, "/": 52, "\\": 53, "|": 54, "?": 55, "~": 56, "`": 57,
            " ": 58
        }

        especial_es = {
            "¡": 27, "¿": 28, "!": 29, "?": 30, "@": 31, "#": 32, "$": 33, "%": 34, "&": 35,
            "*": 36, "(": 37, ")": 38, "-": 39, "_": 40, "+": 41, "=": 42, "{": 43,
            "}": 44, "[": 45, "]": 46, ":": 47, ";": 48, "'": 49, "\"": 50, "<": 51,
            ">": 52, ",": 53, ".": 54, "/": 55, "\\": 56, "|": 57, "^": 58, "~": 59,
            "`": 60, " ": 61
        }
        numbers_en = {
            '0': 59, '1': 60, '2': 61, '3': 62, '4': 63, '5': 64, '6': 65, '7': 66, '8': 67, '9': 68
        }
        numbers_es = {
            '0': 62, '1': 63, '2': 64, '3': 65, '4': 66, '5': 67, '6': 68, '7': 69, '8': 70, '9': 71
        }
        if alphabet == 'en':
            self.alphabet = alphabet_en
            if especial:
                self.alphabet.update(especial_en)
                self.alphabet.update(numbers_en)
        elif alphabet == 'es':
            self.alphabet = alphabet_es
            if especial:
                self.alphabet.update(especial_es)
                self.alphabet.update(numbers_es)
        else:
            self.alphabet = alphabet_es
            if especial:
                self.alphabet.update(especial_es)
                self.alphabet.update(numbers_es)
        self.modulus = len(self.alphabet)

    def gcd(self, a, b):
        """
        Calculates the greatest common divisor (GCD) of two numbers.

        Parameters:
        a (int): The first number.
        b (int): The second number.

        Returns:
        int: The GCD of the two numbers.
        """
        while b:
            a, b = b, a % b
        return a

    def generate_key_matrix(self, n, m):
        """
        Generates a key matrix for the Hill Cipher encryption algorithm.

        Parameters:
        - n (int): The size of the key matrix (n x n).
        - m (int): The modulus value for the key matrix elements.

        Returns:
        - key_matrix (numpy.ndarray): The generated key matrix.

        Notes:
        - The key matrix is generated randomly using integers between 0 and m-1.
        - The determinant of the key matrix must be non-zero and coprime with m.
        """
        while True:
            key_matrix = np.random.randint(0, m, size=(n, n))
            det = int(np.round(np.linalg.det(key_matrix))) % m
            if det != 0 and self.gcd(det, m) == 1:
                return key_matrix

    def encrypt(self, text_plain, n):
        """
        Encrypts the given plain text using the Hill Cipher algorithm.
        Parameters:
            text_plain (str): The plain text to be encrypted.
            n (int): The size of the square key matrix.
        Returns:
            str: The encrypted cipher text.
        Raises:
            None
        """
        self.text_plain = text_plain
        self.n = n
        self.modulus = len(self.alphabet)
        self.text_blocks = [text_plain[i:i + n] for i in range(0, len(text_plain), n)]
        if len(self.text_blocks[-1]) < n:
            self.text_blocks[-1] += 'x' * (n - len(self.text_blocks[-1]))
        self.key_matrix = self.generate_key_matrix(n, self.modulus)
        self.p = [np.array([self.alphabet[char] for char in block]) for block in self.text_blocks]
        self.c = [(np.dot(self.key_matrix, block) % self.modulus).astype(int) for block in self.p]
        self.cipher_txt = ''.join([''.join([list(self.alphabet.keys())[list(self.alphabet.values()).index(num)] for num in block]) for block in self.c])

        with open("data/cipher.txt", "w") as file:
            file.write(self.cipher_txt)

        with open("data/key.txt", "w") as file:
            for row in self.key_matrix:
                file.write(' '.join(str(num) for num in row) + '\n')

        return self.cipher_txt

    def matrix_inverse(self, matrix, modulus):
        """
        Calculates the inverse of a matrix modulo a given modulus.

        Parameters:
        - matrix (numpy.ndarray): The matrix to calculate the inverse of.
        - modulus (int): The modulus to perform the calculations.

        Returns:
        - inverse_matrix (numpy.ndarray): The inverse matrix modulo the given modulus.
        """
        det = int(round(np.linalg.det(matrix)))
        det_inv = pow(det, -1, modulus)
        adjugate_matrix = np.mod(np.round(np.linalg.inv(matrix) * det), modulus)
        inverse_matrix = np.mod(det_inv * adjugate_matrix, modulus)
        return inverse_matrix

    def decrypt(self, cipher_txt=None, key=None, n=None):
        """
        Decrypts the given cipher text using the Hill Cipher algorithm.
        Args:
            cipher_txt (str): The cipher text to be decrypted.
            key (ndarray): The key matrix used for decryption. If not provided, the previously set key matrix will be used.
            n (int): The block size used for encryption. If not provided, the previously set block size will be used.
        Returns:
            str: The decrypted text.
        Raises:
            None
        """
        if key is not None:
            self.key_matrix = key
        if n is not None:
            self.n = n
        self.cipher_txt = cipher_txt
        self.text_blocks = [self.cipher_txt[i:i + self.n] for i in range(0, len(self.cipher_txt), self.n)]
        self.c = [np.array([self.alphabet[char] for char in block]) for block in self.text_blocks]

        self.p_decipher = [(np.dot(self.matrix_inverse(self.key_matrix, self.modulus), block) % self.modulus).astype(int) for block in self.c]
        self.decrypted_txt = ''.join([''.join([list(self.alphabet.keys())[list(self.alphabet.values()).index(num)] for num in block]) for block in self.p_decipher])

        with open("data/decipher.txt", "w") as file:
            file.write(self.decrypted_txt)

        return self.decrypted_txt
