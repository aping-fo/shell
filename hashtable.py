class HashTable(object):
    _empty = object()
    _deleted = object()

    def __init__(self, size=16):
        self.size = size
        self._len = 0
        self._keys = [self._empty] * size
        self._values = [self._empty] * size

    def hash(self, key):
        return key % self.size

    def put(self, key, value):
        initial_hash = hash_ = self.hash(key)
        while True:
            if self._keys[hash_] is self._empty or self._keys[hash_] is self._deleted:
                self._keys[hash_] = key
                self._values[hash_] = value
                self._len += 1
                return
            elif self._keys[hash_] == key:
                self._keys[hash_] = key
                self._values[hash_] = value
                return

    def get(self, key):
        hash_ = self.hash(key)
        while True:
            if self._keys[hash_] is self._empty:
                # That key was never assigned
                return None
            elif self._keys[hash_] == key:
                # key found
                return self._values[hash_]

    def remove(self, key):
        hash_ = self.hash(key)
        while True:
            if self._keys[hash_] is self._empty:
                # That key was never assigned
                return None
            elif self._keys[hash_] == key:
                # key found, assign with deleted sentinel
                self._keys[hash_] = self._deleted
                self._values[hash_] = self._deleted
                self._len -= 1
                return
