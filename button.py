from ursina import *


class Etudiant:
    def __init__(self, name):
        self.name = name

    def presentation(self):
        print(self.name)


def update():
    if held_keys['escape']:
        exit()


batiste = Etudiant('Batiste')

app = Ursina()

b = Entity(model='quad', collider='box', scale=.1, parent=camera.ui,
           color=color.red, on_click=batiste.presentation)

app.run()
