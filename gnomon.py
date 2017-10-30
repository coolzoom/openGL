from OpenGL.GL import *
class Gnomon(object):
    """simple 3 axis colored gnomon to check viewport orientation"""
    def __init__(self):
        self.vertices = ((0, 0, 0),(1, 0, 0),(0, 1, 0),(0, 0, 1))
        self.edges=(0,1),(0,2),(0,3)
    def draw(self):
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_LINES)
        for vertex in self.edges[0]:
            glVertex3fv(self.vertices[vertex])
        glColor3f(0.0, 1.0, 0.0)
        for vertex in self.edges[1]:
            glVertex3fv(self.vertices[vertex])
        glColor3f(0.0, 0.0, 1.0)
        for vertex in self.edges[2]:
            glVertex3fv(self.vertices[vertex])
        glEnd()
