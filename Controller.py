from operator import truediv
import SignUp
import LoginView
import Model
import smtplib
Model.createUserTable()
Model.createRoleTable()
from email.message import EmailMessage

window, headFrame, loginFrame, signUpFrame = SignUp.setupWindow()


def passwordResetEmail(*args):
    print(args)
    # get args for email and label
    email = args[1]
    errorLabel = args[2]

    # Email Content
    msg = EmailMessage()
    msg.set_content("Your password has been automatically reset to: TestPW1!. " +
                    "Please login and update your password.")
    msg['Subject'] = 'Password Reset Request'
    msg['From'] = "julie@douaze.com"
    msg['To'] = email

    # Send Email
    try:
        # Use App Password here, not your regular password
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("julie@douaze.com", "wrclesmqpqqfnanj")
        server.send_message(msg)
        server.quit()
        LoginView.colorValidLabel(errorLabel)
        LoginView.updateLabelText(errorLabel,"Password Reset Complete! Please check your email")


    except Exception as e:
        print(e)
        LoginView.colorInvalidLabel(errorLabel)
        LoginView.updateLabelText(errorLabel,"Email could not be sent, did you create an account?")

def signUpPage(event):
    LoginView.hideLogin(headFrame, loginFrame)
    SignUp.displaySignup(signUpFrame, headFrame)

def validatePW(*args):
    password = args[3].get()
    confirmPassword = args[4].get()
    labels = args[5]  # [matchLabel, lengthLabel, charLabel]

    # Check length
    if len(password) < 8:
        SignUp.colorInvalidLabel(labels[1])
        length = False
    else:
        SignUp.colorValidLabel(labels[1])
        length = True

    # Check special character
    specialcharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '?']
    foundchar = any(spchar in password for spchar in specialcharacters)
    if foundchar:
        SignUp.colorValidLabel(labels[2])
    else:
        SignUp.colorInvalidLabel(labels[2])

    #Check if passwords match
    if password == confirmPassword and password != "Passwords match":
        SignUp.colorValidLabel(labels[0])
        match = True
    else:
        SignUp.colorInvalidLabel(labels[0])
        match = False

    #Return True only if all three conditions are met
    valid = length and foundchar and match
    return valid


def loginAttempt(email, password, errorLabel):
    if Model.loginAttempt(email, password) == True:
        LoginView.colorValidLabel(errorLabel)
        LoginView.updateLabelText(errorLabel, "Success!")
    else:
        LoginView.colorInvalidLabel(errorLabel)
        LoginView.updateLabelText(errorLabel, "Incorect email or password!")

#createAccountAttempt function
def createAccountAttempt(name, email, password, confirmPassword, errorlabel, birthdate=None):
    print("Attempting to create account for: {name}, {email}")

    # Re-run validation before submitting
    # We don't have the labels here, but we can do a quick logic check
    specialcharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '?']
    foundchar = any(c in password for c in specialcharacters)

    if len(password) < 8:
        print("Account creation failed: password too short")
        return False
    if not foundchar:
        print("Account creation failed: no special character")
        return False
    if password != confirmPassword:
        print("Account creation failed: passwords don't match")
        return False

    #CHECK IF EMAIL ALREADY EXISTS
    existingUser = Model.lookupUser(email)
    if existingUser:
        print("Account creation failed: email already exists")
        errorlabel.config(text="Email already exists!")
        return False

    #CREATE USER
    Model.createUser(name, email, password)
    print("Account created successfully!")

    SignUp.hideSignUp(headFrame)
    LoginView.displayLoginView(loginFrame, headFrame)


    #go back to login page
    SignUp.hideSignUp(headFrame)
    LoginView.displayLoginView(loginFrame, headFrame)
    # I added this line to save the user.
    return True


SignUp.setupSignUp(signUpFrame, validatePW, createAccountAttempt)
loginFrame = LoginView.setUpLogin(loginFrame, signUpPage, loginAttempt, passwordResetEmail)

LoginView.displayLoginView(loginFrame, headFrame)

window.mainloop()
