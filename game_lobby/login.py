from wx import *
import wx.richtext as rt
import time

BUTTON_WIDTH = 55
REGISTER_BUTTON_WIDTH = 70
BUTTON_BUFFER = 10
TEXT_BOX_HEIGHT = 30
LABEL_BUFFER = 70
BORDER = 10
TEXT_BOX_BUFFER = 10
LOGIN_WINDOW_WIDTH = 350
LOGIN_WINDOW_HEIGHT = 155
X_INDEX = 0
Y_INDEX = 1



class LoginWindow(Frame):

    def __init__(self):
        self.app = App(False)
        Frame.__init__(self, None, title = "Log In", size = (LOGIN_WINDOW_WIDTH, LOGIN_WINDOW_HEIGHT))

        self.username_input = TextCtrl(self, style = TE_PROCESS_ENTER, pos = (LABEL_BUFFER + BORDER, TEXT_BOX_BUFFER), size = (self.GetSizeTuple()[X_INDEX] - LABEL_BUFFER - BORDER * 2, TEXT_BOX_HEIGHT))
        self.password_input = TextCtrl(self, style = TE_PROCESS_ENTER | TE_PASSWORD, pos = (LABEL_BUFFER + BORDER,self.username_input.GetPositionTuple()[Y_INDEX] + TEXT_BOX_HEIGHT + TEXT_BOX_BUFFER), size = (self.GetSizeTuple()[X_INDEX] - LABEL_BUFFER - BORDER * 2,TEXT_BOX_HEIGHT))
        StaticText(self, label = "Username", pos = (BORDER, self.username_input.GetPositionTuple()[Y_INDEX]))
        StaticText(self, label = "Password", pos = (BORDER, self.password_input.GetPositionTuple()[Y_INDEX]))
        self.register_text = HyperlinkCtrl(self, id = ID_ANY, url = "", pos = (LABEL_BUFFER + BORDER, self.password_input.GetPositionTuple()[Y_INDEX] + TEXT_BOX_HEIGHT), label = "New here? Register here")
        self.register_text.Bind(EVT_HYPERLINK, self.register_mode)
        self.login_button = Button(self, label = "Login", size = (BUTTON_WIDTH,TEXT_BOX_HEIGHT), pos = ((self.GetSizeTuple()[X_INDEX] - BUTTON_WIDTH) / 2, self.register_text.GetPositionTuple()[Y_INDEX] + self.register_text.GetSizeTuple()[Y_INDEX] + BORDER))
        self.register_button =  Button(self, label = "Register", size = (REGISTER_BUTTON_WIDTH,TEXT_BOX_HEIGHT))
        self.register_button.Hide()
        self.message = None
        self.Show(True)


        
    def close(self):
        self.Destroy()

    def register_mode(self, event):
        self.SetSize(Size(LOGIN_WINDOW_WIDTH, LOGIN_WINDOW_HEIGHT + TEXT_BOX_BUFFER + TEXT_BOX_HEIGHT))
        self.register_button.SetPosition(((self.GetSizeTuple()[X_INDEX] - BUTTON_WIDTH * 2) /2, self.GetSizeTuple()[Y_INDEX] - TEXT_BOX_HEIGHT * 2))
        self.login_button.Hide()
        self.register_text.Hide()
        self.password_input_2 =  TextCtrl(self, style = TE_PROCESS_ENTER | TE_PASSWORD, pos = (LABEL_BUFFER + BORDER,TEXT_BOX_HEIGHT * 2 + TEXT_BOX_BUFFER * 3), size = (LOGIN_WINDOW_WIDTH - LABEL_BUFFER - BORDER * 2,TEXT_BOX_HEIGHT))
        self.retype = StaticText(self, label = "Retype\nPassword", pos = (BORDER, TEXT_BOX_BUFFER * 2 + TEXT_BOX_HEIGHT * 2))
        self.register_button.Show()
        self.cancel_button =  Button(self, label = "Cancel", size = (BUTTON_WIDTH,TEXT_BOX_HEIGHT), pos = ((self.register_button.GetPositionTuple()[X_INDEX] + self.register_button.GetSizeTuple()[X_INDEX]), self.register_button.GetPositionTuple()[Y_INDEX]))
        self.cancel_button.Bind(EVT_BUTTON, self.login_mode)
        if (self.message != None): 
            self.message.Destroy()
            self.message = None

    def login_mode(self, event = None):
        self.SetSize((LOGIN_WINDOW_WIDTH, LOGIN_WINDOW_HEIGHT))
        self.register_button.Hide()
        self.login_button.Show()
        self.register_text.Show()
        self.password_input_2.Destroy()
        self.cancel_button.Destroy()
        self.retype.Destroy()
        if (self.message != None): 
            self.message.Destroy()
            self.message = None

    def bind_functions(self, on_register, on_login):
        self.login_button.Bind(EVT_BUTTON, on_login)
        self.register_button.Bind(EVT_BUTTON, on_register)

    def mainloop(self):
        self.app.MainLoop()

    def get_login_info(self):
        return str(self.username_input.GetValue()), str(self.password_input.GetValue())

    def get_register_info(self):
        register_info = str(self.username_input.GetValue()), str(self.password_input.GetValue()), str(self.password_input_2.GetValue())
        self.password_input.Clear()
        self.password_input_2.Clear()
        return register_info
     
    def set_message(self, text):
        if self.message != None:
            self.message.Destroy()
        self.message = StaticText(self, pos = (BORDER, self.GetSizeTuple()[Y_INDEX] - BORDER * 2), label = text)

