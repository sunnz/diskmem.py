#!/usr/bin/env python2

import os
import re


def main():
    m = meminfo()
    mem_total = int(m['MemTotal']) / 1024
    mem_free = int(m['MemFree']) + int(m['Buffers']) + int(m['Cached'])
    mem_usage = (int(m['MemTotal']) - mem_free) / 1024
    swap_total = int(m['SwapTotal']) / 1024
    swap_usage = (int(m['SwapTotal']) - int(m['SwapFree'])) / 1024
    disk_total_bytes = int(diskcap('/'))
    disk_free = int(diskfree('/'))
    disk_total, dt_suffix = humanise_bytes(disk_total_bytes)
    disk_usage, du_suffix = humanise_bytes(disk_total_bytes - disk_free)
    print('Memory usage')
    print("\t{0}/{1} MB of used memory.".format(mem_usage, mem_total))
    print('Swap usage')
    print("\t{0}/{1} MB of used swap.".format(swap_usage, swap_total))
    print('Disk usage:')
    print("\t{0:.2f} {1}/{2:.2f} {3} of used disk space.".format(disk_usage, du_suffix, disk_total, dt_suffix))

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
