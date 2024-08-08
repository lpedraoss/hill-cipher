import numpy as np
from core.hill_cipher import HillCipher

hill = HillCipher()

def load_key(filename):
    return np.loadtxt(filename, dtype=int)

def load_txt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    ascii_content = content.encode('latin1', 'replace').decode('latin1')
    return ascii_content
def load_cipher(filename):
    with open(filename, 'r', encoding='latin1') as file:
        content = file.read()
    return content

def set_alphabet(alphabet=None, character=None, numbers=False):
    especial = False
    if character == 'y':
        especial = True
    hill.set_alphabet(alphabet=alphabet, especial=especial, numbers=numbers)
    print('alfabeto establecido con exito...')

def cipher_CLI():
    try:
        language = input('ingresa el idioma (en/es): ').strip().lower()
        alphanumeric = input('deseas incluir numeros? (y/n): ').strip().lower() == 'y'
        language_especial = input('contiene caracteres especiales? (y/n): ').strip().lower()
        set_alphabet(language, language_especial, alphanumeric)
        option_text = input('deseas cargar el texto plano desde un archivo? (y/n): ').strip().lower()
        if option_text == 'y':
            text_plain = load_txt('data/plain.txt').strip().lower()
            print('texto plano cargado con exito')
            print('texto plano> {}'.format(text_plain))
        else:
            text_plain = input('ingresa el texto plano: ').strip().lower()
            print('texto plano> {}'.format(text_plain))
        character = input('ingresa la cantidad de caracteres por bloque: ')
        hill.encrypt(text_plain=text_plain, n=int(character))
        print('texto cifrado> {}'.format(hill.cipher_txt))
    except Exception as e:
        print(f'Error al cifrar: {e}')

def decrypt_CLI():
    try:
        language = input('ingresa el idioma (en/es): ').strip().lower()
        alphanumeric = input('deseas incluir numeros? (y/n): ').strip().lower() == 'y'
        language_especial = input('contiene caracteres especiales? (y/n): ').strip().lower()
        set_alphabet(language, language_especial, alphanumeric)
        key = load_key('data/key.txt')
        print('matriz clave cargada con exito')
        option_cipher = input('deseas cargar el texto cifrado desde un archivo? (y/n): ').strip().lower()
        if option_cipher == 'y':
            cipher_txt = load_cipher('data/cipher.txt')
            print('texto cifrado cargado con exito')
            print('texto cifrado> {}'.format(cipher_txt))
        else:
            cipher_txt = input('ingresa el texto cifrado: ')
            print('texto cifrado> {}'.format(cipher_txt))
            
        character = input('ingresa la cantidad de caracteres por bloque: ')
        hill.decrypt(cipher_txt=cipher_txt, key=key, n=int(character))
        print('texto descifrado> {}'.format(hill.decrypted_txt))
    except Exception as e:
        print(f'Error al descifrar: {e}')

def hill_CLI():
    print('Hill Cipher CLI')
    print('1. Cifrar')
    print('2. Descifrar')
    option = input('ingresa una opcion> ')
    if option == '1':
        cipher_CLI()
    elif option == '2':
        decrypt_CLI()