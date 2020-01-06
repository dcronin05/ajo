import sys
from fileread import *
from say import Say
if __name__ == '__main__':
    file = FileRead(sys.argv[1])
    for command in file.COMMANDS:
        if 'say' in command:

            Say(command)