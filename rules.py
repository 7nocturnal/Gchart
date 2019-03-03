# coding=utf8

from models import *
from config import *


def is_fastbin_chunk(chunk):    # 检查一个堆块是否属于 fastbin
    if (chunk.size > FASTBIN_MAX_SIZE):    # 注意 size 是经过 request2size 转化后的
        chunk.bin = 0
        return False
    else:
        chunk.bin = 1
        return True


def is_smallbin_chunk(chunk):    # 检查一个堆块是否属于 smallbin
    if chunk.size > SMALLBIN_MAX_SIZE:    # 注意 size 是经过 request2size 转化后的
        chunk.bin = 4    # large bin chunk
        return False
    elif chunk.size <= FASTBIN_MAX_SIZE and chunk.is_consolidate == 1:    # chunk 可能是由 consolidate 合并到 smallbin 中的
        chunk.bin = 2
        return True
    else:
        chunk.bin = 2
        return True


def is_fastbin_empty():
    if len(fast_bin) == 0:
        return True
    else:
        return False


def is_smallbin_empty():
    if len(small_bin) == 0:
        return True
    else:
        return False


def is_unsortedbin_empty():
    if len(unsorted_bin) == 0:
        return True
    else:
        return False

