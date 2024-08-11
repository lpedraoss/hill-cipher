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
        self.especial = False  # Añadir atributo especial

    def set_alphabet(self, alphabet=None, especial=False, numbers=False):
        self.especial = especial  # Asignar valor de especial al atributo de la clase
        alphabet_es = 'abcdefghijklmnñopqrstuvwxyz'
        alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
        especial_en = "!@#$%^&*()-_+={}[]:;'\"<>,./\\|?~` "
        especial_es = "¡¿!?@#$%&*()-_+={}[]:;'\"<>,./\\|^~` "
        alphanum = '0123456789'
        if alphabet == 'en':
            self.alphabet = alphabet_en
            if especial:
                self.alphabet += especial_en
            if numbers:
                self.alphabet += alphanum
        elif alphabet == 'es':
            self.alphabet = alphabet_es
            if especial:
                self.alphabet += especial_es
            if numbers:
                self.alphabet += alphanum
        else:
            self.alphabet = alphabet_es
            
        self.alphabet = {char: i for i, char in enumerate(self.alphabet)}
        self.modulus = len(self.alphabet)

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def generate_key_matrix(self, n, m):
        while True:
            key_matrix = np.random.randint(0, m, size=(n, n))
            det = int(np.round(np.linalg.det(key_matrix))) % m
            if det != 0 and self.gcd(det, m) == 1:
                return key_matrix

    def encrypt(self, text_plain, n, key_matrix=None):
        self.text_plain = text_plain
        self.n = n
        self.modulus = len(self.alphabet)
        
        if not self.especial:
            self.text_plain = self.text_plain.replace(' ', 'x')
        
        self.text_blocks = [self.text_plain[i:i + n] for i in range(0, len(self.text_plain), n)]
        if len(self.text_blocks[-1]) < n:
            self.text_blocks[-1] += 'x' * (n - len(self.text_blocks[-1]))
        
        if key_matrix is None:
            self.key_matrix = self.generate_key_matrix(n, self.modulus)
        else:
            self.key_matrix = key_matrix
        
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
        det = int(round(np.linalg.det(matrix)))
        det_inv = pow(det, -1, modulus)
        adjugate_matrix = np.mod(np.round(np.linalg.inv(matrix) * det), modulus)
        inverse_matrix = np.mod(det_inv * adjugate_matrix, modulus)
        return inverse_matrix

    def decrypt(self, cipher_txt=None, key=None, n=None):
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