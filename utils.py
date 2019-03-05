# coding=utf8

from models import *
from rules import *

def request2size(size):    # 转换用户请求的 size 到实际的 chunk size
    SIZE_SZ = 8
    MALLOC_ALIGN_MASK = 2 * SIZE_SZ - 1
    MINSIZE = 32
    if (size + SIZE_SZ + MALLOC_ALIGN_MASK < MINSIZE):
        new_size = MINSIZE
    else:
        new_size = (size + SIZE_SZ + MALLOC_ALIGN_MASK) & (~MALLOC_ALIGN_MASK)
    return new_size


def mem2chunk(size, content):     # 将用户的请求转换为实际的堆块(实例化堆块)  
    chunk = Chunk()               # TODO
    new_size = request2size(size)
    chunk.size = new_size
    if is_fastbin_chunk(chunk):
        chunk.prev_inuse = 1    # TODO
    elif is_smallbin_chunk(chunk):
        pass    # TODO                                 # new idea : 每次分配堆块在变化的是 size，不变的是流程，那么能否将一个走到底(比如最开始分配堆块时只能从 TOP 切割)
                                                       # 的函数调用链放在列表中，每次分配堆块的时候都按照列表走一遍？
    elif not is_fastbin_empty():
        pass    # consolidate TODO
    if not is_unsortedbin_empty():
        pass    # process unsorted bin
    # TOP CHUNK  TODO

    #chunk.prev_inuse = 1
    length = size - 0x10
    content_len = len(content)
    if content_len > length :
        overflow_len = content_len - length
    t_chunk_list.append(chunk)
    return


def chunk2bin(chunk):    #判断free后进入的bin
    if is_fastbin_chunk(chunk):    # TODO
        fast_bin.append(chunk)
    elif is_smallbin_chunk(chunk):
        unsorted_bin.append(chunk)
    return