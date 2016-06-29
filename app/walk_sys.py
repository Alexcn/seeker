#!/usr/bin/env python3
# encoding: utf-8

import os
import os.path
import hashlib


def is_writeable(path, check_parent=False):
    '''
    Check if a given path is writeable by the current user.

    :param path: The path to check
    :param check_parent: If the path to check does not exist, check for the
           ability to write to the parent directory instead
    :returns: True or False
    '''

    if os.access(path, os.F_OK) and os.access(path, os.W_OK):
        # The path exists and is writeable
        return True

    if os.access(path, os.F_OK) and not os.access(path, os.W_OK):
        # The path exists and is not writeable
        return False

    # The path does not exists or is not writeable

    if check_parent is False:
        # We're not allowed to check the parent directory of the provided path
        return False

    # Lets get the parent directory of the provided path
    parent_dir = os.path.dirname(path)

    if not os.access(parent_dir, os.F_OK):
        # Parent directory does not exit
        return False

    # Finally, return if we're allowed to write in the parent directory of the
    # provided path
    return os.access(parent_dir, os.W_OK)


def is_readable(path):
    '''
    Check if a given path is readable by the current user.

    :param path: The path to check
    :returns: True or False
    '''

    if os.access(path, os.F_OK) and os.access(path, os.R_OK):
        # The path exists and is readable
        return True

    # The path does not exist
    return False


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
                    curent_file = os.path.join(ps_one[0], ps_file)
                    if os.path.isfile(curent_file) and is_readable(curent_file):
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
    #filepath = '/Users/light/'
    filepath = '/Users/light.zhang/'
    pathispath(filepath)


if __name__ == '__main__':
    main()
