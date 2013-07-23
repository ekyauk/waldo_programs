from user_login_emitted import UserLoginHelper
from user_emitted import UserHelper
from server_emitted import Server
from password_server_emitted import PasswordServer
import sys, os, time
from login import LoginWindow
import OpenSSL
from OpenSSL import crypto
import ssl
sys.path.append(os.path.join("../../"))
from waldo.lib import Waldo
HOSTNAME = '127.0.0.1'
PORT = 6922
FILENAME = 'database.txt'
database = {}
STRUCT_FIELD_ONE = "password"
STRUCT_FIELD_TWO = "encryptKey"
STRUCT_FIELD_THREE = "cert"
STRUCT_FIELD_FOUR = "salt"
SEP = "(--^^--)\n"
USER_SEP = "\n----------END USER----------\n\n----------BEGIN USER----------"


def load_database():
    database_file = open(FILENAME, 'r', 0)
    users = database_file.read().split(USER_SEP)
    for line in users:
        if (len(line) > 0):
            split_line = line.split(SEP)
            global database
            user_info = {}
            user_info[STRUCT_FIELD_ONE] = split_line[1]
            user_info[STRUCT_FIELD_TWO] = split_line[2]
            user_info[STRUCT_FIELD_THREE] = split_line[3]
            user_info[STRUCT_FIELD_FOUR] = split_line[4]
            database[split_line[0]] = user_info
    database_file.close()

def save_database(endpoint, user_dict):
    database_file = open(FILENAME, 'w', 0)
    for user in user_dict:
        user_info = user_dict[user]
        line = user + SEP + user_info[STRUCT_FIELD_ONE] + SEP + user_info[STRUCT_FIELD_TWO] + SEP + user_info[STRUCT_FIELD_THREE] + SEP + user_info[STRUCT_FIELD_FOUR] + USER_SEP
        database_file.write(line)
    database_file.close()
    
if __name__ == '__main__':
    load_database()
    server = Waldo.no_partner_create(Server)
    password_server = Waldo.no_partner_create(PasswordServer, database, save_database)
    Waldo.stcp_accept(UserLoginHelper, HOSTNAME, PORT + 1, password_server)
    print 'Server created!'
    Waldo.stcp_accept(UserHelper, HOSTNAME, PORT, server, cert_reqs= ssl.CERT_OPTIONAL, ca_certs = "ca_list.pem")
    while raw_input() != "close": 
        pass
    password_server.close()
