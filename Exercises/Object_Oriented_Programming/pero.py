from math import *

import risar
from risar import stoj

class Turtle:
    def __init__(self):
        self.x, self.y = risar.maxX/2, risar.maxY/2
        self.angle = 0
        self.penActive = True
        self.width = 1
        self.color = risar.bela

        self.pause = 0
        self.body = risar.krog_s(0, 0, 5, risar.zelena, 3)
        self.head = risar.krog_s(0, 0, 2, risar.zelena, 3)
        self.pen = risar.krog_s(0, 0, 2, risar.rumena, 3)  ## DODANO ##
        self.update()
        self.stamps = []

    def update(self):
        self.body.setPos(self.x, self.y)
        phi = radians(90 - self.angle)
        self.head.setPos(self.x + 5 * cos(phi), self.y - 5 * sin(phi))
        risar.obnovi()
        if self.pause:
            self.wait(self.pause)

    def forward(self, a):
        phi = radians(90 - self.angle)
        nx = self.x + a * cos(phi)
        ny = self.y - a * sin(phi)
        if self.pen_active:
            risar.crta(self.x, self.y, nx, ny)
        self.x = nx
        self.y = ny
        self.update()

    def turn(self, phi):
        self.angle += phi
        self.update()

    def backward(self, a):
        self.forward(-a)

    def left(self):
        self.turn(-90)

    def right(self):
        self.turn(90)

    def fly(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.update()

    def pen_up(self):
        self.pen_active = False

    def pen_down(self):
        self.pen_active = True

    def wait(self, s):
        risar.cakaj(s)

    def hide(self):
        self.body.hide()
        self.head.hide()

    def show(self):
        self.body.show()
        self.head.show()

    def set_pause(self, s):
        self.pause = s

    def no_pause(self):
        self.set_pause(0)

    def turnAround(self):
        self.turn(180)

    def __init__(self):
        self.x, self.y = risar.maxX/2, risar.maxY/2
        self.angle = 0
        self.penActive = True
        self.width = 1  ## DODANO ##
        self.color = risar.bela  ## DODANO ##

        self.pause = 0
        self.body = risar.krog(0, 0, 5, risar.zelena, 3)
        self.head = risar.krog(0, 0, 2, risar.zelena, 3)
        self.update()

    def forward(self, l):
        angle = radians(90 - self.angle)
        nx, ny = self.x+l*cos(angle), self.y-l*sin(angle)
        nx, ny = max(0, nx), max(0, ny)
        nx, ny = min(nx, risar.maxX), min(ny, risar.maxY)
        if self.penActive:
            risar.crta(self.x, self.y, nx, ny, self.color, self.width)  ## SPREMENJENO ##
        self.x, self.y = nx, ny
        self.update()

    def setWidth(self, width):  ## NOVA METODA ##
        self.width = width

    def setColor(self, color):  ## NOVA METODA ##
        self.color = color

    def show(self):
        self.body.show()
        self.head.show()
        if self.penActive:  ## DODANO ##
            self.pen.show()  ## DODANO ##

    def hide(self):
        self.body.hide()
        self.head.hide()
        self.pen.hide()  ## DODANO ##

    def penUp(self):
        self.penActive = False
        self.pen.hide()  ## DODANO ##

    def penDown(self):
        self.penActive = True
        if self.head.isVisible():  ## DODANO ##
            self.pen.show()  ## DODANO ##
    
    def stamp(self):
    angle = radians(90 - self.angle)
    body = risar.krog(self.x, self.y, 5, risar.zelena, 3)
    head = risar.krog(self.x+5*cos(angle), self.y-5*sin(angle), 2, risar.zelena, 3)
    self.stamps.append(body)
    self.stamps.append(head)

    def clearStamps(self):
        for stamp in self.stamps:
            stamp.hide()
        self.stamps = []



"""     def stamp(self):
    t = Turtle()
    t.fly(self.x, self.y, self.angle)
    self.stamps.append(t)

    def clearStamps(self):
    for t in self.stamps:
        t.hide()
    self.stamps = [] """

# Testiranje
import turtle

t = turtle.Turtle()
t.hide()
t.penDown()
t.wait()