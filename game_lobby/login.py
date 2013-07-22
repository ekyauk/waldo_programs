from wx import *
import wx.richtext as rt
import time

BUTTON_WIDTH = 50
BUTTON_BUFFER = 10
TEXT_BOX_HEIGHT = 30
LABEL_BUFFER = 70
BORDER = 10
TEXT_BOX_BUFFER = 15
LOGIN_WINDOW_WIDTH = 350
LOGIN_WINDOW_HEIGHT = 155



class LoginWindow(Frame):

    def __init__(self):
        self.app = App(False)
        Frame.__init__(self, None, title = "Log In", size = (LOGIN_WINDOW_WIDTH, LOGIN_WINDOW_HEIGHT))
        StaticText(self, label = "Username", pos = (BORDER, TEXT_BOX_BUFFER))
        StaticText(self, label = "Password", pos = (BORDER, TEXT_BOX_BUFFER * 2 + TEXT_BOX_HEIGHT))
        self.username_input = TextCtrl(self, style = TE_PROCESS_ENTER, pos = (LABEL_BUFFER + BORDER, TEXT_BOX_BUFFER), size = (LOGIN_WINDOW_WIDTH - LABEL_BUFFER - BORDER * 2, TEXT_BOX_HEIGHT))
        self.password_input = TextCtrl(self, style = TE_PROCESS_ENTER | TE_PASSWORD, pos = (LABEL_BUFFER + BORDER,TEXT_BOX_HEIGHT + TEXT_BOX_BUFFER * 2), size = (LOGIN_WINDOW_WIDTH - LABEL_BUFFER - BORDER * 2,TEXT_BOX_HEIGHT))
        self.login_button = Button(self, label = "Login", size = (BUTTON_WIDTH,TEXT_BOX_HEIGHT), pos = ((LOGIN_WINDOW_WIDTH - BUTTON_WIDTH * 3 - BUTTON_BUFFER) /2, TEXT_BOX_HEIGHT * 2 + TEXT_BOX_BUFFER * 2.5))
        self.register_button =  Button(self, label = "Register", size = (BUTTON_WIDTH  * 2,TEXT_BOX_HEIGHT), pos = ((LOGIN_WINDOW_WIDTH - BUTTON_WIDTH) /2, TEXT_BOX_HEIGHT * 2 + TEXT_BOX_BUFFER * 2.5))
        self.message = None
        self.Show(True)

    def bind_functions(self, on_register, on_login):
        self.login_button.Bind(EVT_BUTTON, on_login)
        self.register_button.Bind(EVT_BUTTON, on_register)
        
    def close(self):
        self.Destroy()

    def mainloop(self):
        self.app.MainLoop()

    def get_login_info(self):
        return str(self.username_input.GetValue()), str(self.password_input.GetValue())

            
    def invalid_info(self):
        if self.message != None:
            self.message.Hide()
        self.message = StaticText(self, pos = (BORDER, LOGIN_WINDOW_HEIGHT - TEXT_BOX_HEIGHT), label = "Username/password combination was not found.")

    def register_message(self, registered):
        if self.message != None:
            self.message.Hide()
        if registered:
            self.message = StaticText(self, pos = (BORDER, LOGIN_WINDOW_HEIGHT - TEXT_BOX_HEIGHT), label = "Account created! Please login.")
        else:
            self.message = StaticText(self, pos = (BORDER, LOGIN_WINDOW_HEIGHT - TEXT_BOX_HEIGHT), label = "Username is already used.")
