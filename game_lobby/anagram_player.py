from player_emitted import Player
import sys
import os
sys.path.append(os.path.join("../../"))
from waldo.lib import Waldo
from gui_string import GUI_String_Ext
from game_window import GameWindow
import time
from wx import *
import wx.richtext as rt
WORD_MIN = 3
WORD_MAX = 7

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
        self.enter_waiting_room()
        self.player = Waldo.tcp_connect(Player, 'localhost', 6767, name, GUI_String_Ext(self.text_display))
        self.player.join_waiting_room()
        self.app.MainLoop()
        

    def enter_waiting_room(self):
        self.app = App(False)
        frame = Frame(None, -1, title = "Anagram Waiting Room", size = (CHAT_WINDOW_WIDTH, CHAT_WINDOW_HEIGHT))
        self.text_display = TextCtrl(frame, size = (CHAT_WINDOW_WIDTH, MESSAGE_BOX_HEIGHT), style = TE_READONLY | TE_MULTILINE)
        self.text_input = TextCtrl(frame, style = TE_PROCESS_ENTER, pos = (0,CHAT_WINDOW_HEIGHT - TEXT_BOX_HEIGHT), size = (CHAT_WINDOW_WIDTH - BUTTON_WIDTH, TEXT_BOX_HEIGHT))
        send_button = Button(frame, label = "Send", size = (BUTTON_WIDTH,TEXT_BOX_HEIGHT), pos = (CHAT_WINDOW_WIDTH - BUTTON_WIDTH, CHAT_WINDOW_HEIGHT - TEXT_BOX_HEIGHT))
        self.text_input.Bind(EVT_TEXT_ENTER, self.read_waiting_room_message)    
        send_button.Bind(EVT_BUTTON, self.read_waiting_room_message)
        frame.Show(True)

    def set_anagram_display(self, anagram):
        self.anagram_display.Clear()
        self.anagram_display.WriteText(anagram)

    def initialize_game_window(self):
        self.game_app = App(False)
        frame = Frame(None, -1, title = "Anagram Game", size = (GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))
        self.anagram_display = rt.RichTextCtrl(frame, size = (GAME_WINDOW_WIDTH, ANAGRAM_HEIGHT), style = TE_READONLY | TE_CENTRE)
        self.anagram_display.BeginFontSize(ANAGRAM_HEIGHT/2)
        self.message_display = TextCtrl(frame, size = (GAME_WINDOW_WIDTH, GAME_MESSAGE_BOX_HEIGHT), style = TE_READONLY | TE_MULTILINE, pos = (0, ANAGRAM_HEIGHT))
        self.answer_input = TextCtrl(frame, style = TE_PROCESS_ENTER, pos = (0,GAME_WINDOW_HEIGHT - TEXT_BOX_HEIGHT), size = (GAME_WINDOW_WIDTH - BUTTON_WIDTH,TEXT_BOX_HEIGHT))
        send_answer = Button(frame, label = "Answer", size = (BUTTON_WIDTH,TEXT_BOX_HEIGHT), pos = (GAME_WINDOW_WIDTH - BUTTON_WIDTH, GAME_WINDOW_HEIGHT - TEXT_BOX_HEIGHT))
        self.answer_input.Bind(EVT_TEXT_ENTER, self.send_answer)    
        send_answer.Bind(EVT_BUTTON, self.send_answer)
        frame.Show(True)
        time.sleep(1)

        self.message_display.AppendText("Waiting for game to begin...\n")
        self.anagram = self.player.get_anagram()
        self.solutions = self.player.get_solutions()
       
    def play_anagram_game(self):
        #while not self.player.game_in_session():
        #    time.sleep(0.1)
        self.used_words = []
        self.set_anagram_display(self.anagram)
       # self.game_window.mainloop()


    def send_answer(self, event):
        if self.player.game_in_session():
            answer = self.answer_input.GetValue().upper()
            self.answer_input.Clear()
            if len(answer) > 0 and answer[0] == "/":
                command = answer[1:]
                if command == 'SHUFFLE':
                    anagram = self.shuffle_anagram(anagram)
                else:
                     self.message_display.AppendText('Invalid game command. \n\t/shuffle - shuffles anagram\n')
            elif len(answer) <= WORD_MAX and len(answer) >= WORD_MIN:
                if answer in self.used_words:
                    self.message_display.AppendText(answer + ' was already used.\n')#change for game window
                elif answer in self.solutions:
                    self.used_words.append(answer)
                    self.player.add_points(len(answer))
                else:
                    self.message_display.AppendText(answer + ' is an invalid word.\n')
            else:
                self.message_display.AppendText("Word is not between 3 and 7 letters.\n")#need to change for anagram

        else:
        #self.text_display.AppendText('Remaining answers:\n')
        #for answer in solutions:
         #   if answer not in used_words: 
          #       self.text_display.AppendText(answer + "\n")
            pass
    
    def shuffle_anagram(self, anagram):
        for i in anagram:
            rand_int = random.randint(0, len(anagram) - 1)
            temp = anagram[rand_int]
            anagram = anagram.replace(temp, i, 1)
            anagram = anagram.replace(i, temp, 1)
        return anagram

    def leave_waiting(self):
        self.player.leave_waiting()
        self.app.Destroy()

    def read_waiting_room_message(self, event):
        message = str(self.text_input.GetValue() + "\n")
        self.text_input.Clear()
        if len(message) > 0 and message[0] is "/":
            message = message[1:]
            if message == "ready\n":
                if self.player.game_in_session():
                    self.text_display.AppendText("Cannot enter game room. Game is in session.\n")
                else:
                    self.leave_waiting()
                    self.player.add_to_game()
                    self.initialize_game_window()
                    self.play_anagram_game()
            elif message == "leave\n":
                self.leave_waiting()
            else:
                self.text_display.AppendText('Cannot read command.  Below are valid commands.\n\t"/ready" to try to enter the game room.\n\t"/leave" to leave the waiting room.\n')
        else:
            self.player.send_to_waiting(message)
