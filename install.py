#!/usr/bin/python
import os
import sys
import generator

def __main__():
    if os.geteuid() == 0:
        exit("This script can't be ran as root!")

    generator.generate()

    # but patcher do need to run as root
    print(sys.executable)
    print(os.getcwd())
    os.execlp("pkexec", sys.executable, os.getcwd() + "/patcher.py")

if __name__ == "__main__":
    __main__()

