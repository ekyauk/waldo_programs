from player_emitted import PlayerHelper
from anagram_server_emitted import AnagramServer
import sys
import os
sys.path.append(os.path.join("../"))
from waldo.lib import Waldo
import time
import random
HOSTNAME = '127.0.0.1'
PLAYER_NUM = 2
GAMETIME = 60
FILENAME = 'solutions.txt'
SOLUTION_START_INDEX = 1

global solution_set

def print_message (endpoint, message):
    print message

def load_solutions():
    solution_file = open(FILENAME, 'r', 0)
    solutions = solution_file.read().splitlines()
    solution_file.close()
    anagram = ""
    solution = []
    global solution_set
    solution_set = {}
    for line in solutions:
        if line == "":
            solution_set[anagram] = solution
            solution = []
        elif line.startswith('--'):
            anagram = line[2:].upper()
        else:
            solution.append(line.upper())

def set_solutions(game_server):
    anagram = random.choice([key for key in solution_set])
    solutions = solution_set[anagram]
    game_server.set_solution(anagram, solutions)


if __name__ == '__main__':
    anagram_server = Waldo.no_partner_create(AnagramServer)
    print 'GameServer created!'
    Waldo.tcp_accept(PlayerHelper, 'localhost', 6767, anagram_server)
    while True:
        print 'Waiting for 3 players....'
        while anagram_server.get_player_count() != PLAYER_NUM:
            time.sleep(2)
        anagram_server.broadcastMessage('There are three players.  Game will begin in 3 seconds...')
        load_solutions()
        set_solutions(game_server)
        time.sleep(3)
        anagram_server.broadcastMessage('Game begins!')
        anagram_server.start_game()
        time.sleep(GAMETIME)
        anagram_server.end_game()
    
