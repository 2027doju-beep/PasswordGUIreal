from operator import truediv

import SignUp
import LoginView


#code to create the windows and pages
window, headFrame, loginFrame, signUpFrame = SignUp.setupWindow()

def signUpPage(event): #navigate from login to signup page
    LoginView.hideLogin(loginFrame)
    SignUp.displaySignup(signUpFrame, headFrame)

def validatePW(args):
    # args 0,1, and 2 are from the event
    # then password is 3, confirmPassword is number 4
    # then labels list is number 5[match, length, char]
    password = args[3].get()
    print("called with:" + password)

    # check for special character
    specialcharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '?']
    foundchar = False

    for spchar in specialcharacters:
        if spchar in password:
            foundchar = True

    if len(password) < 8:
        length = False
        SignUp.colorInvalidLabel(args[5][1])

    else:
        length = True
        SignUp.colorValidLabel(args[5][1])

    if not foundchar:
        foundchar = False
        SignUp.colorInvalidLabel(args[5][2])
    else:
        foundchar = True
        SignUp.colorValidLabel(args[5][2])

    validPW = True
    password =(args[3].get())
    print("called with:" + password)

def loginAttempt(email, password, errorLabel):
    print("called with:" + email + "and" + password)


SignUp.setupSignUp(signUpFrame, validatePW)
setUpLogin = LoginView.setUpLogin(loginFrame,signUpPage, loginAttempt)




#Display log in
LoginView.displayLoginView(loginFrame, headFrame)

#SignUp.displaySignup(signUpFrame, headFrame)
#SignUp.hideSignUp(signUpFrame)

window.mainloop() #update window

