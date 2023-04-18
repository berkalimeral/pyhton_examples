import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import base64

window = tk.Tk()
window.title('Secret Notes')
window.minsize(width=350,height=600)
window.config(padx=20,pady=20)

FONT = ('Arial', 13, 'italic')

image = Image.open("top_secret_img_o.jpg")
image.resize((1,1))

img = ImageTk.PhotoImage(image)

image_label = tk.Label(image=img)
image_label.image = img
image_label.pack()

title_label = tk.Label(text='Enter your title',font=FONT)
title_label.pack()

title_entry = tk.Entry(width=40)
title_entry.pack()

secret_label = tk.Label(text='Enter your secret',font= FONT)
secret_label.pack()

secret_text = tk.Text(width= 35,height=20)
secret_text.pack()

master_key_label = tk.Label(text='Enter master key', font= FONT)
master_key_label.pack()

master_key_entry = tk.Entry(width= 40)
master_key_entry.pack()

def save_button():
    if secret_text.get('1.0', tk.END) == "" or master_key_entry.get() == "":
        messagebox.showwarning("showwarning", "Please make sure of encrypted info")
    else:
        title = title_entry.get()
        my_secret_txt = secret_text.get('1.0', tk.END)
        my_master_key = master_key_entry.get()

        my_secret_file = open('mysecret.txt', 'w')
        my_secret_file.write(title + "\n")

        encrypted_text = encode(my_master_key,my_secret_txt)
        my_secret_file.write(encrypted_text + "\n")
        print(encrypted_text)


def encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

save_encrypt_btn = tk.Button(text='Save & Encrypt', command= save_button)
save_encrypt_btn.pack()

def decrypt_button():
    if secret_text.get('1.0', tk.END) == "" or master_key_entry.get() == "":
        messagebox.showwarning("showwarning", "Please make sure of decrypted info")
    else:
        my_secret_txt = secret_text.get('1.0', tk.END)
        my_master_key = master_key_entry.get()

        decrypted_text = decode(my_master_key, my_secret_txt)
        print(decrypted_text)

        secret_text.delete(1.0, tk.END)
        secret_text.insert(tk.END,decrypted_text)

def decode(key,message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))

    return "".join(dec)


decrypt_btn = tk.Button(text='Decrypt', command= decrypt_button)
decrypt_btn.pack()



window.mainloop()