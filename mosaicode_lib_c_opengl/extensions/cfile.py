# -*- coding: utf-8 -*-
# [MOSAICODE PROJECT]
#
"""
This module contains the JavascriptTemplate class.
"""
from mosaicode.model.codetemplate import CodeTemplate


class CFile(CodeTemplate):
    """
    This class contains methods related the JavascriptTemplate class.
    """
    # ----------------------------------------------------------------------

    def __init__(self):
        CodeTemplate.__init__(self)
        self.name = "opengl"
        self.language = "c"
        self.description = "A full template to generate opengl code"
        self.extension = ".c"
        self.command = "gcc -Wall -g $dir_name$$filename$$extension$ -o $dir_name$$filename$ -lGL -lGLU -lglut -lm\n"
        self.command += "$dir_name$./$filename$"
        self.code_parts = ["global", "function", "call","idle","declaration", "execution"]
        self.code = r"""
#include <GL/glut.h>    // Header File For The GLUT Library
#include <GL/gl.h>  // Header File For The OpenGL32 Library
#include <GL/glu.h> // Header File For The GLu32 Library
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#define ESCAPE 27 //Valor em ASCII do Esc
int window;
$code[global]$
typedef struct mosaicgraph_window{
        float x;
        float y;
        float width;
        float height;
        float red;
        float green;
        float blue;
        float alpha;
        float fullscreen;
        char title[128];
        int id;
        void (*process)(void *self);
}mosaicgraph_window_t;
mosaicgraph_window_t * mosaicgraph_create_window(float width, float height,float x, float y){
    mosaicgraph_window_t * window = (mosaicgraph_window_t *) malloc(sizeof(mosaicgraph_window_t));
    window->fullscreen = 0;
    window->x = x;
    window->y = y;
    window->width = width;
    window->height = height;
    return window;
}
int mosaicgraph_draw_window(mosaicgraph_window_t * window){
    glutInitWindowPosition(window->x, window->y);
    glutInitWindowSize(window->width, window->height);
    glClearColor(window->red, window->green, window->blue, window->alpha);
    glClear(GL_COLOR_BUFFER_BIT);
    window->id = glutCreateWindow(window->title);
    if (window->fullscreen){
        glutFullScreen();
    }
    return window->id;
}
$single_code[function]$
void display(){

  glMatrixMode(GL_MODELVIEW);
  glClear(GL_COLOR_BUFFER_BIT);         // Limpa o collor buffer
  glLoadIdentity();
  $code[call]$
  glutSwapBuffers();
  glFlush();
}
void idle(){
    $code[idle]$
    display();
}
int main (int argc, char** argv){
	glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH);
	$code[declaration]$
    mosaicgraph_window_t * window = mosaicgraph_create_window(500,500,0,0);
    strcpy(window->title, "Main Page");
    mosaicgraph_draw_window(window);
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
    $code[execution, connection]$
    glutDisplayFunc(display);
    glutIdleFunc(&idle);
    glutMainLoop();
	return 0;
}
"""

# -------------------------------------------------------------------------
