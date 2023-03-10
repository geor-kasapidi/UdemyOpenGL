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
ortho_top = 0 #-400
ortho_bottom = 800

screen = pygame.display.set_mode(
    (screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Turtle Graphics')

current_position = (0, 0)
direction = np.array([0, 1, 0])

axiom = 'X'
rules = {
    "F": "FF",
    "X": "F+[-F-XF-X][+FF][--XF[+X]][++F-X]"
}
draw_length = 10
angle = 25
stack = []
rule_run_number = 5
instructions = ""

points = []
x = 0
y = 0


def run_rule(run_count):
    global instructions
    instructions = axiom
    for loops in range(run_count):
        old_system = instructions
        instructions = ""
        for c in old_system:
            instructions += rules[c] if c in rules else c
    print("Rule")
    print(instructions)


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)


def line_to(x, y):
    global current_position
    glBegin(GL_LINE_STRIP)
    glVertex2f(current_position[0], current_position[1])
    glVertex2f(x, y)
    current_position = (x, y)
    glEnd()


def move_to(position):
    global current_position
    current_position = position


def reset_turtle():
    global current_position
    global direction
    current_position = (0, 0)
    direction = np.array([0, 1, 0])


def draw_turtle():
    global x, y
    points.append((x, y))
    r = np.random.rand()

    a, b, c, d, e = 0, 0, 0, 0, 0

    if r < 0.1:
        d = 0.16
    elif r < 0.86:
        a, b, c, d, e = 0.85, 0.04, -0.04, 0.85, 1.6
    elif r < 0.93:
        a, b, c, d, e = 0.2, -0.26, 0.23, 0.22, 1.6
    else:
        a, b, c, d, e = -0.15, 0.28, 0.26, 0.24, 0.44

    x, y = a*x + b*y, c*x + d*y + e


def draw_points():
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()


def forward(draw_length):
    new_x = current_position[0] + direction[0] * draw_length
    new_y = current_position[1] + direction[1] * draw_length
    line_to(new_x, new_y)


def rotate(angle):
    global direction
    direction = z_rotation(direction, math.radians(angle))


init_ortho()
done = False
glPointSize(1)
glColor3f(0, 1, 0)

# https://en.wikipedia.org/wiki/Barnsley_fern

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glScaled(80, 80, 1)
    glBegin(GL_POINTS)
    glVertex2f(0, 0)
    glEnd()
    reset_turtle()
    draw_turtle()
    draw_points()
    pygame.display.flip()
    pygame.time.wait(1)
pygame.quit()
