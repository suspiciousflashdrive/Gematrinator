from tkinter import *
import tkinter as tk
from tkinter import filedialog, simpledialog
from cryptography.fernet import Fernet
import base64, hashlib

root = tk.Tk()
root.geometry("300x400")
root.title("Encrypted Notepad")

buttonFrame = tk.Frame(root)
buttonFrame.pack(fill='both', expand=True)

textbox = Text(root, font=("Courier", 12), wrap='word', bg="#eebb32")
textbox.pack(fill='both', expand=True, padx=6, pady=6)

def decryptFile():
    password = simpledialog.askstring("Password", "Enter your password:", show="*")
    filePath = filedialog.askopenfilename(initialdir='/home/goy/Documents/vscode',title='Select a text file', filetypes = [('text files', '.txt')])
    file = open(filePath, "rb")
    content = file.read()
    password_bytes = password.encode()
    key = hashlib.sha256(password_bytes).digest()
    key_64 = base64.urlsafe_b64encode(key)
    decrypted = Fernet(key_64).decrypt(content.decode())
    file.close()
    textbox.delete("0.0", END)
    textbox.insert(INSERT, decrypted)
    if filePath is None:
        return

def encryptFile():
    password = simpledialog.askstring("Password", "Enter your password:", show="*")
    file = filedialog.asksaveasfile(mode='wb', defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file is None:
        return
    filetext = textbox.get("1.0", END)
    password_bytes = password.encode()
    key = hashlib.sha256(password_bytes).digest()
    key_64 = base64.urlsafe_b64encode(key)
    encrypted = Fernet(key_64).encrypt(filetext.encode())
    file.write(encrypted)
    file.close()



def clear():
    textbox.delete(0.0, END)

openButton = tk.Button(buttonFrame, text="Open", font=("Courier", 12), command=decryptFile)
saveButton = tk.Button(buttonFrame, text="Save", font=("Courier", 12), command=encryptFile)
clearButton = tk.Button(buttonFrame, text="Clear", font=("Courier", 12), command=clear)
exitButton = tk.Button(buttonFrame, text="Exit", font=("Courier", 12), command=root.quit)

openButton.pack(side='left', padx=4)
saveButton.pack(side='left', padx=4)
clearButton.pack(side='left', padx=4)
exitButton.pack(side='right', padx=4)
root.mainloop()
