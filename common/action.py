#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#    > Author: Light.Zhang
#    > Mail: zhilight@gmail.com
#    > Created Time: 16/01/18 23:57:13

# 计算大文件的md5值

import hashlib
import os,sys

# 参考代码
# http://pythoncn.sinaapp.com/news/91.html
def md5_for_file(f, block_size=2**10):
    md5 = hashlib.md5()
    while True:
        data = f.read(blocksize)
        if not data:
            break;
        md5.update(data)
    return md5.digest()


def md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, 'r+b') as f:
        for block in iter(lambda: f.read(blocksize), ''):
            hash.update(block)
    return hash.hexdigest()


# 检测文件md5的值
# 参考 http://www.lxway.com/840559214.htm

# 简单的测试一个字符窜的md5值
def GetStrMd5(src):
    m0 = hashlib.md5()
    m0.update.md5(src)
    print(m0.hexdigest())

# 获取大文件的md5值
def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = file(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()

def CalcSha1(filepath):
    with open(filepath, 'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        print(hash)
        return hash

def CalMD5(filepath):
    with open(filepath, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        print(hash)
        return hash

if __name__ == '__main__':
    if len(sys.argv) == 2:
        hashfile = sys.argv[1]
        if not os.path.exists(hashfile):
            hashfile = os.path.join(os.path.dirname(__file__), hashfile)
            if not os.path.exists(hashfile):
                print("Cannot found file")
            else:
                CalcMd5(hashfile)
        else:
            CalcMd5(hashfile)
    else:
        print('no file')



