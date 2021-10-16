# GUI for De/Encryptor
# Rob Ponder
# 15 October 2021

from functools import partial
import tkinter as tk
from DeEncryptor import *
import time

# GUI  operation functions


def check_entry(
    entry,
):  # TK gets angry when clearing blank entry. check if entry is blank.
    if entry == []:
        return 0
    else:
        return 1


def encryptor_button():
    nmsg = encrypt(entry.get(), entry2.get())
    clear = check_entry(entry3.get())

    if clear:
        entry3.delete(0, tk.END)

    entry3.insert(0, str(nmsg))


def deencryptor_button():
    nmsg = deencrypt(entry.get(), entry2.get())
    clear = check_entry(entry3.get())

    if clear:
        entry3.delete(0, tk.END)
    entry3.insert(0, str(nmsg))


# ----------------- Establish root
root = tk.Tk()
root
# ---------------- Top boxes

frame1 = tk.Frame(root, height=100, width=200, bg="grey", relief="ridge", borderwidth=5)
frame1.grid(row=0, column=0, columnspan=2, rowspan=4, ipadx=10, ipady=20)


top_label = tk.Label(text="Original message", bg="grey", fg="black")
top_label.grid(row=0, column=0, columnspan=2)


entry = tk.Entry()
entry.grid(row=1, column=0, columnspan=2, rowspan=1)

top_label = tk.Label(text="Code word", bg="grey", fg="black")
top_label.grid(row=2, column=0, columnspan=2)

entry2 = tk.Entry()
entry2.grid(row=3, column=0, columnspan=2)

# ---------------- Action buttons

button = tk.Button(root, text="Encript", command=encryptor_button, bg="Red", fg="white")

button.grid(row=6, column=0, pady=10, padx=10, ipadx=20, ipady=10)

button2 = tk.Button(
    root, text="De-encript", command=deencryptor_button, bg="#008", fg="white"
)

button2.grid(row=6, column=1, pady=10, padx=10, ipadx=10, ipady=10)


# ---------------- Bottom box

frame2 = tk.Frame(root, height=50, width=200, bg="#55f", relief="ridge", borderwidth=5)

frame2.grid(row=8, column=0, columnspan=2, rowspan=4, ipadx=10, ipady=20)

top_label = tk.Label(text="Translated message", bg="#55f", fg="white")
top_label.grid(row=8, column=0, columnspan=2)
entry3 = tk.Entry()
entry3.grid(row=9, column=0, columnspan=2)


root.mainloop()
