#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


import struct


def typeList():
    return {
        "52617221": EXT_RAR,
        "504B0304": EXT_ZIP
    }

＃binary convert to hex string
def bytes2hex(bytes):
    num = len(bytes)
    hexstr = u""
    for i in range(num):
        t = u"%x" % bytes[i]
        if len(t) % 2:
            hexstr += u"0"
        hexstr += t
    return hexstr.upper()


# judge file type
def filetype(filename):
    binfile = open(filename, 'rb')
    tl = typeList()
    ftype = 'unknown'
    for hcode in tl.keys():
        numOfBytes = len(hcode)
        binfile.seek(0)
        hbytes = struct.unpack_from("B"*numOfBytes, binfile.read(numOfBytes))
        f_hcode = bytes2hex(hbytes)
        if f_hcode == hcode:
            ftype = t1[hcode]
            break
    binfile.close()
    return ftype


if __name__ == '__main__':
    print(filetype('filepath'))
