import pygame
from OpenGL.GLU import *
from math import *
from .transformations import *
from .uniform import *


class Camera:
    def __init__(self, w, h):
        self.transformation = identity_mat()
        self.last_mouse = pygame.math.Vector2(0, 0)
        self.mouse_sensitivityX = 1
        self.mouse_sensitivityY = 1
        self.key_sensitivity = 0.08
        self.screen_size = (w, h)
        self.projection_mat = perspective_mat(60, w/h, 0.01, 10000)
        self.projection = Uniform("mat4", self.projection_mat)

    def rotate(self, yaw, pitch):
        forward = pygame.Vector3(
            self.transformation[0, 2], self.transformation[1, 2], self.transformation[2, 2])
        up = pygame.Vector3(0, 1, 0)
        angle = forward.angle_to(up)
        self.transformation = rotate_y(self.transformation, yaw, local=False)
        if angle < 170.0 and pitch > 0 or angle > 30.0 and pitch < 0:
            self.transformation = rotate_x(
                self.transformation, pitch, local=True)

    def update(self, program_id):
        if pygame.mouse.get_visible():
            return

        mouse_pos = pygame.mouse.get_pos()
        mouse_change = self.last_mouse - pygame.math.Vector2(mouse_pos)

        pygame.mouse.set_pos(self.screen_size[0] / 2, self.screen_size[1] / 2)

        self.last_mouse = pygame.mouse.get_pos()

        self.rotate(mouse_change.x * self.mouse_sensitivityX,
                    mouse_change.y * self.mouse_sensitivityY)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.transformation = translate(
                self.transformation, 0, 0, self.key_sensitivity)
        if keys[pygame.K_UP]:
            self.transformation = translate(
                self.transformation, 0, 0, -self.key_sensitivity)
        if keys[pygame.K_RIGHT]:
            self.transformation = translate(
                self.transformation, self.key_sensitivity, 0, 0)
        if keys[pygame.K_LEFT]:
            self.transformation = translate(
                self.transformation, -self.key_sensitivity, 0, 0)

        self.projection.find_variable(program_id, "projection_mat")
        self.projection.load()

        lookat = Uniform("mat4", self.transformation)
        lookat.find_variable(program_id, "view_mat")
        lookat.load()
