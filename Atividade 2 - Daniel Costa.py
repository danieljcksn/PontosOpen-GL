#Segunda atividade da Disciplina de Computação Gráfica - UESC
#Aluno: Daniel Jackson Cavalcante Costa - Matrícula: 201810657

#Importando as bibliotecas a serem utilizadas
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


#Solicitando, como entrada, as coordenadas de um ponto específico para...
#a criação de um círculo.
x, y = map(int, input().split())

#Exercício 1
#Função que define, manualmente, as posições dos pontos para a formação do círculo
def pontosManuais():
    glBegin(GL_POINTS)
    glVertex2f(250, 120)
    glVertex2f(250, 280)

    glVertex2f(150, 200)
    glVertex2f(350, 200)

    glVertex2f(175, 250)
    glVertex2f(325, 250)

    glVertex2f(175, 150)
    glVertex2f(325, 150)

    glEnd()

#Exercício 2
#Gera, a partir de um ponto inicial recebido como entrada, um círculo.
def pontoInicial(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glVertex2f(x, y+160)

    glVertex2f(x-100, y+80)
    glVertex2f(x+100, y+80)

    glVertex2f(x-75, y+130)
    glVertex2f(x+75, y+130)

    glVertex2f(x-75, y+30)
    glVertex2f(x+75, y+30)

    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    #Imprime o círculo formado pelas coordenadas feitas manualmente.
    pontosManuais()
    #Imprime o círculo formado pelas coordenadas passadas como argumento.
    pontoInicial(x, y)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
