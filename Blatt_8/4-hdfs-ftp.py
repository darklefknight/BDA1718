#!/usr/bin/env python3

# use it on cluster otherwise you need password...

import requests

def read_test():
    # reading
    ## via url
    # curl -i -L "http://abu2:50070/webhdfs/v1/user/burgemeister/test.txt?op=OPEN&user.name=burgemeister"
    print("S1")
    url = 'http://10.0.0.62:50070/webhdfs/v1/user/burgemeister/test.txt?op=OPEN'
    r = requests.get(url)
    print("S2")
    print(r)
    print(r.text)

def run_cmd(cmd):
    """Translate command into REST API call and process the response."""
    pass

def repl():
    while True:
        try:
            cmd = input('>>> ')
        except EOFError:
            print('exit')
            break
        if cmd in ['exit', 'bye']:
            break
        elif cmd == '':
            continue
        else:
            run_cmd(cmd)

if __name__ == '__main__':

    read_test()
    repl()