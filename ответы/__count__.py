import os
import re


def pause():
    input("Press the <ENTER> key to continue...")


def open_utf8(name, mode='r'):
    return open(name, mode, encoding='utf8')


def countlines(file):
    c, fi = 0, iter(open_utf8(file))
    try:
        while True:
            next(fi)
            c += 1
    except StopIteration:
        pass
    return c


Q_REGEX = re.compile(r'[А-Я]-[0-9]{2}\.tex')


def main():
    for f in os.listdir('.'):
        if Q_REGEX.match(f) and countlines(f) != 10:
            print(f)


if __name__ == '__main__':
    main()
    pause()
