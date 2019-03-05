try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import math
import random

from lib.util.Vector import Vector

CANVASWIDTH = 500
CANVASHEIGHT = 500


class Button:
    def __init__(self, canvas, pos, txt):
        self.canvas = canvas
        self.pos = pos
        self.xRat = 1.045
        self.yRat = 6
        self.width = 5
        self.colour = "White"
        self.txt = txt
        self.point1 = pos
        self.point2 = [self.pos[0] + CANVASWIDTH / self.xRat, self.pos[1]]
        self.point3 = [self.pos[0] + CANVASWIDTH / self.xRat, self.pos[1] + CANVASHEIGHT / self.yRat]
        self.point4 = [self.pos[0], self.pos[1] + CANVASHEIGHT / self.yRat]

    def draw(self):
        self.canvas.draw_polygon([self.point1, self.point2, self.point3, self.point4], self.width, self.colour)
        self.canvas.draw_text(self.txt, [self.pos[0] * 4, self.pos[1] + CANVASHEIGHT / self.yRat / 1.5], 50,
                              self.colour, 'monospace')


class Menu:
    def __init__(self):
        self.startPos = [CANVASWIDTH / 50, CANVASHEIGHT / 2.5]
        self.helpPos = [CANVASWIDTH / 50, CANVASHEIGHT / 1.67]
        self.exitPos = [CANVASWIDTH / 50, CANVASHEIGHT / 1.25]
        self.backPos = [[10, 10], [10, 50], [50, 50], [50, 10]]
        self.arrowPos = [[20, 30], [30, 40], [30, 20]]
        self.arrowShaftPos = [[30, 30], [40, 30]]
        self.backX = 50
        self.backY = 50
        self.isStart = False
        self.isHelp = False
        self.isExit = False
        self.isMenu = True

    def click(self, pos):
        self.pos = pos

        if self.pos[1] > self.startButton.point1[1] and self.pos[1] < self.startButton.point4[1]:
            self.isStart = True
            self.isHelp = False
            self.isExit = False
            self.isMenu = False
            print("Start")

        if self.pos[1] > self.helpButton.point1[1] and self.pos[1] < self.helpButton.point4[1]:
            self.isStart = False
            self.isHelp = True
            self.isExit = False
            self.isMenu = False
            print("Help")

        if self.pos[1] > self.exitButton.point1[1] and self.pos[1] < self.exitButton.point4[1]:
            self.isStart = False
            self.isHelp = False
            self.isExit = True
            self.isMenu = False
            print("Exit")

        if (self.isStart or self.isHelp) and self.pos[0] < self.backX and self.pos[1] < self.backY:
            self.isStart = False
            self.isHelp = False
            self.isExit = False
            self.isMenu = True

    def draw(self, canvas):
        self.canvas = canvas
        self.startButton = Button(self.canvas, self.startPos, "Start")
        self.helpButton = Button(self.canvas, self.helpPos, "Help")
        self.exitButton = Button(self.canvas, self.exitPos, "Exit")
        if self.isMenu:
            self.startButton.draw()
            self.helpButton.draw()
            self.exitButton.draw()

        if self.isStart:
            self.canvas.draw_polygon(self.backPos, 4, "White")
            self.canvas.draw_polygon(self.arrowPos, 4, "White")
            self.canvas.draw_polygon(self.arrowShaftPos, 4, "White")

        if self.isHelp:
            self.canvas.draw_polygon(self.backPos, 4, "White")
            self.canvas.draw_polygon(self.arrowPos, 4, "White")
            self.canvas.draw_polygon(self.arrowShaftPos, 4, "White")

        if self.isExit:
            exit()


frame = simplegui.create_frame("Game", CANVASWIDTH, CANVASHEIGHT)
menu = Menu()
frame.set_draw_handler(menu.draw)
frame.set_mouseclick_handler(menu.click)
frame.start()