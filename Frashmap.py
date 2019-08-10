# Implementation of Hashmap from scratch
class Frashmap:
    def __init__(self, size=128):
        self.size = size
        self.table = [[] for i in range(self.size)]
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, value):
        self.put(key, value)
	
    def __repr__(self):
        return "\n".join(["{}: {}".format(index, bucket) for index, bucket in enumerate(self.table) if len(bucket)>0])
        
    def get(self, key):
#         Returns the value for a given key if present, else returns None
        lookup = KV_pair(key)
        value = None
        bucket = self._get_bucket(lookup)
        for kv_pair in self.table[bucket]:
            if kv_pair.key == lookup.key:
                return kv_pair
        return None
        
    def put(self, key, value):
#         Adds a key-value pair to the table
        kv = KV_pair(key, value)
        bucket = self._get_bucket(kv)
        for i, kv_pair in enumerate(self.table[bucket]):
            if kv_pair.key == key:
                del self.table[bucket][i]
            break
        self.table[bucket].append(kv)
    
    def delete(self, key):
#         Deletes a KV_pair for a given key if present
        kv = KV_pair(key)
        bucket = self._get_bucket(kv)
        for i, kv_pair in enumerate(self.table[bucket]):
            if kv_pair.key == kv.key:
                del self.table[bucket][i]
                break
            
    def get_size(self):
#         Returns the number of entries in the hashmap
        table_size = 0
        for bucket in self.table:
            if len(bucket) != 0:
                for entry in bucket:
                    if isinstance(entry, KV_pair):
                        table_size += 1
        return table_size
    
    def _get_bucket(self, kv_pair):
#         Returns the bucket that a KV_pair should be added to based on the size of the table
        if not isinstance(kv_pair, KV_pair):
            raise TypeError("can only get bucket for KV_pairs")
        return kv_pair.hash % self.size

class KV_pair:
#         Simple data structure for a key, value pair
    def __init__(self, key, value=None):
        self.key = str(key)
        self.value = str(value) if value else None
        self._hash_value()
        
    def __eq__(this, that):
#         override equals method to compare based on key
        return this.key == that.key
    
    def __repr__(self):
#         Returns the value for a given key if present, else returns None
        return "{0.key}: {0.value}".format(self)
            
    def _hash_value(self):
        hash_value = 1
        for i in range(len(self.key)):
            hash_value += ord(self.key[i]) * 17
        self.hash = hash_value