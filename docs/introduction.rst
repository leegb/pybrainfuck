Introduction
############

.. image:: https://img.shields.io/pypi/v/pybrainfuck.svg
   :alt: PyPi Version
   :scale: 100%
   :target: https://pypi.python.org/pypi/pybrainfuck/

.. image:: https://img.shields.io/pypi/dm/pybrainfuck.svg
   :alt: PyPi Monthly Donwloads
   :scale: 100%
   :target: https://pypi.python.org/pypi/pybrainfuck/

.. image:: https://img.shields.io/pypi/l/pybrainfuck.svg
   :alt: License
   :scale: 100%
   :target: https://github.com/mementum/pybrainfuck/blob/master/LICENSE

.. image:: https://travis-ci.org/mementum/pybrainfuck.png?branch=master
   :alt: Travis-ci Build Status
   :scale: 100%
   :target: https://travis-ci.org/mementum/pybrainfuck

.. image:: https://readthedocs.org/projects/pybrainfuck/badge/?version=latest
   :alt: Documentation Status
   :scale: 100%
   :target: https://readthedocs.org/projects/pybrainfuck/

.. image:: https://img.shields.io/pypi/pyversions/pybrainfuck.svg
   :alt: Pytghon versions
   :scale: 100%
   :target: https://pypi.python.org/pypi/pybrainfuck/

``pybrainfuck`` is yet another Python BrainFuck implementation. The goal is not
be the fastest or most efficient but rather to be extensive in the
implementation, configurable and extendable.

It contains a ``BrainFck `` class which can be directly used or subclassed to
use in scripts. The code is fully documented and commented.

Or else the pip installed script ``pybrainfuck`` can be directly used.

Documentation
=============

Read the full documentation at readthedocs.org:

  - `pybrainfuck documentation <http://pybrainfuck.readthedocs.org/en/latest/introduction.html>`_


Python 2/3 Support
==================

  - Python 2.7
  - Python 3.2/3.3/3.4/3.5

  - It also works with pypy and pypy3


Installation
============

From pypi::

  pip install pybrainfuck

From source:

  - Place the *pybrainfuck* directory found in the sources inside your project
    and import it

Scriptwise:

  - The entire implementation has been kept inside a single file. You can copy
    it inside other sources too


Quick Usage
===========

Let's quickly put together a script::

    from __future__ import (absolute_import, division, print_function,
                            unicode_literals)

    import sys

    from pybrainfuck import BrainFck

    if name == '__main__':

        bfck = BrainFck()

	for arg in sys.argv[1:]:
	    print('-' * 50)
	    print('Running:', arg)
	    print('-' * 50)
	    bfck.runfile(arg)
	    print()

And prepare a **Hello World** (including a newline) ``brainfuck`` program::

    ++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.

And both paired for a execution::

    $ ./readme-example.py readme-example.b
    --------------------------------------------------
    Running: readme-example.b
    --------------------------------------------------
    Hello World!


Although the newlines after ``Hello World!`` are difficult to perceive.

Using the built-in script ``pybrainfuck``::

    $ pybrainfuck readme-example.b
    Hello World!

Which luckily produces the same result.
