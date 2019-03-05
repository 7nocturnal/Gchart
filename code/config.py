# coding=utf8

OS = 1
SIZE_SZ = 8
MALLOC_ALIGNMENT = 2 * SIZE_SZ
MALLOC_ALIGN_MASK = 2 * SIZE_SZ - 1
MINSIZE = 32

FASTBIN_MAX_SIZE = 0x80
SMALLBIN_MAX_SIZE = 0x3f0

FASTBIN_CHUNK = 1
SMALLBIN_CHUNK = 2
UNSORTEDBIN_CHUNK = 3
LARGEBIN_CHUNK = 4
UNDEFINED = 0