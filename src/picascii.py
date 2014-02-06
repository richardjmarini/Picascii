#!/usr/bin/env python

"""
Author: Richard J. Marini (richardjmarini@gmail.com)
Description: Command Line Ascii Drawing Utility
Date: 1/21/2014
"""

from sys import stderr, stdout, stdin, argv, exit
from optparse import OptionParser, make_option

from draw import Draw, Canvas, Line, Rectangle, Bucket

def test():
   """
   test various draw tools 
   """

   # canvas test
   """
   - - - - - - - - - - - - - - - - - - - - -   
   
   |                                         | 
   
   |                                         | 
   
   |                                         | 
   
   |                                         | 
   
   - - - - - - - - - - - - - - - - - - - - - - 
   """
   c= Canvas(20, 4)
   c.render()

   
   # line test
   """
   - - - - - - - - - - - - - - - - - - - - -   
   
   |                                         | 
   
   | x x x x x x                             | 
   
   |                                         | 
   
   |                                         | 
   
   - - - - - - - - - - - - - - - - - - - - - - 
   """
   id= c.add(Line(1,2,6,2))
   c.render()
   
   """
   - - - - - - - - - - - - - - - - - - - - -   
   
   |                                         | 
   
   | x x x x x x                             | 
   
   |           x                             | 
   
   |           x                             | 
   
   - - - - - - - - - - - - - - - - - - - - - - 
   """
   id= c.add(Line(6, 3, 6, 4))
   c.render()
   
   # rectangle test
   """
   - - - - - - - - - - - - - - - - - - - - -   
   
   |                               x x x x   | 
   
   | x x x x x x                   x       x | 
   
   |           x                   x x x x x | 
   
   |           x                             | 
   
   - - - - - - - - - - - - - - - - - - - - - - 
   """
   id= c.add(Rectangle(16, 1, 20, 3))
   c.render()
   
   # bucket fill test
   """
   - - - - - - - - - - - - - - - - - - - - -   
   
   | o o o o o o o o o o o o o o o x x x x   | 
   
   | x x x x x x o o o o o o o o o x       x | 
   
   |           x o o o o o o o o o x x x x x | 
   
   |           x o o o o o o o o o o o o o o | 
   - - - - - - - - - - - - - - - - - - - - -   
   """
   id= c.add(Bucket(10, 3, 'o'))
   c.render()

def parse_args(argv):

   optParser= OptionParser()

   [ optParser.add_option(opt) for opt in [
      make_option("-t", "--test", action= "store_true", dest= "test", default= False, help= "run test"),
      make_option("-i", "--input", default= stdin, help= "input file (default: stdin)")
   ]]
  
   opts, args= optParser.parse_args()
   if opts.input != stdin:
      setattr(opts, 'input', open(opts.input, 'r'))
 
   return opts

if __name__ == '__main__':

   opts= parse_args(argv)
   if opts.test:
      test()
      exit(0)

   draw= Draw(opts.input)
   draw.run()
