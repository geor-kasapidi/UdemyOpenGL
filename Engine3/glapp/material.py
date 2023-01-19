from .utils import *

class Material:
    def __init__(self, vertex_shader, fragment_shader) -> None:
        self.program_id = create_program(open(vertex_shader).read(), open(fragment_shader).read())
    
    def use(self):
        glUseProgram(self.program_id)
