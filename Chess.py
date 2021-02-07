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


pb1 = Pion_b('Pb1', 1, 0, 1)
pb2 = Pion_b('Pb2', 1, 1, 1)
pb3 = Pion_b('Pb3', 1, 2, 1)
pb4 = Pion_b('Pb4', 1, 3, 1)
pb5 = Pion_b('Pb5', 1, 4, 1)
pb6 = Pion_b('Pb6', 1, 5, 1)
pb7 = Pion_b('Pb7', 1, 6, 1)
pb8 = Pion_b('Pb8', 1, 7, 1)

pw1 = Pion_b('Pw1', 1, 0, 1)
pw2 = Pion_b('Pw2', 1, 1, 1)
pw3 = Pion_b('Pw3', 1, 2, 1)
pw4 = Pion_b('Pw4', 1, 3, 1)
pw5 = Pion_b('Pw5', 1, 4, 1)
pw6 = Pion_b('Pw6', 1, 5, 1)
pw7 = Pion_b('Pw7', 1, 6, 1)
pw8 = Pion_b('Pw8', 1, 7, 1)


pions_w = [pw1, pw2, pw3, pw4, pw4, pw6, pw7, pw8]
pions_b = [pb1, pb2, pb3, pb4, pb4, pb6, pb7, pb8]


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

echiquier_start = [['Tb', 'Cb', 'Fb', 'Db', 'Rb', 'Fb', 'Cb', 'Tb'],
                   ['Pb1', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
                   [0, 1, 0, 1, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 0],
                   [0, 1, 0, 1, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 0],
                   ['Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw'],
                   ['Tw', 'Cw', 'Fw', 'Dw', 'Rw', 'Fw', 'Cw', 'Tw']]

print(np.matrix(echiquier))
print('\n')
print(np.matrix(echiquier_start))
print(echiquier_start[1][0])


# def update():


# app = Ursina()


# app.run()
