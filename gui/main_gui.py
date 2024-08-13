import tkinter as tk
from tkinter import messagebox
import numpy as np
from core.hill_cipher import HillCipher

hill = HillCipher()

def load_key(filename):
    return np.loadtxt(filename, dtype=int)

def load_txt(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        ascii_content = content.encode('latin1', 'replace').decode('latin1')
        return ascii_content
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar el archivo de texto: {e}")
        return None

def load_cipher(filename):
    try:
        with open(filename, 'r', encoding='latin1') as file:
            content = file.read()
        return content
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar el archivo cifrado: {e}")
        return None

def set_alphabet(alphabet=None, character=None, numbers=False):
    especial = False
    if character == 'y':
        especial = True
    hill.set_alphabet(alphabet=alphabet, especial=especial, numbers=numbers)

def execute_action():
    try:
        language = language_var.get()
        alphanumeric = numbers_var.get() == 1
        language_especial = special_chars_var.get()
        set_alphabet(language, language_especial, alphanumeric)
        
        use_default_key = default_key_var.get() == 1
        
        if load_file_var.get() == 1:
            if action_var.get() == "cipher":
                text_plain = load_txt('data/plain.txt')
                if text_plain is None:
                    return
                text_plain = text_plain.strip().lower()
                hill.encrypt(text_plain=text_plain, n=int(block_size_entry.get()), key=use_default_key)
                result = hill.cipher_txt
            else:
                cipher_txt = load_cipher('data/cipher.txt')
                if cipher_txt is None:
                    return
                hill.decrypt(cipher_txt=cipher_txt, n=int(block_size_entry.get()), key=use_default_key)
                result = hill.decrypted_txt
        else:
            if action_var.get() == "cipher":
                text_plain = text_entry.get().strip().lower()
                hill.encrypt(text_plain=text_plain, n=int(block_size_entry.get()), key=use_default_key)
                result = hill.cipher_txt
            else:
                cipher_txt = text_entry.get().strip().lower()
                hill.decrypt(cipher_txt=cipher_txt, n=int(block_size_entry.get()), key=use_default_key)
                result = hill.decrypted_txt
        
        messagebox.showinfo("Resultado", result)
    except Exception as e:
        messagebox.showerror("Error", f"Error al ejecutar la acción: {e}")

def toggle_text_entry():
    if load_file_var.get() == 1:
        text_entry.config(state=tk.DISABLED)
    else:
        text_entry.config(state=tk.NORMAL)

def mainGui():
    global language_var, numbers_var, special_chars_var, action_var, load_file_var, text_entry, block_size_entry, default_key_var

    root = tk.Tk()
    root.title("Hill Cipher GUI")

    language_var = tk.StringVar(value="en")
    numbers_var = tk.IntVar()
    special_chars_var = tk.StringVar(value="n")
    action_var = tk.StringVar(value="cipher")
    load_file_var = tk.IntVar()
    default_key_var = tk.IntVar()

    tk.Label(root, text="Idioma (en/es):").pack()
    tk.Entry(root, textvariable=language_var).pack()

    tk.Label(root, text="Incluir números:").pack()
    tk.Checkbutton(root, variable=numbers_var).pack()

    tk.Label(root, text="Caracteres especiales (y/n):").pack()
    tk.Radiobutton(root, text="Sí", variable=special_chars_var, value="y").pack()
    tk.Radiobutton(root, text="No", variable=special_chars_var, value="n").pack()

    tk.Label(root, text="Acción:").pack()
    tk.Radiobutton(root, text="Cifrar", variable=action_var, value="cipher").pack()
    tk.Radiobutton(root, text="Descifrar", variable=action_var, value="decrypt").pack()

    tk.Checkbutton(root, text="Cargar texto desde archivo", variable=load_file_var, command=toggle_text_entry).pack()

    tk.Label(root, text="Texto:").pack()
    text_entry = tk.Entry(root)
    text_entry.pack()

    tk.Label(root, text="Cantidad de caracteres por bloque:").pack()
    block_size_entry = tk.Entry(root)
    block_size_entry.pack()

    tk.Checkbutton(root, text="Usar clave predeterminada", variable=default_key_var).pack()

    tk.Button(root, text="Ejecutar", command=execute_action).pack()

    root.mainloop()

if __name__ == "__main__":
    mainGui()