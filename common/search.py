#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import os.path
import time
import hashlib


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


def get_hexdigest(filename):
    hashobj = hashlib.md5()
    with open(filename, 'rb') as f:
        hashobj.update(f.read())
    md5_str = hashobj.hexdigest()

    return md5_str

if __name__ == '__main__':
    filename = '/Users/light.zhang/log/slow.log'
    start_time = time.clock()
    md5_str = get_hexdigest(filename)
    end_time = time.clock()
    print('hash of %s: %s' % (filename, md5_str))
    print('duration: %.4f seconds' % (end_time - start_time))
