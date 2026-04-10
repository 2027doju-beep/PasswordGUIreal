from operator import truediv
import SignUp
import LoginView

window, headFrame, loginFrame, signUpFrame = SignUp.setupWindow()

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

    # ✅Check if passwords match
    if password == confirmPassword and password != "Passwords match":
        SignUp.colorValidLabel(labels[0])
        match = True
    else:
        SignUp.colorInvalidLabel(labels[0])
        match = False

    # ✅Return True only if all three conditions are met
    valid = length and foundchar and match
    return valid


def loginAttempt(email, password, errorLabel):
    print("called with:" + email + " and " + password)


# ✅createAccountAttempt function
def createAccountAttempt(name, email, password, confirmPassword):
    print(f"Attempting to create account for: {name}, {email}")

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

    print("Account created successfully!")
    return True


SignUp.setupSignUp(signUpFrame, validatePW, createAccountAttempt)
loginFrame = LoginView.setUpLogin(loginFrame, signUpPage, loginAttempt)

LoginView.displayLoginView(loginFrame, headFrame)

window.mainloop()
