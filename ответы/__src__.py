import os
import re


def pause():
    input('Press the <ENTER> key to continue...')


def open_utf8(name, mode='r'):
    return open(name, mode, encoding='utf8')


def cpy_to(src, dst, line):
    fr = open_utf8(src)
    to = open_utf8(dst, 'w')
    for s in fr:
        if s.rstrip() == '%':
            to.write(line)
        else:
            to.write(s)

pause()

qit = iter(open_utf8('q.tex'))

while True:
    pass

pause()