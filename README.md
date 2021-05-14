This repository contains a Python implementation of the MD5 algorithm, which
is a message digest algorithm widely used as a hash function for producing a
128-bit hash value.

Important notes
===============

MD5 suffers from multiple security vulnerabilities such as collision attacks,
so it should never be used as a cryptographic hash function anymore. It can
still be used as a checksum for data integrity verification.

This is a naive implementation to understand the algorithm, so without focus
on security or performance. For any kind of production software, always use
mature libraries and utilities for hashing, such as `md5sum` on Linux.

Prerequisites
=============

In order to use the code, you need Python 3.9 and Pipenv. Clone the repository
and run the following in the root directory to open a new shell subprocess:

    $ pipenv install
    $ pipenv shell

Command line interface
======================

The command line interface is provided to quickly compute the MD5 hash for
a given string. For example, the MD5 hash for the string "Hello world" is
computed as follows:

    $ python cli.py "Hello world"
    3e25960a79dbc69b674cd4ec67a72c62

You can check the correctness using the `md5sum` utility on Linux:

    $ echo -n "Hello world" | md5sum | cut -d ' ' -f 1
    3e25960a79dbc69b674cd4ec67a72c62

Unit tests
==========

You can run the unit tests with `python -m unittest`.

License
=======

The implementation is licensed under the MIT license. Refer to the `LICENSE`
file for more information.
