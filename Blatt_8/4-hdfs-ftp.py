#!/usr/bin/env python3
import requests

def read_test():
    # reading
    ## via url
    url = 'http://10.0.0.61:50070/webhdfs/v1/user/gresens/data?op=OPEN'
    r = requests.get(url)
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