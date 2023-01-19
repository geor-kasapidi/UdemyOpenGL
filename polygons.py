import math
import numpy as np

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from utils import *

pygame.init()

screen_width = 800
screen_height = 800
ortho_left = -400
ortho_right = 400
ortho_top = -400
ortho_bottom = 400

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Polygons in PyOpenGL')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)


def plot_polygon():
    glColor(0.2, 0.2, 0.2, 1)
    glBegin(GL_TRIANGLES)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

def plot_lines():
    glLineWidth(5)
    glColor3f(1, 0, 0)
    for i in range(0,len(points) // 3):
        p = (points[i*3+0], points[i*3+1], points[i*3+2])
        glBegin(GL_LINE_LOOP)
        glVertex2f(p[0][0], p[0][1])
        glVertex2f(p[1][0], p[1][1])
        glVertex2f(p[2][0], p[2][1])
        glEnd()
    

done = False
init_ortho()
points = []
while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            p = pygame.mouse.get_pos()
            points.append((map_value(0, screen_width, ortho_left, ortho_right, p[0]),
                           map_value(0, screen_height, ortho_bottom, ortho_top, p[1])))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_polygon()
    plot_lines()
    pygame.display.flip()
pygame.quit()
