# -*- coding: utf-8 -*-
"""
Chess game code

github.com/B4tiste/TargetHunter

@author: B4tiste
"""

from ursina import *  # Import all the Ursina lib
# from lib_chess import *
import random
import time
import os
import numpy as np


class Pion_w:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand

    def show_move():
        print("a")
        echiquier.children[mouse.hovered_entity.coord[0]
                           ][mouse.hovered_entity.coord[1]].color = color.green


class Pion_b:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand

    def show_move():
        echiquier.children[mouse.hovered_entity.coord(
            0)][mouse.hovered_entity.coord(1)].color = color.red


class Tour_w:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand

    def show_move():
        echiquier.children[mouse.hovered_entity.colums][mouse.hovered_entity.lines +
                                                        1].color = color.green


class Tour_b:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand

    def show_move():
        echiquier.children[mouse.hovered_entity.colums][mouse.hovered_entity.lines +
                                                        1].color = color.green


class Cav_w:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand

    def show_move():
        echiquier.children[mouse.hovered_entity.colums][mouse.hovered_entity.lines +
                                                        1].color = color.green


class Cav_b:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand

    def show_move():
        echiquier.children[mouse.hovered_entity.colums][mouse.hovered_entity.lines +
                                                        1].color = color.green


class Fou_w:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand

    def show_move():
        echiquier.children[mouse.hovered_entity.colums][mouse.hovered_entity.lines +
                                                        1].color = color.green


class Fou_b:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand

    def show_move():
        echiquier.children[mouse.hovered_entity.colums][mouse.hovered_entity.lines +
                                                        1].color = color.green


class Reine_w:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand

    def show_move():
        echiquier.children[mouse.hovered_entity.colums][mouse.hovered_entity.lines +
                                                        1].color = color.green


class Reine_b:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand

    def show_move():
        echiquier.children[mouse.hovered_entity.colums][mouse.hovered_entity.lines +
                                                        1].color = color.green


class Roi_w:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand

    def show_move():
        echiquier.children[mouse.hovered_entity.colums][mouse.hovered_entity.lines +
                                                        1].color = color.green


class Roi_b:
    def __init__(self, name, lines, colums, stand):
        self.name = name
        self.lines = lines
        self.colums = colums
        self.stand = stand

    def show_move():
        echiquier.children[mouse.hovered_entity.colums][mouse.hovered_entity.lines +
                                                        1].color = color.green


class case_vide:
    def __init__(self, name, lines, colums):
        self.name = name
        self.lines = lines
        self.colums = colums

    def show_move():
        print('')


def clear(): return os.system('cls')


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
fou_w_2 = Fou_w('Fouw2', 7, 5, 1)

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

TEXT_CASE_VIDE = ' '
c = (0, 0)
cpt = 0

window.borderless = False

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
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   pions_w,
                   pieces_w]

'''
for y in range(8):
    for x in range(8):
        try:
            print(echiquier_start[y][x].name)
        except:
            print(echiquier_start[y][x])'''


ech_display_string = [['Tb', 'Cb', 'Fb', 'Db', 'Rb', 'Fb', 'Cb', 'Tb'],
                      ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
                      ['0', '1', '0', '1', '0', '1', '0', '1'],
                      ['1', '0', '1', '0', '1', '0', '1', '0'],
                      ['0', '1', '0', '1', '0', '1', '0', '1'],
                      ['1', '0', '1', '0', '1', '0', '1', '0'],
                      ['Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw'],
                      ['Tw', 'Cw', 'Fw', 'Dw', 'Rw', 'Fw', 'Cw', 'Tw']]


def available_move():

    global c

    echiquier.children[((c[1] * 8) + c[0]) + 8].color = color.red


