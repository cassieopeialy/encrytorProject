from tkinter import *
import tkinter as tk


#Window
window = tk.Tk()
window.geometry("500x700")
window.title("Caesar Cipher Algorithm")
bg_image = tk.PhotoImage(file = "Star.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

#Text Variables
pass_var = tk.StringVar()
encry_var = tk.StringVar()
decry_var = tk.StringVar()
result = tk.StringVar()

#Label for Password
pass_label1 = Label(window,
                    text = "Welcome! Please enter the",
                    font = ("Palatino Linotype", 24),
                    bg = "#fff9d9",
                    relief = RAISED,
                    bd = 10)
pass_label1.pack()

pass_label2 = Label(window,
                    text = "password before continuing:",
                    font=("Palatino Linotype", 24),
                    bg = "#fff9d9",
                    relief = RAISED,
                    bd = 10)
pass_label2.pack()

#Password Entry

pass_entry = Entry(window,
                   show = "*",
                   textvariable = pass_var)
pass_entry.pack()

#Program for Encryption
def encrypt():
    userMessage = encry_var.get()
    key = 6
    encryMessage = ""
    if pass_var.get() == "CompSciClub":
        for character in userMessage:
            if character.isalpha():
                if character == character.lower():
                    x = ord(character)-97
                    x += key
                    x = x % 26
                    encryMessage += chr(x + 97)
                else:
                    x = ord(character) - 65
                    x += key
                    x = x % 26
                    encryMessage += chr(x + 65)
            else:
                encryMessage += character
        result.set(encryMessage)
    else:
        result.set("Incorrect Password.")

#Program for Decryption
def decrypt():
    userMessage = decry_var.get()
    key = 6
    decryMessage = ""
    if pass_var.get() == "CompSciClub":
        for character in userMessage:
            if character.isalpha():
                if character == character.lower():
                    x = ord(character) - 97
                    x -= key
                    x = x % 26
                    decryMessage += chr(x + 97)
                else:
                    x = ord(character) - 65
                    x -= key
                    x = x % 26
                    decryMessage += chr(x + 65)
            else:
                decryMessage += character
        result.set(decryMessage)
    else:
        result.set("Incorrect Password.")



#Label for Encryption
start_label1 = Label(window,
                    text = "Enter your message here to encrypt it: ",
                    font = ("Palatino Linotype", 13),
                    bg = "#d9eeff",
                    relief = RAISED,
                    bd = 10)
start_label1.place(x = 0, y = 230)

#Entry for Encryption
encry_entry = Entry(window,
                    font=("Palatino Linotype", 10),
                    textvariable = encry_var)
encry_entry.place(x = 0, y = 280)

#Button for Encryption
encry_submit = Button(window,
                      text = "ENCRYPT",
                      font = ("Palatino Linotype", 10),
                      bg = "#d9eeff",
                      command = encrypt)
encry_submit.place(x = 148, y = 278)

#Label for Decryption
start_label2 = Label(window,
                    text = "Enter your ciphered text to decrypt it: ",
                    font = ("Palatino Linotype", 13),
                    bg = "#ead6ff",
                    relief = RAISED,
                    bd = 10)
start_label2.place(x = 0, y = 360)

#Entry for Decryption
decry_entry = Entry(window,
                    font=("Palatino Linotype", 10),
                    textvariable = decry_var)
decry_entry.place(x = 0, y = 409)


#Button for Decryption
decry_submit = Button(window,
                      text = "DECRYPT",
                      font = ("Palatino Linotype", 10),
                      bg = "#ead6ff",
                      command = decrypt)
decry_submit.place(x = 148, y = 407)

#Results

results_label = Label(window,
                       text = "RESULT",
                       font = ("Palatino Linotype", 20),
                       bg = "white",
                      relief = RAISED,
                      bd = 10)
results_label.place(x = 195, y = 470)

results_message = Entry(window,
                        font = ("Palatino Linotype", 10, "bold"),
                        textvariable = result)
results_message.place(x = 185, y = 530)
window.mainloop()

