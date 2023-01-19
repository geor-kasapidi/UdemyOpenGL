from glapp.base_app import *
import numpy as np
from glapp.utils import *
from glapp.graphics_data import *
from glapp.uniform import *
from glapp.square_mesh import *
from glapp.axes import *
from glapp.cube import *
from glapp.load_mesh import *

vertex_shader = r'''
#version 330 core

uniform mat4 projection_mat;
uniform mat4 view_mat;
uniform mat4 model_mat;

in vec3 position;
in vec3 vertex_color;
out vec3 color;

void main() {
    
    gl_Position = projection_mat * inverse(view_mat) * model_mat * vec4(position, 1);
    color = vertex_color;
}
'''

fragment_shader = r'''
#version 330 core

in vec3 color;
out vec4 frag_color;

void main() {
    frag_color = vec4(color, 1);
}
'''


class Projections(BaseApp):
    def __init__(self) -> None:
        super().__init__((850, 200), (1000, 800))
        self.mesh = None
        self.axes = None
        self.cube = None
        self.teapot = None
        self.angle = 45
        self.translation = 0

    def initialize(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.camera = Camera(self.program_id, self.screen_size[0], self.screen_size[1])
        self.mesh = SquareMesh(self.program_id)
        self.axes = AxesMesh(self.program_id)
        self.cube = CubeMesh(self.program_id)
        self.teapot = LoadMesh(self.program_id, '/Users/georkasapidi/UdemyOpenGL/Engine2/models/teapot.obj')
        glEnable(GL_DEPTH_TEST)

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        self.camera.update()
        # self.mesh.draw(identity_mat())
        self.axes.draw(identity_mat())

        self.angle += 2
        self.translation += 0.01

        # tt = identity_mat()
        # tt = rotate_a(tt, self.angle, pygame.Vector3(1,0,1))
        # tt = scale3(tt, 0.5,0.5,0.5)
        # tt = translate(tt, 2,1,2)
        self.teapot.draw(identity_mat())
        # tt = translate(tt, 0,0,self.translation)
        # tt = rotate_y(tt, self.angle)
        # self.cube.draw(tt)


Projections().mainloop()
