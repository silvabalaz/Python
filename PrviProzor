import sys
import OpenGL.GL as gl
import OpenGL.GLUT as glut

#iscrtavanje scene 
def display():
    glut.glutSwapBuffers()

#pozicija gornjeg lijevog ugla a (0,0), a druga tocka (width,height)
def reshape(width,height):
    gl.glViewport(0, 0, width, height)
#događaj kada se pritisne gumb
def keyboard( key, x, y ):
    if key == 'a':
        sys.exit( )

#inicijaliziranje biblioteke GLUT
glut.glutInit()
#podesavanje nacina iscrtavanja scene-dva graficka spremnika
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)
#stvaranje prozora u kojem ce se iscrtavati scena
glut.glutCreateWindow('Moj prvi prozor')
#velicina prozora
glut.glutReshapeWindow(550,550)
glut.glutReshapeFunc(reshape)
#predajemo pokazivac na metodu display
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard)
#iz ove metode se vise ne izlazi
glut.glutMainLoop()
