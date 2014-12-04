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
