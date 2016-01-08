#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import os.path
import sys
import codecs

#reload(sys)
sys.setdefaultencoding('utf-8')

def deep_search(path):
    dir_content = os.listdir(path)
    for name in dir_content:
        if os.path.isfile(name):
            print('%s is a common file and absolute path is %s' % (name, os.path.abspath(name)))
        else:
            print('%s is a directory and absolute path is %s' % (name, os.path.abspath(name)))


def deep_search2(path):
    dir_content = os.listdir(path)
    dir_list = []
    file_list = []
    for name in dir_content:
        if os.path.isfile(name):
            file_list.append(os.path.join(path, name))
        elif os.path.isdir(os.path.join(path, name)):
            dir_list.append(os.path.join(path, name))
    return dir_list, file_list


def deep_search_list(dir_list):
    for dir in dir_list:
        dir_content = os.listdir(dir)
        print('***************************************************')
        print(dir)
        print(dir_content)


if __name__ == '__main__':
    dir_list, __ = deep_search2('C:\\')
    if 'C:\\bootmgr' in dir_list:
        print('OK')
    if os.path.isdir('C:\\bootmgr'):
        print('OK')
    print(dir_list)
    print(os.listdir('C:\\dl'))

    deep_search_list(dir_list)



