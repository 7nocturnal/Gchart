# coding=utf8

t_chunk_list = []           #物理上的chunk
fast_bin = [[],[],[],[],[],[],[],[],[],[]]              #fast_bin

small_bin = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[], \
            [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[], \
            [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[], \
            [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]               #smallbin

large_bin = []              #large_bin  保留字段
unsorted_bin = []           #unsorted_bin


class Chunk():
    def __init__(self):
        # 堆块的基本结构
        self.id = 0
        self.prev_size = 0
        self.size = 0
        self.fd = 0
        self.bk = 0
        self.prev_inuse = 0
        self.is_consolidate = 0
        # 下面两个是保留字段
        self.fd_nextsize = 0
        self.bk_nextsize = 0
        
        # 堆块的归属
        self.bin = 0   # 1 表示 fastbin   2 表示 smallbin
                       # 3 表示 unsorted bin  4  表示 largebin
