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
        self.trace = []  ## DODANO ##

        self.pause = 0
        self.body = risar.krog_s(0, 0, 5, risar.zelena, 3)
        self.head = risar.krog_s(0, 0, 2, risar.zelena, 3)
        self.pen = risar.krog_s(0, 0, 2, risar.rumena, 3)
        self.update()

    def startRecording(self):  ## NOVA METODA ##
        self.trace = []

    def stopRecording(self):  ## NOVA METODA ##
        return self.trace[:]

    def play(self, trace):  ## NOVA METODA ##
        for func, pars in trace:
            func(*pars)

    def forward(self, l):
        angle = radians(90 - self.angle)
        nx, ny = self.x+l*cos(angle), self.y-l*sin(angle)
        nx, ny = max(0, nx), max(0, ny)
        nx, ny = min(nx, risar.maxX), min(ny, risar.maxY)
        if self.penActive:
            risar.crta(self.x, self.y, nx, ny, self.color, self.width)
        self.x, self.y = nx, ny
        self.update()
        self.trace.append((self.forward, (l,)))  ## DODANO ##

    def turn(self, angle):
        self.angle += angle
        self.update()
        self.trace.append((self.turn, (angle,)))  ## DODANO ##

# Testiranje
t = Turtle()
t.startRecording()
for i in range(4):
    t.forward(100)
    t.right()
kvadrat = t.stopRecording()

for i in range(10):
    t.turn(36)
    t.play(kvadrat)
risar.stoj()