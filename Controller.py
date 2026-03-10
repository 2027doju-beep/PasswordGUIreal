import SignUp
import LoginView


#code to create the windows
window, headFrame, mainFrame = SignUp.setupWindow()

#Display login in
LoginView.displayHeader(headFrame)
LoginView.displayLogin(mainFrame)


#SignUp.displayHeader(headFrame)
#SignUp.displaySignUp(mainFrame)

window.mainloop() #update window