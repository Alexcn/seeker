#!/usr/bin/env python3
# encoding: utf-8

import os
import os.path
import hashlib


def findfile(start, name=None):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))


def md5Checksum(filePath):
    fh = open(filePath, 'rb')
    m = hashlib.md5()
    while True:
        data = fh.read(8192)
        if not data:
            break
        m.update(data)
    fh.close()
    return m.hexdigest()

# 还需要解决判断文件的类型，例如socket文件不能被计算，只能计算常规的文件
def pathispath(ps_path):
    if os.path.isfile(ps_path):
        pa_path = os.path.split(ps_path)
        print(' '*32, pa_path[0])
        print(md5Checksum(ps_path))
        print(pa_path[1])
    else:
        if os.path.isdir(ps_path):
            for ps_one in os.walk(ps_path):
                print(' '*32, ps_one[0])
                for ps_file in ps_one[2]:
                    print(os.path.join(ps_one[0], ps_file))
                    print(md5Checksum(os.path.join(ps_one[0], ps_file)))



def printall(ps_path):
    if os.path.isfile(ps_path):
        pass


def visit(arg, dirname, names):
    print(dirname, arg)
    for name in names:
        subname = os.path.join(dirname, name)
        if os.path.isdir(subname):
            print('%s/' % name)
        else:
            print('%s' % name)


def main():
    filepath = '/Users/light/'
    pathispath(filepath)


if __name__ == '__main__':
    main()
