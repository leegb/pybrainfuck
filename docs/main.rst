Main
####

There are many ``brainfuck`` implementations (compilers/interpreters) and
therefore no need for yet another implementation.

But here it is.

The goal is to make something configurable, extendable and at the same time
extensive in itself from the very beginning.

``pybrainfuck`` will for sure not win any price for memory efficiency, speed or
size. But it can serve to experiment with the configuration options, extension
commands or who knows what.

The introduction has already shown how to use the ``BrainFck`` class and the
``pybrainfuck`` script.

For the configuration options, take a look at the class reference or the scrip
reference.

Using the ``BrainFck`` class
============================

See the class reference for the full set configuration options and methods.

The most important methods for a external user are::

  - ``runfiles`` which defined as ``def runfiles(self, *args)``

    Each arg in args must be the path to a file containing a ``brainfuck``
    program

  - ``run`` which is  defined as ``def run(self, f)``

    f is either a file (or file-like) object or a string containing the program.

    If a string is passed it will internally converted to a file-like object
    before execution.

Those are the ones the end user pass the ``brainfuck`` programs too.

Formatting of the programs
--------------------------

Usually each ``brainfuck`` is contained in a single file. ``pybrainfuck``
supports additional formats which can aid when it comes down to testing and
readability. The configuration options to support additional formats:

  - linemode (default: False)
    Read the input in lines and interpret each line as a program skipping
    blank lines

  - multiline (default: False)
    In ``linemode`` join lines until a blank line is seen

  - comments (default: False)
    In ``linemode`` skip lines starting with ``commentchar``

  - commentchar (default: #)
    Comment charachter for ``comments`` in ``linemode``

Doing this configuration::

  bfck = BrainFck(linemode=True, multiline=True, comments=True)

and applying it to the following file::

    # Yo!
    +[--->++<]>+++.[->+++++++<]>.[--->+<]>----.

    # Hello World! (and newline)
    ++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.

    # Prints H (and newline) after checking some pathological cases
    []++++++++++[>>+>+>++++++[<<+<+++>>>-]<<<<-]
    "A*$";?@![#>>+<<]>[>>]<<<<[>++<[-]]>.>.

    # Cell 30000 (prints # and newline)
    ++++[>++++++<-]>[>+++++>+++++++<<-]>>++++<[[>[[>>+<<-]<]>>>-]>-[>+>+<<-]>]+++++[>+++++++<<++>-]>.<<.

Results in the execution of 4 ``brainfuck`` programs. Lines starting with '#'
and blank lines will be skipped.

And the 2 line program (because 'multiline' was set to True) will be joined


Extending the command set
=========================

To aid in addind commands without tapping into the logic and internals of the
classavoid tapping into the internals of ``BrainFck`` a decorator is provided to
define commands.

Operation of the existing commands is defined by modifying the ``status``
variables (see the class reference).

In regular ``brainfuck`` the commands ``+`` and ``-`` increment and decrement
the value of the current cell by 1.

To experiment with "shorter" programs which can increment/decrement by 2, let's
add a couple of commands: ``"`` and ``=``::

    from pybrainfuck import BrainFck, BfCommand

    class BrainFck2(BrainFck):

        @BfCommand('"')
	def proc_increment2(self):
	    self.cells[self.ptr] += 2

        @BfCommand('=')
	def proc_decrement2(self):
	    self.cells[self.ptr] -= 2

´Rather than directly modifying the status of the interpreter/machine the
existing methods can be reused::

    from pybrainfuck import BrainFck, BfCommand

    class BrainFck2(BrainFck):

        @BfCommand('"')
	def proc_increment2(self):
	    self.proc_increment()
	    self.proc_increment()

        @BfCommand('=')
	def proc_decrement2(self):
	    self.proc_decrement()
	    self.proc_decrement()

This implementation makes use of the existing methods which manage the
increment/decrement actions. This can also be done by looking up the command
characters::

    from pybrainfuck import BrainFck, BfCommand

    class BrainFck2(BrainFck):

        @BfCommand('"')
	def proc_increment2(self):
	    method = self.cmd_procs['+']
	    method()
	    method()

        @BfCommand('=')
	def proc_decrement2(self):
	    method = self.cmd_procs['-']
	    method()
	    method()


The entire ``BrainFck`` class is fully documented, just see the reference to
modify the behaviors or add new ones.
