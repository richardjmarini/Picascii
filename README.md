Picascii
========

Ascii Drawing Command Line Utility
The Draw utility can read from stdin:

   cat input.txt | ./draw.py

Or read a command file:

    ./draw.py --input=input.txt

Or read user input:

   ./draw.py 
   C 20 4 <enter>
   L 1 2 6 2 <enter>
   etc..

Or you can run the built-in test:

   ./draw.py --test

Help on module draw:

NAME
    draw

FILE
    /home/marini/Projects/huge/draw.py

DESCRIPTION
    Author: Richard J. Marini (richardjmarini@gmail.com)
    Description: Huge Interview Quiz
    Date: 1/21/2014

CLASSES
    __builtin__.object
        Tool
            Line
            Point
                Bucket
            Rectangle
                Canvas
    
    class Bucket(Point)
     |  container for bucket tool
     |  
     |  Method resolution order:
     |      Bucket
     |      Point
     |      Tool
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, x, y, color, id=None)
     |  
     |  render(self)
     |      generates the point at which the bucket tool is applied
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Tool:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Canvas(Rectangle)
     |  container for canvas tool
     |  
     |  Method resolution order:
     |      Canvas
     |      Rectangle
     |      Tool
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __delitem__(self, id)
     |      removes a tool from the canvas (see .remove())
     |  
     |  __init__(self, width, height, id=None)
     |  
     |  __setitem__(self, id, tool)
     |      adds a tool to the canvas (see .add())
     |  
     |  add(self, tool, id=None)
     |      adds a tool to the canvas (see .__setitem__())
     |  
     |  clear(self)
     |      clears the toolbox and buffer
     |  
     |  fill(self, x, y, color)
     |      fills area connected to x,y via recursion
     |  
     |  remove(self, id)
     |      removes tool from the canvas (see .__delitem__())
     |  
     |  render(self)
     |      renders all the points of the canvas to stdout  (see ._render())
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Tool:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Line(Tool)
     |  line object
     |  
     |  Method resolution order:
     |      Line
     |      Tool
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, x1, y1, x2, y2, id=None)
     |  
     |  render(self)
     |      genereates all the points in a straight line
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Tool:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Point(Tool)
     |  represents a point in a 2d plane
     |  
     |  Method resolution order:
     |      Point
     |      Tool
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, x, y, id=None)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Tool:
     |  
     |  render(self)
     |      override this in your dervied object
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Tool:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Rectangle(Tool)
     |  container for the rectangle tool
     |  
     |  Method resolution order:
     |      Rectangle
     |      Tool
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, x1, y1, x2, y2, id=None)
     |  
     |  render(self)
     |      genereates all the points of a rectangle by drawing a line between each vertex
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Tool:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Tool(__builtin__.object)
     |  container for tool object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, id=None)
     |  
     |  render(self)
     |      override this in your dervied object
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    exit(...)
        exit([status])
        
        Exit the interpreter by raising SystemExit(status).
        If the status is omitted or None, it defaults to zero (i.e., success).
        If the status is numeric, it will be used as the system exit status.
        If it is another kind of object, it will be printed and the system
        exit status will be one (i.e., failure).
    
    test()
        test various draw tools

DATA
    argv = ['-c']
    stdin = <open file '<stdin>', mode 'r'>
    stdout = <open file '<stdout>', mode 'w'>


