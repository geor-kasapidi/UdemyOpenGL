import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)

pygame.display.set_caption('Hello world')

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, screen_width, screen_height, 0)

init_ortho()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2i(100, 50)
    glEnd()

    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2i(130, 65)
    glEnd()

    glPointSize(15)
    glBegin(GL_POINTS)
    glVertex2i(180, 90)
    glEnd()

    glPointSize(20)
    glBegin(GL_POINTS)
    glVertex2i(240, 120)
    glEnd()

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
