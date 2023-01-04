#!/usr/bin/python3
from ctypes import *
ugwu = CDLL("./libhellowrite.so")

friday = ugwu.hello_write()
