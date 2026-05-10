import tkinter as tk
from tkmacosx import Button
import pathlib, os

def clearEntry(*args):
    entryBox = args[1]
    entryBox.delete(0, "end")

def displayHeader(headFrame, backCommand=None):
   img_file_name = "arrow.png"
   current_dir = pathlib.Path(__file__).parent.resolve()
   img_path = os.path.join(current_dir, img_file_name)
   imgArw = tk.PhotoImage(file=img_path)
   imgArwLabel = tk.Label(master=headFrame, image=imgArw, bg="#2699FB", cursor="hand2")
   imgArwLabel.image = imgArw
   if backCommand:                                      # bind the arrow if a command is given
       imgArwLabel.bind("<Button-1>", backCommand)
   imgArwLabel.grid(row=0, column=0, sticky="w")

   headLabel = tk.Label(master=headFrame, text="Login", bg="#2699FB", height=3)
   headLabel.grid(row=0, column=1, padx=10, sticky="nsew")

   headFrame.grid(row=0, column=0, sticky="ew", columnspan=3)

def setUpLogin(LoginFrame, SignUpPage, loginAttempt, passwordResetEmail):
    """
    Adds all elements for the main frame of signup screen and displays the frame
    """
    # add elements

    # Name label and textbox
    emailLabel = tk.Label(master=LoginFrame, text="Email", fg="#000000", bg="#FAFAFA", height=3)
    emailLabel.grid(row=1, column=0, columnspan=3, padx=10, sticky="w")
    emailText = tk.StringVar()
    emailText.set("Please enter your email")
    emailBox = tk.Entry(master=LoginFrame, width=30, font=('calibre',18,'normal'),
                       textvariable=emailText, bg="#FFFFFF",  fg="#2699FB",
                       highlightthickness=1, relief="flat",highlightcolor="#2699FB",
                       highlightbackground="#2699FB")
    emailBox.grid(row=2, column=0, columnspan=3, padx=30, sticky="w")
    emailBox.bind("<FocusIn>", lambda *args: clearEntry(*args, emailBox))

    # password label and textbox
    passwordLabel = tk.Label(master=LoginFrame, text="Password", fg="#000000", bg="#FAFAFA", height=3)
    passwordLabel.grid(row=3, column=0, columnspan=3, padx=10, sticky="w")
    passwordText = tk.StringVar()
    passwordText.set("********")
    passwordBox = tk.Entry(master=LoginFrame, width=30, font=('calibre', 18, 'normal'),
                           textvariable=passwordText, show="*",  # ← ADD
                           bg="#FFFFFF", fg="#2699FB",
                        highlightthickness=1, relief="flat", highlightcolor="#2699FB",
                        highlightbackground="#2699FB")
    passwordBox.grid(row=4, column=0, columnspan=3, padx=30, sticky="w")
    passwordBox.bind("<FocusIn>", lambda *args: clearEntry(*args, passwordBox))

    # error message
    errorLabel = tk.Label(
        master=LoginFrame,
        text="",  # so that it starts with no text
        fg="#FF0000",
        bg="#FAFAFA",
        height=3
    )
    errorLabel.grid(row=5, column=0, columnspan=3, padx=10, sticky="ew")

    # forgot password label
    ForgotpwLabel = tk.Label(master=LoginFrame, text="Forgot Password?", font=("Arial", 10, "underline"),
                             cursor="hand2", fg="#2699FB", bg="#FAFAFA", height=1)
    ForgotpwLabel.grid(row=6, column=1, columnspan=3, padx=10, sticky="w")
    ForgotpwLabel.bind("<Button-1>", lambda *args: passwordResetEmail(*args, emailText.get(), errorLabel))

    # Submit button
    submit = Button(master=LoginFrame, width=31, bg="#2699FB", text="Submit",borderless=1, fg="#FFFFFF",
                    command=lambda: loginAttempt(emailText.get(), passwordText.get(), errorLabel))
    submit.grid(row=7, pady=20, column=0, columnspan=3, sticky="nsew")

    # sign up section
    SignUpLabel = tk.Label(master=LoginFrame, text="Don't have an Account? Sign up", font=("Arial", 16, "underline"),
                           cursor="hand2", fg="#2699FB", bg="#FAFAFA", height=3)
    SignUpLabel.grid(row=9, column=0, columnspan=3, padx=10, sticky="ew")
    SignUpLabel.bind("<Button-1>", SignUpPage)

    return LoginFrame


def displayLoginView(LoginFrame, headFrame):

    displayHeader(headFrame)

    # display frame
    LoginFrame.grid(row=1, column=0, columnspan=3, rowspan=15, sticky="nsew")


def hideLogin(headFrame, LoginFrame):
    LoginFrame.grid_forget()

    for widget in headFrame.winfo_children():
        widget.destroy()

def colorValidLabel(label):
    label.config(fg="#00BC16")

def colorInvalidLabel(label):
    label.config(fg="#F20847")

def updateLabelText(label, text):
    label.config(text=text)