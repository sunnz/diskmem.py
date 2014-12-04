diskmem.py
==========

simple centos 6.6 compatible python cli tool that displays current usage of memory, swap and diskspace for /.

## requirement

* python 2.6 or higher - it is most likely already installed if you are running
linux, especially centos/rhel, since yum is written in python.
* argparse - python 2.7 or above have argparse build in. otherwise install it
via pip:

if you don't have pip:

```
sudo yum install python-pip
```

install with pip:

```
sudo pip install argparse
```

## usage

```
./diskmem.py
```

--csv flag to output in csv format:

```
./diskmem.py --csv
```

the csv format option would display something like:

```
0.56,0.01,0.16,992 MB,1023 MB,42.27 GB,1417649899.1
```

which we can easily append to a file to keep a record of ongoing usage.

## license

diskmem.py is available under the isc license:

> Copyright (c) 2014, sunnz (https://github.com/sunnz)
> 
> Permission to use, copy, modify, and/or distribute this software for any
> purpose with or without fee is hereby granted, provided that the above
> copyright notice and this permission notice appear in all copies.
> 
> THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
> WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
> MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
> ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
> WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
> ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
> OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
