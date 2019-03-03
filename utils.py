def chunk2bin(chunk):
    #判断free后进入的bin
    fast_bin.append(chunk)
    return

def request2size(size):
    new_size = size + 0x10
    return new_size


def mem2chunk(size,content):     #size is true chunk size
    chunk = Chunk()
    chunk.size = size
    chunk.prev_inuse = 1
    len = size - 0x10
    content_len = len(content)
    if content_len > len :
        overflow_len = content_len - len
    
    t_chunk_list.append(chunk)
    
    return
