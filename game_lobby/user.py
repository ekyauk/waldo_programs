from user_emitted import User
from server_emitted import Server
from player_emitted import Player
from anagram_player import AnagramPlayer
from gui_string import GUI_String_Ext
import sys
import os
sys.path.append(os.path.join("../../"))
from waldo.lib import Waldo
import time
import random
sys.path.append(os.path.join("mtTkinter-0.4"))
from mtTkinter import *
HOSTNAME = '127.0.0.1'
WORD_MIN = 3
WORD_MAX = 7
global user
global name
global chatline
global text_window
global user_window
global name

def create_gui_window():
    global user_window
    user_window = Tk()
    global chatline
    global text_window
    text_window = Text(user_window, height = 40, width = 45, bg = '#fff', wrap = WORD)
    text_window.pack()
    chatline = Entry(user_window)
    chatline.pack(side = LEFT)
    send_button = Button(user_window, text = "Send", command = send_message)
    send_button.pack()

def connect_user(name):
    create_gui_window()
    print 'gui created'
    global user
    gui_string = GUI_String_Ext(text_window)
    print 'gui string created'
    user = Waldo.tcp_connect(User, HOSTNAME, 6922, name, gui_string)
    print 'user connected.'
    #text_window.insert(END, "You have been added to the chat server.\n")
    user.add_to_server(False)
    user_window.mainloop()
 

def read_command(message):
    if message.startswith('quit'):
        user.quit(False)
        print 'You have left the chatserver.'
        exit(0)

    elif message.startswith('private'):
       new_start = len('private ')
       new_message = message[new_start:]
       if (new_message == ""):
           print('Username must be specified.')
       else:
           split_message = new_message.partition(' ')#split_message now contains the tuple (username,' ',message) 
           user.private_message(split_message[0], split_message[2]);

    elif message.startswith('users_list'):
       user.print_users()

    elif message.startswith('anagram_game'):
        user.quit(True)
        anagram_player = AnagramPlayer(name, print_message)
        print 'You have entered the anagram waiting room.'
        anagram_player.read_waiting_room_commands()    
        user.add_to_server(True)
            

    elif message.startswith('h'):
        print 'Commands:\n\t/quit - to leave the chatroom.\n\t/private [username] [message] - to send a private message.\n\t/users_list - to see a list of users.\n\t/anagram_game - to enter the anagram game.'

    else:
       print "Invalid command. Type /h for a list of commands."

def send_message():
    """while True:
        message = raw_input()"""
    message = chatline.get()
    chatline.delete(0, END)
    print message
    if len(message) > 0 and message[0] is "/":
        message = message[1:]
        read_command(message)
    else:
        message = name + ': ' + message
        user.send_message(message)

if __name__ == '__main__':
    name = raw_input('ENTER YOUR NAME: ')
    connect_user(name)
    send_message(name)
