import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from cube import *
from load_mesh import *
from camera import *
import os

pygame.init()

# project settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode(
    (screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')

mesh = LoadMesh(
    GL_LINE_LOOP, '/Users/georkasapidi/UdemyOpenGL/Engine/Resources/cube.obj')  # teapot
camera = Camera()


def initialise():
    glClearColor(background_color[0], background_color[1],
                 background_color[2], background_color[3])
    glColor(drawing_color)

    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 1000.0)


def camera_init():
    # modelview
    glMatrixMode(GL_MODELVIEW)
    # glTranslate(0, 0, -5)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    camera.update(screen.get_width(), screen.get_height())


def draw_sphere(p, c):
    glPushMatrix()
    s = gluNewQuadric()
    glColor(c[0], c[1], c[2])
    glTranslate(p[0], p[1], p[2])
    gluSphere(s, 0.05, 10, 10)
    glPopMatrix()


def draw_world_axes():
    glLineWidth(4)
    glBegin(GL_LINES)
    glColor(1, 0, 0)
    glVertex3d(-1000, 0, 0)
    glVertex3d(1000, 0, 0)
    glColor(0, 1, 0)
    glVertex3d(0, -1000, 0)
    glVertex3d(0, 1000, 0)
    glColor(0, 0, 1)
    glVertex3d(0, 0, -1000)
    glVertex3d(0, 0, 1000)
    glEnd()
    draw_sphere((1, 0, 0), (1, 0, 0))
    draw_sphere((0, 1, 0), (0, 1, 0))
    draw_sphere((0, 0, 1), (0, 0, 1))


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    camera_init()
    # glPushMatrix()
    # mesh.draw()
    draw_world_axes()
    glLineWidth(1)
    mesh.draw((1,1,1), 30)
    # glPopMatrix()


done = False
initialise()
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
    display()
    pygame.display.flip()
    # pygame.time.wait(10)
pygame.quit()
