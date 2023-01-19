import pygame
from OpenGL.GLU import *
from math import *


class Camera:
    def __init__(self) -> None:
        self.eye = pygame.math.Vector3(0, 0, 0)
        self.up = pygame.math.Vector3(0, 1, 0)
        self.right = pygame.math.Vector3(1, 0, 0)
        self.forward = pygame.math.Vector3(0, 0, 1)
        self.look = self.eye + self.forward
        self.yaw = -90
        self.pitch = 0
        self.last_mouse = pygame.math.Vector2(0, 0)
        self.mouse_sensitivity = pygame.math.Vector2(0.1, 0.1)
        self.key_sensitivity = 0.008

    def rotate(self, yaw, pitch):
        self.yaw += yaw
        self.pitch += pitch

        if self.pitch > 89.0:
            self.pitch = 89.0
        if self.pitch < -89.0:
            self.pitch = -89.0

        y, p = radians(self.yaw), radians(self.pitch)

        self.forward = pygame.math.Vector3(
            cos(y) * cos(p),
            sin(p),
            sin(y) * cos(p)
        ).normalize()

        self.right = self.forward.cross(pygame.Vector3(0,1,0)).normalize()
        self.up = self.right.cross(self.forward).normalize()

    def update(self, w, h):
        mouse_pos = pygame.mouse.get_pos()
        mouse_change = self.last_mouse - pygame.math.Vector2(mouse_pos)
        self.last_mouse = mouse_pos
        # pygame.mouse.set_pos(w/2,h/2)

        self.rotate(-mouse_change.x * self.mouse_sensitivity.x, mouse_change.y * self.mouse_sensitivity.y)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            self.eye -= self.up * self.key_sensitivity
        elif keys[pygame.K_UP]:
            self.eye += self.up * self.key_sensitivity

        if keys[pygame.K_LEFT]:
            self.eye -= self.right * self.key_sensitivity
        elif keys[pygame.K_RIGHT]:
            self.eye += self.right * self.key_sensitivity

        self.look = self.eye + self.forward
        gluLookAt(self.eye.x, self.eye.y, self.eye.z,
                  self.look.x, self.look.y, self.look.z,
                  self.up.x, self.up.y, self.up.z)
