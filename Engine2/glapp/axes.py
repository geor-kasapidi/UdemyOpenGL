from .mesh import *

class AxesMesh(Mesh):
    def __init__(self, program_id) -> None:
        vertices = [
            [-100, 0, 0],
            [100, 0, 0],
            [0, -100, 0],
            [0, 100, 0],
            [0, 0, -100],
            [0, 0, 100],
        ]
        colors = [
            [1,0,0],
            [1,0,0],
            [0,1,0],
            [0,1,0],
            [0,0,1],
            [0,0,1],
        ]
        super().__init__(program_id, vertices, colors, GL_LINES)
