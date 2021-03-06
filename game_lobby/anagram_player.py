from player_emitted import Player
import sys, os, random, time
sys.path.append(os.path.join("../../"))
from waldo.lib import Waldo
from gui_string import GUI_String_Ext
from wx import *
import wx.richtext as rt
WORD_MIN = 3
WORD_MAX = 7
HOSTNAME = '127.0.0.1'
BUTTON_WIDTH = 50
TEXT_BOX_HEIGHT = 30
CHAT_WINDOW_WIDTH = 500
CHAT_WINDOW_HEIGHT = 500
MESSAGE_BOX_HEIGHT = 450

TEXT_BOX_HEIGHT = 30
GAME_WINDOW_WIDTH = 500
GAME_WINDOW_HEIGHT = 200
GAME_MESSAGE_BOX_HEIGHT = 50
ANAGRAM_HEIGHT = 100

class AnagramPlayer:
    
    def __init__(self, name):
        self.name = name
        self.enter_waiting_room()
        self.initialize_game_window()
        self.player = Waldo.tcp_connect(Player, HOSTNAME, 6767, name, GUI_String_Ext(self.text_display), GUI_String_Ext(self.message_display))
        self.player.join_waiting_room()
        self.text_display.AppendText("You have entered the anagram waiting room. Type /ready when you are ready to play.\n")
        self.game_app.MainLoop()
        

    def enter_waiting_room(self):
        app = App(False)
        self.frame = Frame(None, -1, title = self.name + "'s Anagram Waiting Room", size = (CHAT_WINDOW_WIDTH, CHAT_WINDOW_HEIGHT))
        self.text_display = TextCtrl(self.frame, size = (CHAT_WINDOW_WIDTH, MESSAGE_BOX_HEIGHT), style = TE_READONLY | TE_MULTILINE)
        self.text_input = TextCtrl(self.frame, style = TE_PROCESS_ENTER, pos = (0,CHAT_WINDOW_HEIGHT - TEXT_BOX_HEIGHT), size = (CHAT_WINDOW_WIDTH - BUTTON_WIDTH, TEXT_BOX_HEIGHT))
        send_button = Button(self.frame, label = "Send", size = (BUTTON_WIDTH, TEXT_BOX_HEIGHT), pos = (CHAT_WINDOW_WIDTH - BUTTON_WIDTH, CHAT_WINDOW_HEIGHT - TEXT_BOX_HEIGHT))
        self.text_input.Bind(EVT_TEXT_ENTER, self.read_waiting_room_message)    
        send_button.Bind(EVT_BUTTON, self.read_waiting_room_message)
        self.frame.Show(True)

    def set_anagram_display(self, anagram):
        self.anagram_display.Clear()
        self.anagram_display.WriteText(anagram)

    def initialize_game_window(self):
        self.game_app = App(False)
        self.game_frame = Frame(None, -1, title = self.name + "'s Anagram Game", size = (GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))
        self.anagram_display = rt.RichTextCtrl(self.game_frame, size = (GAME_WINDOW_WIDTH, ANAGRAM_HEIGHT), style = TE_READONLY | TE_CENTRE)
        self.anagram_display.BeginFontSize(ANAGRAM_HEIGHT/2)
        self.message_display = TextCtrl(self.game_frame, size = (GAME_WINDOW_WIDTH, GAME_MESSAGE_BOX_HEIGHT), style = TE_READONLY | TE_MULTILINE, pos = (0, ANAGRAM_HEIGHT))
        self.answer_input = TextCtrl(self.game_frame, style = TE_PROCESS_ENTER, pos = (0,GAME_WINDOW_HEIGHT - TEXT_BOX_HEIGHT), size = (GAME_WINDOW_WIDTH - BUTTON_WIDTH,TEXT_BOX_HEIGHT))
        send_answer = Button(self.game_frame, label = "Send", size = (BUTTON_WIDTH,TEXT_BOX_HEIGHT), pos = (GAME_WINDOW_WIDTH - BUTTON_WIDTH, GAME_WINDOW_HEIGHT - TEXT_BOX_HEIGHT))
        self.answer_input.Bind(EVT_TEXT_ENTER, self.send_answer)    
        send_answer.Bind(EVT_BUTTON, self.send_answer)
        

    def display_game_window(self):
        self.game_frame.Show(True)
        self.message_display.AppendText("Waiting for game to begin...\n")   

    def send_answer(self, event):
        if self.player.game_in_session():
            answer = self.answer_input.GetValue().upper()
            self.answer_input.Clear()
            if len(answer) == 0:
                self.set_anagram_display(self.shuffle_anagram())
            elif len(answer) <= WORD_MAX and len(answer) >= WORD_MIN:
                self.player.check_answer(answer)
            else:
                self.message_display.AppendText("Word is not between 3 and 7 letters.\n")

        elif self.player.game_ended():
            self.message_display.AppendText('Remaining answers:\n')
            self.player.display_remaining_answers()
    
    def shuffle_anagram(self):
        for i in self.anagram:
            rand_int = random.randint(0, len(self.anagram) - 1)
            temp = self.anagram[rand_int]
            self.anagram = self.anagram.replace(temp, i, 1)
            self.anagram = self.anagram.replace(i, temp, 1)
        return self.anagram

    def leave_waiting(self):
        self.player.leave_waiting()
        self.frame.Close()

    def read_waiting_room_message(self, event):
        message = str(self.text_input.GetValue() + "\n")
        self.text_input.Clear()
        if len(message) > 0 and message[0] is "/":
            message = message[1:]
            if message == "ready\n":
                if self.player.game_in_session():
                    self.text_display.AppendText("Cannot enter game room. Game is in session.\n")
                else:
                    self.player.add_to_game()
                    time.sleep(1)
                    self.display_game_window()
                    self.anagram = self.player.get_game_information()
            elif message == "leave\n":
                self.leave_waiting()
            else:
                self.text_display.AppendText('Cannot read command.  Below are valid commands.\n\t"/ready" to try to enter the game room.\n\t"/leave" to leave the waiting room.\n')
        else:
            self.player.send_to_waiting(message)
