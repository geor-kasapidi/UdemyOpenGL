from OpenGL.GL import *
import pygame
from mesh import *

def load_drawing(file):
    vertices = []
    triangles = []
    with open(file) as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            if line[:2] == "v ":
                vx, vy, vz = [float(value)
                                for value in line[2:].split(' ')]
                vertices.append((vx, vy, vz))
            if line[:2] == "f ":
                t1, t2, t3 = [int(value.split('/')[0]) -
                                1 for value in line[2:].split(' ')]
                triangles.extend((t1, t2, t3))
    return (vertices, triangles)

class LoadMesh(Mesh):
    def __init__(self, draw_type, file_name):
        vertices, triangles = load_drawing(file_name)
        super().__init__(vertices, triangles, draw_type)
