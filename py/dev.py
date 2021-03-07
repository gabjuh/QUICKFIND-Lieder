from colorama import init
from colorama import Fore as F
from colorama import Back as B
from colorama import Style
from termcolor import colored

# def color(fore='', back='', text=''):
#     return f'{fore}{back}{text}{Style.RESET_ALL}'

# print(color(F.GREEm, B.BLUE, 'Hello!'))

init()

print(F.YELLOW + '?: ' + Style.RESET_ALL, end="")
word = input()

print(colored('BLABLA', 'green'))
print(colored('BLABLA', 'red'))

