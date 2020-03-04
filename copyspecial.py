#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

__author__ = "Koren Nyles, Sean Bailey, Chris Wilson, Julita Marshall"
__helped__ = "geeterista"

import re
import os
import shutil
# import subprocess didn't use
import argparse

# get_special_paths(dir) -- returns a list of the
# absolute paths of the special
# files in the given directory.


def get_spec_paths(dir):
    """ given dir name returns the appended
    results of the search for special files"""
    result = []
    file_directory = os.listdir(dir)
    for file_name in file_directory:
        if re.search(r'__\w+__', file_name):
            result.append(file_name)
    return result

# copy_to(paths, dir) given a list of paths,
# copies those files into the given directory


def copy_to_dir(path, files):
    """ copies path of special files to
    a directory (only if --todir is an arg)"""
    cwd = os.getcwd()
    if not os.path.exists(path):
        create_dir = 'mkdir -p {0}'.format(path)
        os.system(create_dir)
    else:
        print("Path exists")
    for file in files:
        os.chdir(cwd)
        shutil.copy(file, path)


# zip_to(paths, zippath) given a list of paths,
# zip those files up into the given zipfile


def zip_to_file(paths, zippath):
    """creates zipfile from special path"""
    paths = list(paths)
    command = "zip -j {} {}".format(zippath, ' '.join(paths))
    print("Command I'm going to do: ")
    print(command)
    os.system(command)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    parser.add_argument('fromdir', help='dir to look for local files')
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    all_paths = get_spec_paths(args.fromdir)

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something
    # is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions
    if args.todir:
        copy_to_dir(args.todir, all_paths)
    if args.tozip:
        zip_to_file(all_paths, os.path.join(os.getcwd(), args.tozip))

    if not args.todir and not args.tozip:
        for file in all_paths:
            print(os.path.abspath(file))


if __name__ == "__main__":
    main()
