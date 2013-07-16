from wx import *
import wx.richtext as rt

BUTTON_WIDTH = 50
TEXT_BOX_HEIGHT = 30
CHAT_WINDOW_WIDTH = 500
CHAT_WINDOW_HEIGHT = 300
MESSAGE_BOX_HEIGHT = 50
ANAGRAM_HEIGHT = 100

class GameWindow(Frame):

    def __init__(self):
        self.app = App(False)
        title = "Anagram Game"
        Frame.__init__(self, None, title = title, size = (CHAT_WINDOW_WIDTH, CHAT_WINDOW_HEIGHT))
        self.anagram_display = rt.RichTextCtrl(self, size = (CHAT_WINDOW_WIDTH, ANAGRAM_HEIGHT), style = TE_READONLY | TE_CENTRE)
        self.text_display = TextCtrl(self, size = (CHAT_WINDOW_WIDTH, MESSAGE_BOX_HEIGHT), style = TE_READONLY | TE_MULTILINE, pos = (0, ANAGRAM_HEIGHT))
        self.text_input = TextCtrl(self, style = TE_PROCESS_ENTER, pos = (0,CHAT_WINDOW_HEIGHT - TEXT_BOX_HEIGHT), size = (CHAT_WINDOW_WIDTH,TEXT_BOX_HEIGHT))
        self.send_button = Button(self, label = "Send", size = (BUTTON_WIDTH,TEXT_BOX_HEIGHT), pos = (CHAT_WINDOW_WIDTH - BUTTON_WIDTH, CHAT_WINDOW_HEIGHT - TEXT_BOX_HEIGHT))
        self.Show(True)

    def set_anagram_display(self, anagram):
        self.anagram_display.Clear()
        self.anagram_display.WriteText(anagram)
    
    def show_message(self, txt_message):
        self.text_display.Clear()
        self.text_display.AppendText(txt_message)

    def bind_enter_text(self, funct):
        self.Bind(EVT_TEXT_ENTER, funct, self.text_input)
        self.Bind(EVT_BUTTON, funct, self.send_button)

    def get_text(self):
        message = self.text_input.GetValue()
        self.text_input.Clear()
        return message

    def mainloop(self):
        self.app.MainLoop()
