#!/usr/bin/env python2

import os
import re


def main():
    m = meminfo()
    freemem = (int(m['MemFree']) + int(m['Buffers']) + int(m['Cached'])) / 1024
    swap = (int(m['SwapTotal']) - int(m['SwapFree'])) / 1024
    freespace, fs_suffix = humanise_bytes(int(diskfree('/')))
    capacity, cap_suffix = humanise_bytes(int(diskcap('/')))
    print('Memory:')
    print("\t" + str(freemem) + ' MB of free memory available.')
    print("\t" + str(swap) + '/' + str(int(m['SwapTotal'])/1024) + ' MB of swap used.')
    print('Disk:')
    print("\t" + str(int(freespace)) + ' ' + fs_suffix + ' out of ' + str(int(capacity)) + ' ' + cap_suffix + ' disk space available.')

def diskfree(path):
    """
    Returns the number of free bytes on the drive that path is on.
    """
    s = os.statvfs(path)
    return s.f_bsize * s.f_bavail

def diskcap(path):
    """
    Returns the total number of bytes on the drive that paht is on.
    """
    s = os.statvfs(path)
    return s.f_bsize * s.f_blocks

def meminfo():
    """
    Returns meminfo in dictionary (kB omitted).
    """
    info = {}
    with open('/proc/meminfo', 'r') as f:
        for line in f:
            w = re.split('[:\s]+', line)
            info[w[0]] = w[1]
    return info

def humanise_bytes(bytes):
    """
    Returns humanised tuple of a number, typically bytes.
    
    For example, (1, 'MB') for 1'000'000 bytes.
    """
    if bytes >= 1e12:
        return (bytes/1e12, 'TB')
    elif bytes >= 1e9:
        return (bytes/1e9, 'GB')
    elif bytes >= 1e6:
        return (bytes/1e6, 'MB')
    elif bytes >= 1e3:
        return (bytes/1e3, 'KB')
    elif bytes > 1:
        return (bytes, 'bytes')
    else:
        return (bytes, 'byte')

if __name__ == '__main__':
    main()
