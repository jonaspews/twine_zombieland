#!/usr/bin/env python
# -*- coding: utf-8 -*-

# UTF8 encoding seems to be needed because some city names have special characters
# TODO: think about out sourcing list to seperate file ... so far that works better

from list_of_cities import cities  # cities is a very long list, kept seperate for easier programming
import random
import time
from datetime import date

'''
TWINE-syntax
(if: $size is 'giant')[
    an intimidating rumble!
](else-if: $size is 'big')[
    a loud growl
](else:​)[
    a faint gurgle
]

**********************

(set: $code to (prompt: "what is your code:", "code"))
(set: $jumpCodes to (a: "1","2","3"))

Your stomach makes {
(if: $code is in $jumpCodes)[
    gesprungen nach [[test1]]
](else-if: $code is '9')[
    megacheat9 [[test2]]
](else:)[
    nix
]}.



'''

# list of levels, change names and number of levels to your needs
level_names = ['level1', 'level2', 'level3', 'level4']

def create_twine_syntax_arrays():
    print('<!-- Syntax created on ' + str(date.today()) +' -->')
    print('(set: $code to (prompt: "what is your code:", "code"))')  # create syntax for TWINE user prompt
    # create syntax for TWINE jumpCode arrays
    # for every level there needs to be an array (a: ...) which collects all the codes for every player for
    # a certain level
    for h in level_names:
        syntax_string = '(set: $jumpCodes_' + str(h) + ' to (a: '
        for i in dict_of_players:
            jumpcode = random.randrange(1000000, 1000000000, 1)  # TODO: needs checking whether jumpcode already exists
            syntax_string = syntax_string + "\"" + str(jumpcode) + "\","
            # TODO: add timestamp if CSV and TWINE syntax
            # TODO: also store this info in an pair/array for creation of CSV
            dict_of_players[i].append(jumpcode)
        syntax_string = syntax_string[:-1] + "))"
        print(syntax_string)

def create_twine_syntax_if():
    print('Let\'s see {')
    for h in level_names:
        print('(if: $code is in $jumpcodes_' + str(h) + ')[')
        print('    gesprungen nach [[' + str(h) + ']]')
        print(']')
    print('(else:)[')
    print('    You cannot cheat Zombies! You are dead!!!')
    print(']}')

def create_gameplan():
    print(dict_of_players)

# list of player names, keep empty here, is filled in main program
dict_of_players = {}
c = False
number_players = int(input('Wie viele Spieler//How many players: '))

for j in range(number_players):
    player_names = cities[int(random.randrange(0, len(cities), 1))]
    print(player_names)
    while c == False:
        if player_names in dict_of_players:
            player_names = cities[int(random.randrange(0, len(cities), 1))]
        else:
            c = True
    dict_of_players[player_names] = []

print('')
create_twine_syntax_arrays()
print('')
create_twine_syntax_if()
print('')
create_gameplan()
