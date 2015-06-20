#dva trokuta , jedan unutar drugog
import sys
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

def display():
	gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
	gl.glColor3f(1,0,0,1)
	gl.glBegin(gl.GL_TRIANGLES)
	gl.glVertex2f(-1.0,-1.0)
	gl.glVertex2f(1.0,-1.0)
	gl.glVertex2f(0.0,1.0)
	gl.glEnd()

	gl.glColor3f(1,1,1,1)
	gl.glBegin(gl.GL_TRIANGLES)
	gl.glVertex2f(-0.5,-0.5)
	gl.glVertex2f(0.5,-0.5)
	gl.glVertex2f(0.0,0.5)
	gl.glEnd()
	glut.glutSwapBuffers()


def keyboard( key, x, y ):
    if key == 'a':
        sys.exit()

def mouse(button,state, x, y):
    if(button == glut.GLUT_RIGHT_BUTTON):
	sys.exit()

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DEPTH |glut.GLUT_DOUBLE | glut.GLUT_RGBA)
glut.glutInitWindowPosition(100,100)
glut.glutInitWindowSize(640,640)
glut.glutCreateWindow("Moj cetvrti prozor")
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard)
glut.glutMouseFunc(mouse)
glut.glutMainLoop()
