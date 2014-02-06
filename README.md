Picascii
========

Ascii Drawing Command Line Utility
The Draw utility can read from stdin:

   cat smaple_input.txt | ./draw.py

Or read a command file:

    ./draw.py --input=sample_input.txt

Or read user input:

   ./draw.py 
   C 20 4 <enter>
   L 1 2 6 2 <enter>
   etc..

Or you can run the built-in test:

   ./draw.py --test
