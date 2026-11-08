from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.od = OrderedDict() 
        self.length = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.od: 
            self.od.move_to_end(key)
            return self.od[key]
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od.move_to_end(key)
            self.od[key] = value
        elif self.length == self.capacity:
            self.od.popitem(last=False)
            self.od[key] = value
        else: 
            self.length += 1
            self.od[key] = value