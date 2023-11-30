import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Simple Login Python")
window.geometry('750x550')

def login():
    username = "221011400667"
    password = "unpam#400667"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Berhasil!", message="Selamat datang Arria Gemilang!")
        window.destroy()
    else:
        messagebox.showerror(title="Kesalahan!", message="Password anda salah!")

# bikin frame
frame = tkinter.Frame(window, bg='#F0F8FF', padx=20, pady=20)
frame.pack(pady=50)

# bikin label, entry, sama button
login_label = tkinter.Label(frame, text="Simple Login Python", fg="#FF1493", font=("Verdana", 18, "bold"))
username_label = tkinter.Label(frame, text="Username", font=("Verdana", 12))
password_label = tkinter.Label(frame, text="Password", font=("Verdana", 12))
username_entry = tkinter.Entry(frame, font=("Verdana", 12))
password_entry = tkinter.Entry(frame, show="*", font=("Verdana", 12))
login_button = tkinter.Button(frame, text="Login", bg="#FF1493", fg="#FFFFFF", font=("Verdana", 12), command=login)

# grid buat login, username, sama button
login_label.grid(row=0, column=0, columnspan=2, pady=10)
username_label.grid(row=1, column=0, sticky="e", pady=5)
username_entry.grid(row=1, column=1, pady=5)
password_label.grid(row=2, column=0, sticky="e", pady=5)
password_entry.grid(row=2, column=1, pady=5)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

# warna background
window.configure(bg='#F0F0F0')
window.option_add("*Font", "Verdana 10")

window.mainloop()