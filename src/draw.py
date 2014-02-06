#!/usr/bin/env python

"""
Author: Richard J. Marini (richardjmarini@gmail.com)
Description: Command Line Ascii Drawing Utility
Date: 1/21/2014
"""

from sys import stderr, argv, exit
from uuid import uuid1
from itertools import product
from operator import itemgetter
from re import sub


class Tool(object):
   """
   container for tool object
   """

   def __init__(self, id= None):

      if not id:
         id= uuid1()

      self.id= id
      self.verticies= ()

   def render(self):
      """
      override this in your dervied object
      """
      pass

class Point(Tool):
   """
   represents a point in a 2d plane
   """
   
   def __init__(self, x, y, id= None):

      if not id:
         id= uuid1()

      super(Point, self).__init__(id)
      self.x= x
      self.y= y


class Line(Tool):
   """
   line object
   """

   def __init__(self, x1, y1, x2, y2, id= None):

      if not id:
         id= uuid1()

      super(Line, self).__init__(id)
 
      self.verticies= (Point(x1, y1), Point(x2, y2))

   def render(self):
      """
      genereates all the points in a straight line
      """

      # calculte the x and y deltas
      dx=  self.verticies[1].x - self.verticies[0].x
      dy=  self.verticies[1].y - self.verticies[0].y

      # figure out the slope of the line
      try:
         slope= dy / dx
      except ZeroDivisionError:
         slope= None

      if slope != None:

         # genereate the points of the line on the slope
         width= int(self.verticies[1].x - self.verticies[0].x + 1)
         for interval in range(min(0, width), max(0, width)):
            yield Point(
               self.verticies[0].x + interval,
               self.verticies[0].y + (slope * interval)
            )

      else:
         
         # if there is no slope then it's just a vertical line
         width= self.verticies[1].y - self.verticies[0].y + 1
         for interval in range(min(0, width), max(0, width)):
            yield Point(self.verticies[0].x, self.verticies[0].y + interval)

class Rectangle(Tool):
   """
   container for the rectangle tool
   """

   def __init__(self, x1, y1, x2, y2, id= None):

      if not id:
         id= uuid1()

      super(Rectangle, self).__init__(id)

      self.verticies= (
         Point(x1, y1),
         Point(x1, y2),
         Point(x2, y2),
         Point(x2, y1)
      )

   def render(self):
      """
      genereates all the points of a rectangle by drawing a line between each vertex
      """

      for i in range(0, len(self.verticies)):
         for point in Line(self.verticies[i-1].x, self.verticies[i-1].y,  self.verticies[i].x, self.verticies[i].y).render():
            yield point

class Bucket(Point):
   """
   container for bucket tool
   """

   def __init__(self, x, y, color, id= None):
      if not id:
         id= uuid1()

      super(Bucket, self).__init__(x, y, id)
      self.color= color
      
   def render(self):
      """
      generates the point at which the bucket tool is applied
      """
      yield self.point
 


class Canvas(Rectangle):
   """
   container for canvas tool
   """

   def __init__(self, width, height, id= None):

      if not id:
         id= uuid1()

      super(Canvas, self).__init__(0, 0, width+1, height+1, id)

      self.width= width
      self.height= height
      self.bgcolor= ' '
      self.fgcolor= 'x'
      self.bdcolor= ('-', '|')
      self.bucket= None

      # initializse the shape dictionary and buffer
      self.clear()

   def __setitem__(self, id, tool):
      """
      adds a tool to the canvas (see .add())
      """

      if type(tool) == Bucket:
         self.bucket= tool
      else:
         self.toolbox[id]= tool

   def add(self, tool, id= None):
      """
      adds a tool to the canvas (see .__setitem__())
      """

      if not id:
         id= uuid1()

      if id in self.toolbox:
         raise Exception("tool %s already exists, please remove before adding" % (id))

      self[id]= tool
      return id

   def __delitem__(self, id):
      """
      removes a tool from the canvas (see .remove())
      """
      try:
         del self.toolbox[id]
      except KeyError:
         raise Exception("tool %s does not exist" % (id))

   def remove(self, id):
      """
      removes tool from the canvas (see .__delitem__())
      """
      del self[id]

   def clear(self):
      """
      clears the toolbox and buffer
      """
      self.toolbox= {}

      self.buffer= []
      for i in range(0, self.height + 2):
         col= []
         for j in range(0, self.width + 2):
            col.append(self.bgcolor)
         self.buffer.append(col)


   def fill(self, x, y, color):
      """
      fills area connected to x,y via recursion
      """

      if self.buffer[y][x] != self.bgcolor:
         return

      self.buffer[y][x]= color

      self.fill(x+1, y, color)
      self.fill(x-1, y, color)
      self.fill(x, y+1, color)
      self.fill(x, y-1, color)
      
   def _render(self):
      """
      genereates points for canvas where tools were applied (see .render())
      """
 
      # generates the points for the border
      border= [point for point in super(Canvas, self).render()]
      border_points= map(lambda point: (point.x, point.y), border)

      # genereate the points for all the applied tools from the toolbox
      render_points= []
      for points in [tool.render() for id, tool in self.toolbox.items()]:
         render_points+= [(point.x, point.y) for point in points]
      render_points= sorted(render_points, key= itemgetter(1))

      # genereate the points for the entire canvas
      coordinates= product(range(0, self.height+2), range(0, self.width+2))
      for (y, x) in coordinates:

         if (x,y) in border_points:
            color= self.bdcolor[0] if y in (0, self.height+1) else self.bdcolor[1]
         elif (x,y) in render_points:
            color= self.fgcolor
         else:
            color= self.bgcolor

         self.buffer[y][x]= color

   def render(self):
      """
      renders all the points of the canvas to stdout  (see ._render())
      """

      # render into the buffer
      self._render()

      # apply bucket fill to the buffer
      if self.bucket != None:
         self.fill(self.bucket.x, self.bucket.y, self.bucket.color)

      # render all the points of the buffer to stdout
      last_y= self.height 
      coordinates= product(range(0, self.height+2), range(0, self.width+2))
      for (y, x) in coordinates:
         if y != last_y:
            print '\n'
         print self.buffer[y][x],
         last_y= y
      print

class Draw(object):

   toolbox= {
      'c': Canvas,
      'l': Line,
      'r': Rectangle,
      'b': Bucket,
      'q': exit
   }

   def __init__(self, input):

      super(Draw, self).__init__()
      self.input= input
      self.canvas= None

   def run(self):

      while True:

         line= sub("\r|n", "", self.input.readline().lower())
         args= line.split()
         if len(args) == 0:
            break

         toolname= args.pop(0)

         handler= self.toolbox.get(toolname)
         if handler == None:
            print >> stderr, "unknown tool", toolname

         tool= handler(*[int(arg) if arg.isdigit() else arg  for arg in args])
         if type(tool) == Canvas:
            self.canvas= tool
            self.canvas.render()
            continue

         if self.canvas:
            self.canvas.add(tool)
            self.canvas.render()
         else:
            print >> stderr, "must create canvas first"
