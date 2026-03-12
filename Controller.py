import SignUp
import LoginView


#code to create the windows
window, headFrame, loginFrame, signUpFrame = SignUp.setupWindow()


#Display log in
LoginView.displayHeader(headFrame)
LoginView.setUpLogin(LoginFrame)
#SignUp.displayHeader(headFrame)
#SignUp.displaySignUp(mainFrame)


window.mainloop() #update window