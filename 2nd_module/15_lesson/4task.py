class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_dict = {}
        self.order = []  

    @property
    def cache(self):
        return [(key, self.cache_dict[key]) for key in self.order]

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        if key in self.cache_dict:
            self.order.remove(key)
        elif len(self.cache_dict) >= self.capacity:
            oldest_key = self.order.pop(0)
            self.cache_dict.pop(oldest_key)

        self.cache_dict[key] = value
        self.order.append(key)

    def get(self, key):
        if key in self.cache_dict:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_dict[key]
        else:
            return None

    def print_cache(self):
        print("LRU Cache:")
        for key, value in self.cache:
            print(f"{key} : {value}")

cache = LRUCache(3)
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
cache.print_cache()
print(cache.get("key2"))
cache.cache = ("key4", "value4")
cache.print_cache()
