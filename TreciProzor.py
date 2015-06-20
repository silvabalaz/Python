import sys
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

def display():
	
	
	gl.glClearColor(1,1,0,0)
	gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT )
	gl.glColor3f(1,0,1,1)
	
	gl.glBegin(gl.GL_LINE_STRIP)
	gl.glVertex2f(0.50,0.50) 
	gl.glVertex2f(1.50,1.50)
	gl.glVertex2f(0.50,1.50)
	gl.glVertex2f(0.50,0.50)
	gl.glEnd()
	glut.glutSwapBuffers()


def keyboard( key, x, y ):
    if key == 'a':
        sys.exit( )

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DEPTH |glut.GLUT_DOUBLE | glut.GLUT_RGBA)
glut.glutInitWindowPosition(100,100)
glut.glutInitWindowSize(640,640)
glut.glutCreateWindow("Moj treci prozor")
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard)
glut.glutMainLoop()