def reset_show():

    global echiquier
    global c

    print('reset')

    for lignes in range(8):
        for colonnes in range(8):
            x = lignes % 2
            y = colonnes % 2
            if x == 1:
                if y == 1:
                    try:
                        echiquier.children[(lignes * 8) + colonnes
                                           ].color = color.dark_gray
                    except:
                        echiquier.children[(lignes * 8) + colonnes
                                           ].color = color.dark_gray
                elif y == 0:
                    try:
                        echiquier.children[(lignes * 8) + colonnes
                                           ].color = color.gray
                    except:
                        echiquier.children[(lignes * 8) + colonnes
                                           ].color = color.gray
            elif x == 0:
                if y == 1:
                    try:
                        echiquier.children[(lignes * 8) + colonnes
                                           ].color = color.gray
                    except:
                        echiquier.children[(lignes * 8) + colonnes
                                           ].color = color.gray
                elif y == 0:
                    try:
                        echiquier.children[(lignes * 8) + colonnes
                                           ].color = color.dark_gray
                    except:
                        echiquier.children[(lignes * 8) +
                                           colonnes].color = color.dark_gray


def update():

    global cpt
    global c

    if cpt == 60:
        cpt = 0
    else:
        cpt = cpt + 1

    if held_keys['escape']:
        exit()
    if held_keys['c']:
        print(camera.position)

    if held_keys['r']:
        reset_show()

    if (cpt % 30) == 0:
        try:
            c = mouse.hovered_entity.coord
            print(c)
            # print(echiquier.children[(c[1] * 8) + c[0]].text)

            print_on_screen(
                'Colonne : ' + str(mouse.hovered_entity.coord[0]+1) + '\n' + 'Ligne : ' + str(mouse.hovered_entity.coord[1]+1))
            # print(mouse.hovered_entity.color)

            if mouse.hovered_entity.text != ' ':
                available_move()
            else:
                reset_show()
        except:
            reset_show()


app = Ursina()

# grid = Entity(model=Grid(8, 8))

'''
    echiquier -> Plateau
    case -> Children de echiquier
    echiquier.children -> Tableau de case
'''

echiquier = Entity()

for l in range(8):
    for c in range(8):
        x = l % 2
        y = c % 2
        if x == 1:
            if y == 1:
                try:
                    case = Button(parent=echiquier, model='quad', scale=Vec2(.1, .1), text=echiquier_start[l][c].name, coord=(
                        c, l), color=color.dark_gray, on_click=print(echiquier_start[l][c].name))
                except:
                    case = Button(parent=echiquier, model='quad', scale=Vec2(.1, .1),
                                  text=TEXT_CASE_VIDE, coord=(c, l), color=color.dark_gray, on_click=print(TEXT_CASE_VIDE))
            elif y == 0:
                try:
                    case = Button(parent=echiquier, model='quad', scale=Vec2(.1, .1),
                                  text=echiquier_start[l][c].name, coord=(c, l), color=color.gray, on_click=print(echiquier_start[l][c].name))
                except:
                    case = Button(parent=echiquier, model='quad', scale=Vec2(.1, .1),
                                  text=TEXT_CASE_VIDE, coord=(c, l), color=color.gray, on_click=print(TEXT_CASE_VIDE))
        elif x == 0:
            if y == 1:
                try:
                    case = Button(parent=echiquier, model='quad', scale=Vec2(.1, .1),
                                  text=echiquier_start[l][c].name, coord=(c, l), color=color.gray, on_click=print(echiquier_start[l][c].name))
                except:
                    case = Button(parent=echiquier, model='quad', scale=Vec2(.1, .1),
                                  text=TEXT_CASE_VIDE, coord=(c, l), color=color.gray, on_click=print(TEXT_CASE_VIDE))
            elif y == 0:
                try:
                    case = Button(parent=echiquier, model='quad', scale=Vec2(.1, .1),
                                  text=echiquier_start[l][c].name, coord=(c, l), color=color.dark_gray, on_click=print(echiquier_start[l][c].name))
                except:
                    case = Button(parent=echiquier, model='quad', scale=Vec2(.1, .1),
                                  text=TEXT_CASE_VIDE, coord=(c, l), color=color.dark_gray, on_click=print(TEXT_CASE_VIDE))
        case.text_entity.scale = 0.5

grid_layout(echiquier.children, max_x=8, max_y=8,
            origin=(0, .5), spacing=(.15, 0))

# EditorCamera()

camera.position = (0, -0.4, -2)

print("TEST")
print(echiquier.children[8].text)
print("TEST")

app.run()
