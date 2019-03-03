#coding=utf-8

from functools import wraps
from utils import *
from models import *


def top_add(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
#       size_list.append(args[1])
        size = request2size(args[1])
        content = args[2]
        mem2chunk(size,content)
        
        return func(*args, **kwargs)
    return with_logging

def top_delete(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        index = args[0]
        free(index)
        return func(*args, **kwargs)
    return with_logging


def show():
    print("----------------------")
    for i in t_chunk_list:
        print("* pre_size is " + str(i.prev_size))
        print("* size is " + str(i.size))
        print("* fd is " + str(i.fd))
        print("----------------------")


def fastbin():
    for i in fast_bin:
        print(hex(i.size) + " -> "),
    print("\n")





def free(index):
    chunk  = t_chunk_list[index]
    chunk2bin(chunk)
