from OpenGL.GL import *
import pygame
from math import *

class Mesh:
    def __init__(self, vertices, triangles, draw_type):
        self.vertices = vertices
        self.triangles = triangles
        self.draw_type = draw_type

    def draw(self, position, rotation):
        glPushMatrix()
        glTranslate(position[0], position[1], position[2])
        glRotatef(rotation,0,1,0)
        for i in range(0, len(self.triangles) // 3):
            glBegin(self.draw_type)
            glVertex3fv(self.vertices[self.triangles[3 * i + 0]])
            glVertex3fv(self.vertices[self.triangles[3 * i + 1]])
            glVertex3fv(self.vertices[self.triangles[3 * i + 2]])
            glEnd()
        glPopMatrix()
