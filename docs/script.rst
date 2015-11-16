pybrainfuck - the script
########################

A regular ``pip`` installation will deliver a ``pybrainfuck`` executable which
can be directly used to run ``brainfuck`` programs.

The arguments match those of the ``BrainFck`` class which can be used in scripts.

Usage::

    $ pybrainfuck --help
    usage: pybrainfuck-script.py [-h] [--totalcells TOTALCELLS] [--prealloc]
                                 [--noextleft] [--wrapover] [--cellsize CELLSIZE]
                                 [--nonumclass] [--debug] [--linemode]
                                 [--multiline] [--comments]
                                 [--commentchar COMMENTCHAR] [--breakline]
                                 [--flushout]
                                 script

    BrainF*ck Interpreter/Virtual Machine

    positional arguments:
      script                BrainF*ck script to execute (can be specified multiple
                            times

    optional arguments:
      -h, --help            show this help message and exit
      --totalcells TOTALCELLS, -tc TOTALCELLS
                            Size of memory in cells (set to 0 for unbounded
                            (default: 30000)
      --prealloc, -pa       Preallocate cells if a memory size has been set
                            (default: False)
      --noextleft, -nl      Do not extend the cells to the left in
                            dynamicallocation (default: False)
      --wrapover, -wo       If the number of totalcells is limited, wrap over the
                            boundaries when the amount of totalcells has already
                            been allocated (default: False)
      --cellsize CELLSIZE, -cs CELLSIZE
                            Size in bits of each cell (default: 8)
      --nonumclass, -nn     Do numerics directly rather than with a class
                            (default: False)
      --debug, -db          Print debug information (default: False)
      --linemode, -lm       In line mode each line of a provided script file will
                            be interpreted as a single script. Empty lines will be
                            skipped (default: False)
      --multiline, -ml      In linemode subsequent lines will be joined until a
                            blank line is seen (default: False)
      --comments, -co       In line mode lines starting with # will be skipped
                            (default: False)
      --commentchar COMMENTCHAR, -cc COMMENTCHAR
                            Char which indicates a line is a comment (default: #)
      --breakline, -br      Print a break line in between output of scripts
                            (default: False)
      --flushout, -fo       Flush output on each write (meant for broken buffering
                            like Python 2.x under Win32 (default: False)
