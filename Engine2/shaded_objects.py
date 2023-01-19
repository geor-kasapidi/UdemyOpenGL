from glapp.base_app import *
import numpy as np
from glapp.utils import *
from glapp.graphics_data import *
from glapp.uniform import *
from glapp.square_mesh import *
from glapp.axes import *
from glapp.cube import *
from glapp.load_mesh import *
from glapp.light import *

vertex_shader = r'''
#version 330 core

uniform mat4 projection_mat;
uniform mat4 view_mat;
uniform mat4 model_mat;

in vec3 position;
in vec3 vertex_color;
in vec3 vertex_normal;
out vec3 color;
out vec3 normal;
out vec3 frag_pos;
out vec3 view_pos;

void main() {
    view_pos = vec3(inverse(model_mat) * vec4(view_mat[3][0], view_mat[3][1], view_mat[3][2],1));
    gl_Position = projection_mat * inverse(view_mat) * model_mat * vec4(position,1);
    normal = mat3(transpose(inverse(model_mat))) * vertex_normal;
    frag_pos = vec3(model_mat * vec4(position,1));
    color = vertex_color;
}
'''

fragment_shader = r'''
#version 330 core

struct Light {
    vec3 position;
    vec3 color;
};

#define NUM_LIGHTS 2

uniform Light light_data[NUM_LIGHTS];

in vec3 color;
in vec3 normal;
in vec3 frag_pos;
in vec3 view_pos;

out vec4 frag_color;

vec4 createLight(vec3 light_pos, vec3 light_color, vec3 normal, vec3 frag_pos, vec3 view_dir) {
    //ambient
    float a_strength = 0.1;
    vec3 ambient = a_strength * light_color;
    
    //diffuse
    vec3 norm = normalize(normal);
    vec3 light_dir = normalize(light_pos - frag_pos);
    float diff = max(dot(norm, light_dir), 0);
    vec3 diffuse = diff * light_color;
    
    //specular
    float s_strength = 0.3;
    vec3 reflect_dir = normalize(-light_dir - norm);
    float spec = pow(max(dot(view_dir, reflect_dir), 0), 32);
    vec3 specular = s_strength * spec * light_color;
    
    return vec4(color * (ambient + diffuse + specular), 1);
}

void main() {
    vec3 view_dir = normalize(view_pos - frag_pos);
    frag_color = vec4(0,0,0,1);
    for(int i=0; i<NUM_LIGHTS; i++) {
        frag_color += createLight(light_data[i].position, light_data[i].color, normal, frag_pos, view_dir);
    }
}
'''


class ShadedObjects(BaseApp):
    def __init__(self) -> None:
        super().__init__((850, 200), (1000, 800))
        self.mesh = None
        self.axes = None
        self.cube = None
        self.teapot = None
        self.lights = None
        self.angle = 45
        self.translation = 0

    def initialize(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.camera = Camera(
            self.program_id, self.screen_size[0], self.screen_size[1])
        self.mesh = SquareMesh(self.program_id)
        self.axes = AxesMesh(self.program_id)
        self.cube = CubeMesh(self.program_id)
        self.teapot = LoadMesh(
            self.program_id, '/Users/georkasapidi/UdemyOpenGL/Engine2/models/teapot.obj')
        self.lights = [
            Light(self.program_id, pygame.Vector3(
                2, 1, 2), pygame.Vector3(1, 0, 0), 0),
            Light(self.program_id, pygame.Vector3(-2, 1, 2),
                  pygame.Vector3(0, 1, 0), 1)
        ]
        glEnable(GL_DEPTH_TEST)

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        self.camera.update()
        # self.mesh.draw(identity_mat())
        # self.axes.draw(identity_mat())

        # self.angle += 2
        # self.translation += 0.01

        for light in self.lights:
            light.update()

        tt = identity_mat()
        # tt = rotate_a(tt, self.angle, pygame.Vector3(1,0,1))
        # tt = scale3(tt, 0.5,0.5,0.5)
        # tt = translate(tt, 2,1,2)

        self.teapot.draw(tt)
        # tt = translate(tt, 0,0,self.translation)
        # tt = rotate_y(tt, self.angle)
        # self.cube.draw(tt)


ShadedObjects().mainloop()
