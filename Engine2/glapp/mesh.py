from OpenGL import *
import pygame
from .graphics_data import *
import numpy as np
from .uniform import *
from .texture import *


class Mesh():
    def __init__(self, program_id, vertices, vertex_colors, draw_type, uvs=None, normals=None, texture_file=None) -> None:
        self.program_id = program_id
        self.vertices = vertices
        self.uvs = uvs
        self.normals = normals
        self.draw_type = draw_type
        self.vao_ref = glGenVertexArrays(1)
        glBindVertexArray(self.vao_ref)

        position_var = GrapicsData("vec3", self.vertices)
        position_var.create_variable(program_id, "position")

        if self.uvs is not None:
            uvs_var = GrapicsData("vec2", self.uvs)
            uvs_var.create_variable(program_id, "vertex_uv")

        if self.normals is not None:
            normals_var = GrapicsData("vec3", self.normals)
            normals_var.create_variable(program_id, "vertex_normal")

        colors_var = GrapicsData("vec3", vertex_colors)
        colors_var.create_variable(program_id, "vertex_color")

        if texture_file is not None:
            self.image = Texture(texture_file)
            self.texture = Uniform("sampler2D", [self.image.texture_id, 1])
            self.texture.find_variable(program_id, "tex")

    def draw(self, transformation_mat):
        if self.texture is not None:
            self.texture.load()
        transformation = Uniform("mat4", transformation_mat)
        transformation.find_variable(self.program_id, "model_mat")
        transformation.load()
        glBindVertexArray(self.vao_ref)
        glDrawArrays(self.draw_type, 0, len(self.vertices))
