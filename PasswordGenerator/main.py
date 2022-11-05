from tkinter import *
from password_generator import random_password_generator


# create a window
root = Tk()
generatedPassword = "Click Generate Password button..!" # Initially generated password is empty


def copyText():
    root.clipboard_clear()
    root.clipboard_append(generatedPassword)


def generatePassword():
    global generatedPassword
    generatedPassword = random_password_generator()
    passwordLabel.config(text=generatedPassword)


# set title & geometry to the window
root.title("Password Generator")
root.geometry("700x500")

# disable the window resize
root.resizable(False, False)

# create a frame to display components in side by side view
frame1 = Frame(root)
frame1.pack(pady=(150, 50))

# add label to display the generated password in frame
passwordLabel = Label(frame1, text=generatedPassword, bg="#dee0e3", fg="#0e5fe3",
                      padx=10, pady=15, width=40, height=1, font="Helvetica 12 bold")
passwordLabel.grid(column=0, row=0, padx=10)

# add a button to copy the generated password
copyButton = Button(frame1, text="COPY", bg="#0e5fe3", fg="#fff", padx=10, pady=6,
                    font="Helvetica 12 bold",command=copyText)
copyButton.grid(column=1, row=0)

pass_gen_btn = Button(root, text="GENERATE PASSWORD", height=2, bg="#0e5fe3", fg="#fff",
                      activebackground="#fff", activeforeground="#0e5fe3", padx=10,
                      font="Helvetica 12 bold", command=lambda: generatePassword())
pass_gen_btn.pack()

# running the application loop
root.mainloop()


