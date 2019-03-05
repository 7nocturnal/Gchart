# def request2size(size):
#     SIZE_SZ = 8
#     MALLOC_ALIGN_MASK = 2 * SIZE_SZ - 1
#     MINSIZE = 32
#     if (size + SIZE_SZ + MALLOC_ALIGN_MASK < MINSIZE):
#         new_size = MINSIZE
#     else:
#         new_size = (size + SIZE_SZ + MALLOC_ALIGN_MASK) & (~MALLOC_ALIGN_MASK)
#     return new_size
