from glapp.base_app import *
import numpy as np
from glapp.utils import *
from glapp.graphics_data import *
from glapp.uniform import *
from glapp.axes import *
from glapp.load_mesh import *
from glapp.light import *
from glapp.texture import *
from glapp.material import *


class MultiShaders(BaseApp):
    def __init__(self) -> None:
        super().__init__((850, 200), (1000, 800))
        self.axes = None
        self.teapot = None
        self.lights = None
        self.angle = 45
        self.translation = 0
        glEnable(GL_CULL_FACE)

    def initialize(self):
        mat = Material(
            vertex_shader="/Users/georkasapidi/UdemyOpenGL/Engine3/shaders/texturedvert.vs",
            fragment_shader="/Users/georkasapidi/UdemyOpenGL/Engine3/shaders/texturedfrag.vs"
        )
        mat1 = Material(
            vertex_shader="/Users/georkasapidi/UdemyOpenGL/Engine3/shaders/colvert.vs",
            fragment_shader="/Users/georkasapidi/UdemyOpenGL/Engine3/shaders/colfrag.vs"
        )
        self.camera = Camera(self.screen_size[0], self.screen_size[1])
        self.axes = AxesMesh(mat1)
        self.teapot = LoadMesh(
            mat,
            file_name='/Users/georkasapidi/UdemyOpenGL/Engine3/models/cube.obj',
            texture_file='/Users/georkasapidi/UdemyOpenGL/Engine3/images/crate.png'
        )
        self.cubeobj = LoadMesh(
            mat,
            file_name='/Users/georkasapidi/UdemyOpenGL/Engine3/models/plane.obj',
            texture_file='/Users/georkasapidi/UdemyOpenGL/Engine3/images/window.png'
        )
        self.lights = [
            Light(pygame.Vector3(0, 2, -1), pygame.Vector3(1, 1, 1), 0)
        ]
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        tt = identity_mat()

        self.axes.draw(tt, self.camera, self.lights)
        self.teapot.draw(tt, self.camera, self.lights)
        self.cubeobj.draw(translate(tt, 0, 1, 0), self.camera, self.lights)


MultiShaders().mainloop()
