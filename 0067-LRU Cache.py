class LRUCache:
    def __init__(s,c: int):
        s.d=OrderedDict()
        s.c=c
    def get(s,k: int) -> int:
        if k not in s.d:
            return -1
        s.d.move_to_end(k)
        return s.d[k]

    def put(s, k: int, v: int) -> None:
        if k in s.d:
            s.d.move_to_end(k)
        s.d[k]=v
        if len(s.d)>s.c:
            s.d.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''SOLVED BY ADIT MUGDHA DAS'''