from ursina import *
import numpy as np

ech_display = [['Tb', 'Cb', 'Fb', 'Db', 'Rb', 'Fb', 'Cb', 'Tb'],
               ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
               ['0', '1', '0', '1', '0', '1', '0', '1'],
               ['1', '0', '1', '0', '1', '0', '1', '0'],
               ['0', '1', '0', '1', '0', '1', '0', '1'],
               ['1', '0', '1', '0', '1', '0', '1', '0'],
               ['Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw'],
               ['Tw', 'Cw', 'Fw', 'Dw', 'Rw', 'Fw', 'Cw', 'Tw']]


def update():
    if held_keys['escape']:
        exit()
    '''if held_keys['a']:
        grid.texture = white_cube'''


app = Ursina()

# grid = Entity(model=Grid(8, 8))
# EditorCamera()

# center = Entity(model='quad', scale=.1, color=color.red)
p = Entity()
for lines in range(8):
    for colums in range(8):
        x = lines % 2
        y = colums % 2
        if x == 1:
            if y == 1:
                b = Button(parent=p, model='quad', scale=Vec2(.1, .1),
                           text=ech_display[lines][colums], color=color.dark_gray)
            elif y == 0:
                b = Button(parent=p, model='quad', scale=Vec2(.1, .1),
                           text=ech_display[lines][colums], color=color.gray)
        elif x == 0:
            if y == 1:
                b = Button(parent=p, model='quad', scale=Vec2(.1, .1),
                           text=ech_display[lines][colums], color=color.gray)
            elif y == 0:
                b = Button(parent=p, model='quad', scale=Vec2(.1, .1),
                           text=ech_display[lines][colums], color=color.dark_gray)
        b.text_entity.scale = 1
# t = time.time()
grid_layout(p.children, max_x=8, max_y=8, origin=(0, .5), spacing=(.15, 0))
center = Entity(parent=camera.ui, model=Circle(), scale=.005, color=color.lime)
# EditorCamera()
# print(time.time() - t)

app.run()
