from OpenGL.GL import *
import pygame
from .mesh import *
from .utils import *
from collections import namedtuple


class OBJData:
    def __init__(self, vertices, uvs, normals) -> None:
        self.vertices = vertices
        self.uvs = uvs
        self.normals = normals


def load_drawing(file):
    vertices = []
    vertices_i = []
    uvs = []
    uvs_i = []
    normals = []
    normals_i = []

    with open(file) as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            if line[:2] == "v ":
                x, y, z = [float(value)
                           for value in line[2:].split(' ')]
                vertices.append((x, y, z))
            elif line[:3] == "vt ":
                u, v = [float(value) for value in line[3:].split(' ')]
                uvs.append((u, v))
            elif line[:3] == "vn ":
                x, y, z = [float(value) for value in line[3:].split(' ')]
                normals.append((x, y, z))
            elif line[:2] == "f ":
                indices = [int(value) - 1 for values in line[2:].split(' ')
                           for value in values.split('/')]

                vertices_i.extend((indices[0], indices[3], indices[6]))
                uvs_i.extend((indices[1], indices[4], indices[7]))
                normals_i.extend((indices[2], indices[5], indices[8]))

    return OBJData(
        format_vertices(vertices, vertices_i),
        format_vertices(uvs, uvs_i),
        format_vertices(normals, normals_i)
    )


class LoadMesh(Mesh):
    def __init__(self, program_id, file_name, texture_file=None) -> None:
        obj_data = load_drawing(file_name)
        colors = np.repeat([1, 1, 1], len(obj_data.vertices))
        # colors = np.random.uniform(low=0, high=1, size=(len(obj_data.vertices), 3))
        super().__init__(program_id, obj_data.vertices, colors,
                         GL_TRIANGLES, uvs=obj_data.uvs, normals=obj_data.normals, texture_file=texture_file)
