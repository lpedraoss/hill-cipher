import numpy as np
from core.hill_cipher import HillCipher


hill = HillCipher()
def load_key(filename):
    return np.loadtxt(filename, dtype=int)
def load_cipher(filename):
    with open(filename, 'r') as file:
        return file.read()
def set_alphabet(alphabet = None, character = None):
    especial = False
    if character == 'y':
        especial = True
    hill.set_alphabet(alphabet=alphabet,especial=especial)
    print('alfabeto establecido con exito...')

def cipher_CLI():
    language = input('ingresa el idioma (en/es): ')
    language_especial = input('contiene caracteres especiales? (y/n): ')
    set_alphabet(language, language_especial)
    option_text = input('deseas cargar el texto plano desde un archivo? (y/n): ')
    if option_text == 'y':
        text_plain = load_cipher('data/plain.txt')
        print('texto plano cargado con exito')
        print('texto plano> {}'.format(text_plain))
    else:
        text_plain = input('ingresa el texto plano: ')
        print('texto plano> {}'.format(text_plain))
    character = input('ingresa la cantidad de caracteres por bloque: ')
    hill.encrypt(text_plain=text_plain,n = int(character))
    print('texto cifrado> {}'.format(hill.cipher_txt))
    
def decrypt_CLI():
    
    language = input('ingresa el idioma (en/es): ')
    language_especial = input('contiene caracteres especiales? (y/n): ')
    set_alphabet(language, language_especial)
    
    key = load_key('data/key.txt')
    print('matriz clave cargada con exito')
    option_cipher = input('deseas cargar el texto cifrado desde un archivo? (y/n): ')
    if option_cipher == 'y':
        cipher_txt = load_cipher('data/cipher.txt')
        print('texto cifrado cargado con exito')
        print('texto cifrado> {}'.format(cipher_txt))
    else:
        cipher_txt = input('ingresa el texto cifrado: ')
        print('texto cifrado> {}'.format(cipher_txt))
        
    character = input('ingresa la cantidad de caracteres por bloque: ')
    hill.decrypt(cipher_txt = cipher_txt, key=key, n=int(character))
    print('texto descifrado> {}'.format(hill.decrypted_txt))    
    
def hill_CLI():
    print('Hill Cipher CLI')
    print('1. Cifrar')
    print('2. Descifrar')
    option = input('ingresa una opcion> ')
    if option == '1':
        cipher_CLI()
    elif option == '2':
        decrypt_CLI()