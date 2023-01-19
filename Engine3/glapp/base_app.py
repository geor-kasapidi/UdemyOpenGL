from pygame.locals import *
from .camera import *
import os
from OpenGL.GL import *
from OpenGL.GLU import *

class BaseApp():
    def __init__(self, screen_pos, screen_size) -> None:
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_pos[0], screen_pos[1])
        self.screen_size = screen_size
        pygame.init()
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 32)
        self.screen = pygame.display.set_mode((screen_size[0], screen_size[1]), DOUBLEBUF | OPENGL)
        pygame.display.set_caption('OpenGL in Python')
        self.camera = None
        self.program_id = None
        self.clock = pygame.time.Clock()
    
    def draw_world_axes(self):
        glLineWidth(4)
        glBegin(GL_LINES)
        glColor(1, 0, 0)
        glVertex3d(-1000, 0, 0)
        glVertex3d(1000, 0, 0)
        glColor(0, 1, 0)
        glVertex3d(0, -1000, 0)
        glVertex3d(0, 1000, 0)
        glColor(0, 0, 1)
        glVertex3d(0, 0, -1000)
        glVertex3d(0, 0, 1000)
        glEnd()

        sphere = gluNewQuadric()

        # x pos sphere
        glColor(1, 0, 0)
        glPushMatrix()
        glTranslated(1, 0, 0)
        gluSphere(sphere, 0.05, 10, 10)
        glPopMatrix()

        # y pos sphere
        glColor(0, 1, 0)
        glPushMatrix()
        glTranslated(0, 1, 0)
        gluSphere(sphere, 0.05, 10, 10)
        glPopMatrix()

        # z pos sphere
        glColor(0, 0, 1)
        glPushMatrix()
        glTranslated(0, 0, 1)
        gluSphere(sphere, 0.05, 10, 10)
        glPopMatrix()

        glLineWidth(1)
        glColor(1, 1, 1)
    
    def initialize(self):
        pass

    def display(self):
        pass

    def camera_init(self):
        pass

    def mainloop(self):
        self.initialize()

        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.mouse.set_visible(True)
                        pygame.event.set_grab(False)
                    if event.key == K_SPACE:
                        pygame.mouse.set_visible(False)
                        pygame.event.set_grab(True)
            self.camera_init()
            self.display()
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
    