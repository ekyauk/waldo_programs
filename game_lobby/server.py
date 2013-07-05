from user_emitted import User
from user_emitted import UserHelper
from server_emitted import Server
import sys
import os
sys.path.append(os.path.join("../../"))
from waldo.lib import Waldo
import time
HOSTNAME = '127.0.0.1'

def print_message (endpoint, message):
    print message

if __name__ == '__main__':
    server = Waldo.no_partner_create(Server)
    print 'Server created!'
    Waldo.tcp_accept(UserHelper, HOSTNAME, 6922, server)
    while True:
        time.sleep(2)
