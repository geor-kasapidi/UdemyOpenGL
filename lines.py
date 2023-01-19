import math
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from utils import *

pygame.init()

screen_width = 1000
screen_height = 800
ortho_width = 640
ortho_height = 480

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Graphs in PyOpenGL')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 4, -1, 1)


def plot_point(p):
    glBegin(GL_POINTS)
    glVertex2f(p[0], p[1])
    glEnd()

def plot_lines(points):
    glBegin(GL_LINE_STRIP)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

def plot_graph(px, py):
    glBegin(GL_LINE_STRIP)
    for (x, y) in zip(px, py):
        glVertex2f(x, y)
    glEnd()

done = False
init_ortho()
glPointSize(5)

point_groups = []
current_points = []

mouse_down = False

px = np.arange(0, 4, 5e-3)
py = np.exp(-px) * np.cos(2 * math.pi * px)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            if not mouse_down:
                point_groups.append(current_points)
                current_points = []
                mouse_down = True
        elif event.type == MOUSEBUTTONUP:
            if mouse_down:
                mouse_down = False
        elif event.type == MOUSEMOTION:
            if mouse_down:
                p = pygame.mouse.get_pos()
                _p = (map_value(0, screen_width, 0, ortho_width, p[0]), map_value(0, screen_height, ortho_height, 0, p[1]))
                current_points.append(_p)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_graph(px, py)
    # for point_group in point_groups:
        # plot_lines(point_group)
    # plot_lines(current_points)
    pygame.display.flip()
    # pygame.time.wait(100)
pygame.quit()
