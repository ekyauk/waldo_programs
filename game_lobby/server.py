from user_emitted import User
from user_emitted import UserHelper
from server_emitted import Server
import sys, os, time
import OpenSSL
from OpenSSL import crypto
import ssl
sys.path.append(os.path.join("../../"))
from waldo.lib import Waldo
HOSTNAME = '127.0.0.1'

def print_message (endpoint, message):
    print message

if __name__ == '__main__':
    server = Waldo.no_partner_create(Server)
    print 'Server created!'
    Waldo.stcp_accept(UserHelper, HOSTNAME, 6922, server, ca_req = ssl.CERT_REQUIRED, ca_certs = "ca_list.pem")
    while True:
        time.sleep(2)
