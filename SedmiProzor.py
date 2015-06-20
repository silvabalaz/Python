import sys
import OpenGL.GL as gl
import OpenGL.GLUT as glut

def display():
	#zadane tocke grupiraju se u grupe po 4 i tumace kao vrhovi cetverokuta koje treba nacrtati
	gl.glBegin(gl.GL_QUADS)
	gl.glColor3f(1,0,0); gl.glVertex2f( 1.0,-1.0) 
	gl.glColor3f(1,1,0); gl.glVertex2f(-1.0,-1.0)
	gl.glColor3f(1,1,1); gl.glVertex2f(-1.0, 1.0)
	gl.glColor3f(1,0,1); gl.glVertex2f( 1.0, 1.0)
	gl.glEnd()  
	

	
	gl.glBegin(gl.GL_QUADS)
	gl.glColor3f(1,0,0); gl.glVertex2f( -0.85,0.85) 
	gl.glColor3f(1,1,1); gl.glVertex2f(0.85,0.85)
	gl.glColor3f(0,1,1); gl.glVertex2f(0.85, -0.85)
	gl.glColor3f(0,1,0); gl.glVertex2f( -0.85, -0.85)
	gl.glEnd() 

	gl.glBegin(gl.GL_QUADS)
	gl.glColor3f(0,1,1); gl.glVertex2f( 0.5,-0.5) 
	gl.glColor3f(1,0,1); gl.glVertex2f(-0.5,-0.5)
	gl.glColor3f(1,1,1); gl.glVertex2f(-0.5, 0.5)
	gl.glColor3f(1,0,0); gl.glVertex2f( 0.5, 0.5)
	gl.glEnd()  

	glut.glutSwapBuffers()
	#cetverokuti se popunjavaju aktivnom bojom

def reshape(width,height):
    gl.glViewport(0, 0, width, height)

def keyboard( key, x, y ):
    if key == 'a':
        sys.exit( )

glut.glutInit()

glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)

glut.glutCreateWindow('Moj sedmi prozor')

glut.glutReshapeWindow(550,550)
glut.glutReshapeFunc(reshape)

glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard)

glut.glutMainLoop()
