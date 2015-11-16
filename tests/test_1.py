#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2015 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# StringIO from io is cStringIO which has problems with encoding if used
# to capture output as below
import StringIO

from pybrainfuck import BrainFck

test_program = '''
# Yo!
+[--->++<]>+++.[->+++++++<]>.[--->+<]>----.

# Hello World! (and newline)
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.

# Prints H (and newline) after checking some pathological cases
[]++++++++++[>>+>+>++++++[<<+<+++>>>-]<<<<-]
"A*$";?@![#>>+<<]>[>>]<<<<[>++<[-]]>.>.

# Quine
->++>+++>+>+>++>>+>+>+++>>+>+>++>+++>+++>+>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>+>+>++>>>+++>>>>>+++>+>>>>>>>>>>>>>>>>>>>>>>+++>>>>>>>++>+++>+++>+>>+++>+++>+>+++>+>+++>+>++>+++>>>+>+>+>+>++>+++>+>+>>+++>>>>>>>+>+>>>+>+>++>+++>+++>+>>+++>+++>+>+++>+>++>+++>++>>+>+>++>+++>+>+>>+++>>>+++>+>>>++>+++>+++>+>>+++>>>+++>+>+++>+>>+++>>+++>>+[[>>+[>]+>+[<]<-]>>[>]<+<+++[<]<<+]>>>[>]+++[++++++++++>++[-<++++++++++++++++>]<.<-<]

# Cell 30000 (prints # and newline)
++++[>++++++<-]>[>+++++>+++++++<<-]>>++++<[[>[[>>+<<-]<]>>>-]>-[>+>+<<-]>]+++++[>+++++++<<++>-]>.<<.
'''

test_output = '''Yo!
Hello World!

H

->++>+++>+>+>++>>+>+>+++>>+>+>++>+++>+++>+>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>+>+>++>>>+++>>>>>+++>+>>>>>>>>>>>>>>>>>>>>>>+++>>>>>>>++>+++>+++>+>>+++>+++>+>+++>+>+++>+>++>+++>>>+>+>+>+>++>+++>+>+>>+++>>>>>>>+>+>>>+>+>++>+++>+++>+>>+++>+++>+>+++>+>++>+++>++>>+>+>++>+++>+>+>>+++>>>+++>+>>>++>+++>+++>+>>+++>>>+++>+>+++>+>>+++>>+++>>+[[>>+[>]+>+[<]<-]>>[>]<+<+++[<]<<+]>>>[>]+++[++++++++++>++[-<++++++++++++++++>]<.<-<]
#

'''


def test_run(main=False):

    fout = StringIO.StringIO()
    bfck = BrainFck(
        fout=fout,
        linemode=True,
        multiline=True,
        comments=True,
        breakline=True)

    bfck.run(test_program)

    if main:
        print(fout.getvalue())
        print('len fout:', len(fout.getvalue()))
        print('len output:', len(test_output))

    assert fout.getvalue() == test_output

if __name__ == '__main__':
    test_run(main=True)
