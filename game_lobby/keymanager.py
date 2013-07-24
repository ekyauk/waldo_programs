#!/usr/bin/env python

import os,sys, Queue, time
base_dir = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), '..','..')
sys.path.append(base_dir)
from waldo.lib import Waldo
from optparse import OptionParser

KEY_MANAGER_HOST = '127.0.0.1'
KEY_MANAGER_PORT = 6974


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-g", "--generate", action ="store_true", dest = "generate", default = False)
    (option, args) = parser.parse_args()
    Waldo.start_ca(option.generate, host = KEY_MANAGER_HOST, port = KEY_MANAGER_PORT, cert_end = 60*60*24*365)
    if option.generate:
        Waldo.add_ca_to_list("ca_list.pem", KEY_MANAGER_HOST, KEY_MANAGER_PORT)
    while True:
        time.sleep(5)



