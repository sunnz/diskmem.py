#!/usr/bin/env python2

import os


def main():
    print(diskfree('/'))

def diskfree(path):
    """
    Returns the number of free bytes on the drive that path is on.
    """
    s = os.statvfs(path)
    return s.f_bsize * s.f_bavail

if __name__ == '__main__':
    main()
