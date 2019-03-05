# coding=utf8

from models import *
from config import *


def is_fastbin_chunk(chunk):    # 检查一个堆块是否属于 fastbin
    if (chunk.size > FASTBIN_MAX_SIZE):    # 注意 size 是经过 request2size 转化后的
        chunk.bin = UNDEFINED
        return False
    else:
        chunk.bin = FASTBIN_CHUNK
        return True


def is_smallbin_chunk(chunk):    # 检查一个堆块是否属于 smallbin
    if chunk.size > SMALLBIN_MAX_SIZE:    # 注意 size 是经过 request2size 转化后的
        chunk.bin = LARGEBIN_CHUNK    # large bin chunk
        return False
    elif chunk.size <= FASTBIN_MAX_SIZE and chunk.is_consolidate == 1:    # chunk 可能是由 consolidate 合并到 smallbin 中的
        chunk.bin = SMALLBIN_CHUNK
        return True
    else:
        chunk.bin = SMALLBIN_CHUNK
        return True


def is_fastbin_empty():
    outside_i = 0
    for outside_i in range(7):
        if len(fast_bin[outside_i]) == 0:
            continue
        else:
            return False
    return True


def is_smallbin_empty():
    outside_i = 0
    for outside_i in range(2, 64):
        if len(small_bin[outside_i]) == 0:
            continue
        else:
            return False
    return True


def is_unsortedbin_empty():
    if len(unsorted_bin) == 0:
        return True
    else:
        return False


def size2fastbin_index(size):    # 计算当前 size 在链表中的 index
    if SIZE_SZ == 8:
        offset = 4
    elif SIZE_SZ == 4:
        offset = 3
    else:
        print("[!] Error! Wrong SIZE_SZ detected when converting size to fastbin_index.")
        exit(0)
    index = (size >> offset) - 2
    if index < 0 or index > 6:
        print("[!] Error! Something wrong when trying to convert size to fastbin_index.\nMaybe the size is illegal！\n Current size is %d." % size)
        exit(0)
    return index


def size2smallbin_index(size):    # 计算当前 size 在链表中的 index
    if MALLOC_ALIGNMENT == 16:
        index = size >> 4
        if index < 2 or index > 62:
            print("[!] Error! Something wrong when trying to convert size to smallbin_index.\nMaybe the size is illegal！\n Current size is %d." % size)
            exit(0)
        return index
    else:
        index = size >> 3 + (MALLOC_ALIGNMENT > 2 * SIZE_SZ)    # 保留
        return index


def process_fastbin(chunk):
    index_in_fastbin = size2fastbin_index(chunk.size)
    if len(fast_bin[index_in_fastbin]) == 0:
        return -1    # can't find a suitable chunk in fastbin
    try:
        victim = fast_bin[index_in_fastbin][0]    # Take the first chunk
    except IndexError:
        print("[!] Error! Something wrong when processing fastbin.")
        exit(0)
    if size2fastbin_index(victim.size) != index_in_fastbin:
        print("[!] Warning! Fastbin chunk error status!\nMaybe you are working on fastbin attack but failed?")
        exit(0)
    fast_bin[index_in_fastbin].pop(0)    # delete the one we take
    return victim


def process_smallbin(chunk):
    index_in_smallbin = size2smallbin_index(chunk.size)
    if len(small_bin[index_in_smallbin]) == 0:
        pass    # can't find a suitable chunk in smallbin,   but is smallbin init ?
                # TODO     add consolidate or process unsorted bin
    try:
        victim = small_bin[index_in_smallbin][-1]   # take last chunk
    except IndexError:
        print("[!] Error! Something wrong when processing smallbin.")
        exit(0)
    small_bin[index_in_smallbin].pop()    # delete the one we take
    return victim