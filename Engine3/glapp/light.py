import pygame
from .transformations import *
from .uniform import *


class Light:
    def __init__(self, position=pygame.Vector3(0, 0, 0), color=pygame.Vector3(1, 1, 1), light_number=0) -> None:
        self.transformation = identity_mat()
        self.position = position
        self.color = color
        self.pos_variable = "light_data["+str(light_number)+"].position"
        self.color_variable = "light_data["+str(light_number)+"].color"

    def update(self, program_id):
        light_pos = Uniform("vec3", self.position)
        light_pos.find_variable(program_id, self.pos_variable)
        light_pos.load()

        light_color = Uniform("vec3", self.color)
        light_color.find_variable(program_id, self.color_variable)
        light_color.load()
