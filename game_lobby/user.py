from user_emitted import User
from server_emitted import Server
from player_emitted import Player
import sys
import os
sys.path.append(os.path.join("../../"))
from waldo.lib import Waldo
import time
import random
HOSTNAME = '127.0.0.1'
WORD_MIN = 3
WORD_MAX = 7
global user
global player
global name

def shuffle_anagram(anagram):
    for i in anagram:
        rand_int = random.randint(0, len(anagram) - 1)
        temp = anagram[rand_int]
        anagram = anagram.replace(temp, i, 1)
        anagram = anagram.replace(i, temp, 1)
    return anagram

def enter_anagram_lobby():
    global player
    player = Waldo.tcp_connect(Player, 'localhost', 6767, name, print_message)
    player.add_to_server()
    user.quit(True)
    
def wait_in_lobby():
    print 'Waiting for more players...'
    while(not player.game_in_session()):
        time.sleep(1)

def play_game():
    anagram = player.get_anagram()
    solutions = player.get_solutions()
    used_words = []
    while player.game_in_session():
        answer = raw_input("%s: " %anagram).upper()
        if not player.game_in_session:
            break
        if len(answer) > 0 and answer[0] == "/":
            command = answer[1:]
            if command == 'SHUFFLE':
               anagram = shuffle_anagram(anagram)
            else:
                print 'Invalid game command. \n     /shuffle - shuffles anagram'

        elif len(answer) <= WORD_MAX and len(answer) >= WORD_MIN:
            if answer in used_words:
                print '%s was already used.' %answer
            elif answer in solutions:
                used_words.append(answer)
                player.add_points(len(answer))
            else:
                print '%s is an invalid word.' %answer
        else:
            print "Word is not between 3 and 7 letters."
    print 'Remaining answers:'
    for answer in solutions:
        if answer not in used_words: 
            print answer
            

def print_message(endpoint, message):
    print message

def connect_user(name):
    global user
    user = Waldo.tcp_connect(User, HOSTNAME, 6922, name, print_message)
    user.add_to_server(False);
    print 'You have been added to the chatserver.'

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
        enter_anagram_lobby()
        while True:
            wait_in_lobby()
            play_game()
            response = raw_input('Enter \'yes\' to play again. ')
            if response != 'yes':
                break
            player.add_to_server()
        user.add_to_server(True)
            

    elif message.startswith('h'):
        print 'Commands:'
        print '     /quit - to leave the chatroom.'
        print '     /private [username] [message] - to send a private message.'
        print '     /users_list - to see a list of users.'
        print '     /anagram_game - to enter the anagram game.'

    else:
       print "Invalid command. Type /h for a list of commands."

def send_message(name):
    while True:
        message = raw_input()
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
