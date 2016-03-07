import config
from sys import exit
from inspect import getargspec
from collections import OrderedDict

def initialize():
    print('initializing')
    config.command_dict = OrderedDict([('action', action),('change',change),('alter',alter)])

def select_screen():
    print('Selecting screen')

def action():
    print('Doing an action')

def change():
    print('Changing')

def alter():
    print('Altering')

def get_cmd():
    print('Available commands : ', *config.command_dict.keys())
    # Get the main command and store the remainder of input in a list
    cmd = input('What is you command? :')
    cmd, *args = cmd.split(maxsplit=1)

    if cmd == 'end':
        exit()
    elif cmd in config.command_dict:
        # Get the number of arguments that the function of the main command takes
        num_args = len(getargspec(config.command_dict[cmd])[0])

        # Split remainder of input based on number of args
        if len(args) > 0:
            args = args[0].split(maxsplit=num_args-1)

        # Execute command and gracefully fail if given faulty input
        try:
            config.command_dict[cmd](*args)
        except (TypeError, ValueError):
            print('Please format your input properly')
    else:
        print('Please input legitimate command')

if __name__ == "__main__":
    print('Welcome to codename teal')
    initialize()

    while True:
        get_cmd()

    #select_screen()
