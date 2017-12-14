#!/usr/bin/env python3

# use it on cluster otherwise you need password...

import requests
import getpass

# set initial path
user_name = getpass.getuser()
path = 'http://10.0.0.62:50070/webhdfs/v1/user/' + user_name + '/'


def run_cmd(cmd):
    """Translate command into REST API call and process the response.
        :param cmd: String: command
    """
    split = cmd.split(" ")
    
    if len(split)==1:
        com = cmd
    elif len(split)==2:
        com, par = cmd.split(" ")
    else:
        print("ERROR COMMAND")
    
    if com == 'pwd':
        get_dir()
    elif com == 'chdir':
        change_dir(par)
    elif com == 'ls':
        list_dir()
    #elif com == 'put':
    #    put_file(par)
    #elif com == 'get':
    #    read_file(par)
    #elif com == 'mkdir':
    #    make_dir()
    #elif com == 'rmdir':
    #    remove_()
    #elif com == 'rm':
    #    remove_file()
    else:
        'TRY pwd. chdir, ls [parameterstring]'


def repl():
    """Input control."""
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


def get_dir():
    """List directory"""
    print(path.replace(('http://10.0.0.62:50070/webhdfs/v1/user/'+user_name),''))


def change_dir(par):
    """Change directory
        :param String: absolute path
    """
    if par[0] == '/':
        new_path = 'http://10.0.0.62:50070/webhdfs/v1/user/' + user_name + par
        if file_exists(new_path):
            path = new_path
        else:
            print('DIRECTORY DOES NOT EXIST')
    else:
        print('NEED ABSOLUTE PATH')


def file_exists(loc):
    """Check if file exists
        :param String: absolute location with url
    """
    url = loc + '?op=GETFILESTATUS'

    r = requests.get(url)

    if r.status_code == 200:
        return True
    else:
        return False


def list_dir(loc):
    """List direcotry
        :param String: absolute location with url
    """
    url = loc + '?op=LISTSTATUS'

    r = requests.get(url)


if __name__ == '__main__':
    #get_dir()
    #file_exists('http://abu2:50070/webhdfs/v1/user/burgemeister/test.txt?op=OPEN&user.name=burgemeister')
    #main()
    #read_test()
    repl()

