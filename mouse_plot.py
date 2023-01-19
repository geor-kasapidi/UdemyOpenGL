import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from utils import *

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Graphs in PyOpenGL')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)


def plot_point(p):
    glBegin(GL_POINTS)
    glVertex2f(p[0], p[1])
    glEnd()


done = False
init_ortho()
glPointSize(5)

points = []

while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            p = pygame.mouse.get_pos()
            _p = (map_value(0, screen_width, 0, 640, p[0]), map_value(0, screen_height, 480, 0, p[1]))
            points.append(_p)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    for p in points:
        plot_point(p)
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
