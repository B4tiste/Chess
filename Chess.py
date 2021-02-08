# -*- coding: utf-8 -*-
"""
Chess game code

github.com/B4tiste/TargetHunter

@author: B4tiste
"""

# from ursina import *  # Import all the Ursina lib
import random
import time
import os
import numpy as np


def clear(): return os.system('cls')


class Pion_w:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand


class Pion_b:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand


class Tour_w:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand


class Tour_b:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand


class Cav_w:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand


class Cav_b:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand


class Fou_w:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand


class Fou_b:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand


class Reine_w:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand


class Reine_b:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand


class Roi_w:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand


class Roi_b:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand


p_b_1 = Pion_b('Pb1', 1, 0, 1)
p_b_2 = Pion_b('Pb2', 1, 1, 1)
p_b_3 = Pion_b('Pb3', 1, 2, 1)
p_b_4 = Pion_b('Pb4', 1, 3, 1)
p_b_5 = Pion_b('Pb5', 1, 4, 1)
p_b_6 = Pion_b('Pb6', 1, 5, 1)
p_b_7 = Pion_b('Pb7', 1, 6, 1)
p_b_8 = Pion_b('Pb8', 1, 7, 1)

p_w_1 = Pion_b('Pw1', 1, 0, 1)
p_w_2 = Pion_b('Pw2', 1, 1, 1)
p_w_3 = Pion_b('Pw3', 1, 2, 1)
p_w_4 = Pion_b('Pw4', 1, 3, 1)
p_w_5 = Pion_b('Pw5', 1, 4, 1)
p_w_6 = Pion_b('Pw6', 1, 5, 1)
p_w_7 = Pion_b('Pw7', 1, 6, 1)
p_w_8 = Pion_b('Pw8', 1, 7, 1)

t_b_1 = Tour_b('Tb1', 0, 0, 1)
t_b_2 = Tour_b('Tb2', 0, 7, 1)

t_w_1 = Tour_w('Tw1', 7, 0, 1)
t_w_2 = Tour_w('Tw2', 7, 7, 1)

cav_b_1 = Cav_b('Cavb1', 0, 1, 1)
cav_b_2 = Cav_b('Cavb2', 0, 6, 1)

cav_w_1 = Cav_w('Cavw1', 7, 1, 1)
cav_w_2 = Cav_w('Cavw1', 7, 6, 1)

fou_b_1 = Fou_b('Foub1', 0, 2, 1)
fou_b_2 = Fou_b('Foub2', 0, 5, 1)

fou_w_1 = Fou_w('Fouw1', 7, 2, 1)
fou_w_2 = Fou_w('Fouw1', 7, 5, 1)

reine_b = Reine_b('Reineb', 0, 3, 1)

reine_w = Reine_w('Reinew', 7, 3, 1)

roi_b = Roi_b('Roib', 0, 4, 1)

roi_w = Roi_w('Roiw', 7, 4, 1)

pions_b = [p_b_1, p_b_2, p_b_3, p_b_4, p_b_4, p_b_6, p_b_7, p_b_8]
pions_w = [p_w_1, p_w_2, p_w_3, p_w_4, p_w_4, p_w_6, p_w_7, p_w_8]

pieces_b = [t_b_1, cav_b_1, fou_b_1, reine_b, roi_b, fou_b_2, cav_b_2, t_b_2]
pieces_w = [t_w_1, cav_w_1, fou_w_1, reine_w, roi_w, fou_w_2, cav_w_2, t_w_2]


# Change this value according to your screen refresh rate (60Hz for instance):
REFRESH_RATE = 60

echiquier = [[0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0]]

echiquier_start = [pieces_b,
                   pions_b,
                   [0, 1, 0, 1, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 0],
                   [0, 1, 0, 1, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 0],
                   pions_w,
                   pieces_w]

for y in range(8):
    for x in range(8):
        try :
            print(echiquier_start[y][x].name)
        except :
            print(echiquier_start[y][x])


# def update():


# app = Ursina()


# app.run()
