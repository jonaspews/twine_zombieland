#!/usr/bin/env python
# -*- coding: utf-8 -*-

# UTF8 encoding seems to be needed because some city names have special characters
# TODO: think about out sourcing list to seperate file ... so far that works better

from list_of_cities import cities  # cities is a very long list, kept seperate for easier programming
import random  # needed to create random codes
# import time  # TODO: delete later, if not needed
from datetime import date  # needed for time stamp in CSV
import csv  # needed for CSV-file manipulation
import sys  # needed for try/exception

# *****************************************************
# *                                                   *
# * Function: create TWINE syntax for jumpcode-arrays *
# * ************************************************* *
# *****************************************************

# example for TWINE syntax for arrays (with prompt for USER):

# (set: $code to (prompt: "what is your code:", "code"))
# (set: $jumpCodes to (a: "1","2","3"))


def create_twine_syntax_arrays():
    print('<!-- ************************************ -->')
    print('<!-- for TWINE-syntax: start copying here -->')
    print('<!-- Syntax created on ' + str(date.today()) +' -->')  # create TWINE syntax for diplaying date when rest of syntax for the specific game was created
    print('(set: $code to (prompt: "what is your code:", "code"))')  # create syntax for TWINE user prompt
    # create syntax for TWINE jumpCode arrays
    # for every level there needs to be an array (a: ...) which collects all the codes for every player for
    # a certain level
    for h in level_names:
        syntax_string = '(set: $jumpCodes_' + str(h) + ' to (a: '
        for i in dict_of_players:
            # create random jumpcodes for each level
            jumpcode = random.randrange(1000000, 1000000000, 1)  # TODO: needs checking whether jumpcode already exists
            syntax_string = syntax_string + "\"" + str(jumpcode) + "\","
            dict_of_players[i].append(jumpcode)  # store jumpcodes in python-dict for each player, used for CSV-writing
        syntax_string = syntax_string[:-1] + "))"  # delete last comma from string
        print(syntax_string)

# ***************************************************
# *                                                 *
# * Function: create TWINE syntax for if-statements *
# * *********************************************** *
# ***************************************************

# example for TWINE syntax for if-statements:

# Your stomach makes {
# (if: $code is in $jumpCodes)[
#     gesprungen nach [[test1]]
# ](else-if: $code is '9')[
#     megacheat9 [[test2]]
# ](else:)[
#     nix
# ]}.


def create_twine_syntax_if():
    print('Let\'s see {')
    for h in level_names:
        print('(if: $code is in $jumpCodes_' + str(h) + ')[')  # TODO: this needs to be if-else
        print('    gesprungen nach [[' + str(h) + ']]')
        print(']')
    print('(else:)[')
    print('    You cannot cheat Zombies! You are dead!!!')
    print(']}')

# ************************************************
# *                                              *
# * Function: create gameplan as CSV for teacher *
# * ******************************************** *
# ************************************************


def create_gameplan():
    print(dict_of_players)
    try:
        csvfile = open("zombieland_gameplan.csv")
    except:
        print("Datei nicht vorhanden!")
        sys.exit(0)

    with open('zombieland_gameplan.csv', 'w', newline='') as empty_gameplan:
        headers = ['date',
                    'student',
                     'class',
                      'playername',
                       'code_level1',   # number of levels must fit number of levels in level_names list (main part)
                        'code_level2',
                          'code_level3',
                            'code_level4']
        csvwriter = csv.DictWriter(empty_gameplan, fieldnames=headers)
        csvwriter.writeheader()
        for i in dict_of_players:
            csvwriter.writerow({'date': date.today(),
                                'student': '',
                                'class': '',
                                'playername': i,
                                'code_level1': (dict_of_players[i])[0],
                                'code_level2': (dict_of_players[i])[1],
                                'code_level3': (dict_of_players[i])[2],
                                'code_level4': (dict_of_players[i])[3]})

# *****************
# *****************
# *!! MAIN PART !!*
# *****************
# *****************

# list of levels, change names and number of levels to your needs
level_names = ['level1', 'level2', 'level3', 'level4']
# list of player names, keep empty here, is filled in main program
dict_of_players = {}
# variable for while-loop
c = False

# prompt gamemaster (== teacher) how many students will play game
number_players = int(input('Wie viele Spieler//How many players: '))

for j in range(number_players):
    player_names = cities[int(random.randrange(0, len(cities), 1))]
    print(player_names)
    while c == False:
        if player_names in dict_of_players:
            player_names = cities[int(random.randrange(0, len(cities), 1))]
        else:
            c = True
    dict_of_players[player_names] = []  # add key(player_name)-vlaue(empty)-pair to dictionary

print('')
create_twine_syntax_arrays()  # TODO: think about copying this directly in twine-HTML?!?! oder extra text-file
print('')
create_twine_syntax_if()    # TODO: think about copying this directly in twine-HTML?!?! oder extra text-file
print('<!-- for TWINE-Syntax: stop copy here -->')
print('<!-- ******************************** -->')
create_gameplan()
