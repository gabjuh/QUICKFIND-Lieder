from colorama import init
from colorama import Fore as F
from colorama import Back as B
from colorama import Style
from termcolor import colored

# def color(fore='', back='', text=''):
#     return f'{fore}{back}{text}{Style.RESET_ALL}'

# print(color(F.GREEm, B.BLUE, 'Hello!'))

init()

# print(F.YELLOW + '?: ' + Style.RESET_ALL, end="")
# word = input()

# print(colored('BLABLA', 'green'))
# print(colored('BLABLA', 'red'))

def colorInput(txt):
    print(F.YELLOW + txt + Style.RESET_ALL, end="")
    return input()
    

def printGreen(txt):
    print(colored(txt, 'green'))
    

def printRed(txt):
    print(colored(txt, 'red'))


def printYellow(txt):
    print(colored(txt, 'yellow'))



