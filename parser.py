from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing
See the file script for an example of the file format
"""

#add_line done!
#done!
def make_ident(fname, points, transform, screen, color):
    ident(points)

#done!
def scale(transform, sx, sy, sz):
    m = make_scale(sx, sy, sz)
    matrix_mult(m, transform)

#done!
def move(transform, tx, ty, tz):
    matrix_mult(make_translate(tx, ty, tz), transform)

#done!
def rotate(transform, axis, theta):
    if (axis == 'x'):
        matrix_mult(make_rotX(theta), transform)
    elif (axis == 'y'):
        matrix_mult(make_rotY(theta), transform)
    elif (axis == 'z'):
        matrix_mult(make_rotZ(theta), transform)
    print("rotate")

#done!
def apply_transformation(fname, points, transform, screen, color):
    matrix_mult(transform, points)

#done!
def display_pic(fname, points, transform, screen, color):
    draw_lines(points, screen, color)
    display(screen)
    clear_screen(screen)

#done!
def save(fname, points, screen, color):
    draw_lines(points, screen, color)
    save_extension(screen, fname)
    clear_screen(screen)

def end_parsing():
    pass

def parse_file( fname, points, transform, screen, color ):
    f = open(fname, 'r')
    s = f.read()
    l = s.split('\n')
    for i in range(len(l)):
        #If current command needs arguments
        if l[i] in commands:
            if i != len(l)-1 and l[i+1] not in commands:
                m = l[i+1].split(' ')
                #save command
                if len(m) == 1:
                    commands[l[i]](m[0], points, screen, color)
                #rotate command
                elif len(m) == 2:
                    commands[l[i]](transform, m[0], int(m[1]))
                #scale, move commands
                elif len(m) == 3:
                    commands[l[i]](transform, int(m[0]), int(m[1]), int(m[2]))
                #add_line command
                elif len(m) == 6:
                    commands[l[i]](points, int(m[0]), int(m[1]), int(m[2]), int(m[3]), int(m[4]), int(m[5]))
            #ident, apply, display, quit commands
            else:
                commands[l[i]](fname, points, transform, screen, color)
    f.close()
    
commands = {'line': add_edge, 'ident': make_ident, 'scale': scale, 'move': move,
            'rotate': rotate, 'apply': apply_transformation, 'display': display_pic,
            'save': save, 'quit': end_parsing}

                    
