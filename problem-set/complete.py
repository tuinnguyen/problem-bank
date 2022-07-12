#!/usr/bin/env python3

import os
import sys


def get_current_path():
    return os.getcwd()


def terminal(command):
    os.system(command)


def file_exist(file_name):
    path = get_current_path() + "/" + file_name + ".cpp"
    return os.path.exists(path)


#inputs = list(sys.argv)

#file_name = inputs[1]


REMOVE_FILES = [
    "compile.py",
    "compile",
    "gen.cpp",
    "random-functions.h",
    "input.txt",
    "complete.py",
    "complete",
]

for FILE in REMOVE_FILES:
    command = "rm " + FILE
    terminal(command)