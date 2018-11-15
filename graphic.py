import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def init_window():
    pygame.init()
    display = (600,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 4000.0)
    glTranslatef(0.0,0.0, -1500)

def init_window_3d():
    pygame.init()
    display = (600,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 4000.0)
    glTranslatef(0.0,0.0, -1500)
    glRotatef(10,1,1,0)

def render_polygon(CURRENT_VERTICES):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(3.0,4.0,5.0)
    for vertex in CURRENT_VERTICES :
        glVertex3f(vertex[0],vertex[1],vertex[2])
    glEnd()
    glBegin(GL_LINES)
    glVertex3f(-900,0,0)
    glVertex3f(900,0,0)
    glVertex3f(0,-900,0)
    glVertex3f(0,900,0)
    glEnd()
    pygame.display.flip()

def render_cube(CURRENT_VERTICES,EDGES):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINES)
    for edge in EDGES :
        for vertex in edge :
            glVertex3f(CURRENT_VERTICES[vertex][0],CURRENT_VERTICES[vertex][1],CURRENT_VERTICES[vertex][2])
    glEnd()
    glBegin(GL_LINES)
    glVertex3f(-900,0,0)
    glVertex3f(900,0,0)
    glVertex3f(0,-900,0)
    glVertex3f(0,900,0)
    glVertex3f(0,0,900)
    glVertex3f(0,0,-900)
    glEnd()
    pygame.display.flip()