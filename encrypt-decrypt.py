

from tkinter import *
app=Tk()
app.geometry("350x200")
def machine():
    keys='abcdefghijklmnopqrstuvwxyz ! @'
    values=keys[-1]+keys[0:-2]

    encryptdictionaries=dict(zip(keys, values))
    decryptdictionaries=dict(zip(values, keys))
    message=entry_label.get()

    if var.get()==1:
        newMessage=''.join([encryptdictionaries[letter] for letter in message.lower()])
    elif var.get()==2:
        newMessage = ''.join([decryptdictionaries[letter] for letter in message.lower()])
    else:
        print("Please choose a choice")

    show_label.config(text=newMessage)

entry_label=Entry(app)
entry_label.grid(row=0, padx=10, pady=10)

var = IntVar()
R1 = Radiobutton(app, text="Encryption", variable=var, value=1)
R1.grid(row=1, column=0)

R2 = Radiobutton(app, text="Decryption", variable=var, value=2)
R2.grid(row=1, column=1)

button2 = Button(app, text="Show Encrypted/ Decrypted Data", command=machine)
button2.grid(row=2, padx=10, pady=10)

show_label=Label(app, text="Output")
show_label.grid(row=3, padx=10, pady=10)

app.mainloop()


