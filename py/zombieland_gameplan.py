#!/usr/bin/env python
# -*- coding: utf-8 -*-

# UTF8 encoding seems to be needed because some city names have special characters
# TODO: think about out sourcing list to seperate file

from list_of_cities import cities  # cities is a very long list, kept seperate for easier programming

# print(cities)

import random

number_players = int(input('Wie viele Spieler//How many players: '))

for i in range(number_players):
    print(cities[int(random.randrange(0,len(cities),1))])
