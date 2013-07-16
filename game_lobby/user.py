from user_emitted import User
from server_emitted import Server
from player_emitted import Player
from anagram_player import AnagramPlayer
from keymanager_emitted import Client
from gui_string import GUI_String_Ext
from wx import *
import sys, os, time, random
sys.path.append(os.path.join("../../"))
from waldo.lib import Waldo
import OpenSSL
from OpenSSL import crypto
HOSTNAME = '127.0.0.1'
WORD_MIN = 3
WORD_MAX = 7
global user
global name
global text_display
global text_input
BUTTON_WIDTH = 50
TEXT_BOX_HEIGHT = 30
CHAT_WINDOW_WIDTH = 400
CHAT_WINDOW_HEIGHT = 500
MESSAGE_BOX_HEIGHT = 450
KEY_TEXT_FILE = "user_key.pem"
CERT_TEXT_FILE = "user_cert.pem"


KEY_MANAGER_HOST = '127.0.0.1'
KEY_MANAGER_PORT = 6974

def get_keytext():
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA,2048)
    keytext = crypto.dump_privatekey(crypto.FILETYPE_PEM,key)
    return keytext

def text_to_file(text, filename):
    f = open(filename, "w+")
    f.write(text)
    f.close()

def generate_request(CN):
    key = crypto.load_privatekey(crypto.FILETYPE_PEM,open(KEY_TEXT_FILE).read())
    req = OpenSSL.crypto.X509Req()
    req.get_subject().CN = CN
    req.set_pubkey(key)
    req.sign(key, "sha1")
    req = crypto.dump_certificate_request(crypto.FILETYPE_PEM, req)
    return req

def create_certificate():
    client = Waldo.stcp_connect(Client, KEY_MANAGER_HOST, KEY_MANAGER_PORT)
    request = generate_request(name)
    return client.req_to_cert(request)

def create_chat_window():
    app = App(False)
    title = name + "'s chat window";
    frame = Frame(None, -1, title, size = (CHAT_WINDOW_WIDTH, CHAT_WINDOW_HEIGHT))
    global text_display
    text_display = TextCtrl(frame, size = (CHAT_WINDOW_WIDTH, MESSAGE_BOX_HEIGHT), style = TE_READONLY | TE_MULTILINE)
    global text_input
    text_input = TextCtrl(frame, style = TE_PROCESS_ENTER, pos = (0,CHAT_WINDOW_HEIGHT - TEXT_BOX_HEIGHT), size = (CHAT_WINDOW_WIDTH - BUTTON_WIDTH, TEXT_BOX_HEIGHT))
    send_button = Button(frame, label = "Send", size = (BUTTON_WIDTH,TEXT_BOX_HEIGHT), pos = (CHAT_WINDOW_WIDTH - BUTTON_WIDTH, CHAT_WINDOW_HEIGHT - TEXT_BOX_HEIGHT))
    text_input.Bind(EVT_TEXT_ENTER, send_message)    
    send_button.Bind(EVT_BUTTON, send_message)
    frame.Show(True)
    return app

def connect_user():
    text_to_file(get_keytext(), KEY_TEXT_FILE)
    text_to_file(create_certificate(), CERT_TEXT_FILE)
    app = create_chat_window()
    gui_string = GUI_String_Ext(text_display)
    global user
    user = Waldo.stcp_connect(User, HOSTNAME, 6922, name, gui_string, key = KEY_TEXT_FILE, cert = CERT_TEXT_FILE)
    text_display.AppendText("You have been added to the chat server.\n")
    user.add_to_server(False)
    app.MainLoop()

    

def read_command(message):
    if message.startswith('quit'):
        user.quit()
        text_display.AppendText('You have left the chatserver.\n')
        exit(0)

    elif message.startswith('private'):
       new_start = len('private ')
       new_message = message[new_start:]
       if (new_message == ""):
           text_display.AppendText('Username must be specified.\n')
       else:
           split_message = new_message.partition(' ')#split_message now contains the tuple (username,' ',message) 
           user.private_message(split_message[0], split_message[2]);#Make this block a foreign function to move to waldo code

    elif message.startswith('users_list'):
       user.print_users()

    elif message.startswith('anagram_game'):
        anagram_player = AnagramPlayer(name)
        text_display.AppendText('You have entered the anagram waiting room.')
        anagram_player.read_waiting_room_commands()                

    elif message.startswith('h'):
        text_display.AppendText('Commands:\n\t/quit - to leave the chatroom.\n\t/private [username] [message] - to send a private message.\n\t/users_list - to see a list of users.\n\t/anagram_game - to enter the anagram game.')

    else:
       text_display.AppendText("Invalid command. Type /h for a list of commands.")

def send_message(event):
    message = str(text_input.GetValue() + "\n")
    text_input.Clear()
    if len(message) > 0 and message[0] is "/":
        message = message[1:]
        read_command(message)
    else:
        user.send_message(message)

if __name__ == '__main__':
    name = raw_input('ENTER YOUR NAME: ')
    connect_user()
