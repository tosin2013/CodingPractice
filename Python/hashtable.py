class Hashitem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size) ]
        self.count = 0

    def _hash(self, key):
        multi = 1
        hashvalue = 0
        for ch in key:
            hashvalue += multi * ord(ch)
            multi += 1
        #return the remainder of the by dividing hash by the size of the table
        return hashvalue % self.size

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def put(self, key, value):
        item = Hashitem(key, value)
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h + 1) % self.size
        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item

    def get(self, key):
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            else:
                return None
            h = (h + 1) % self.size

ht = HashTable()
ht["word1"]="drinks"
ht["healthy"]="water"
ht["tasty"]= "Lemondade"
ht["da"]="do not"
ht["ga"]="collide"

for key in ("word1", "healthy", "tasty","nothere","da", "ga"):
    value = ht[key]
    print value

print("The number of elements is: {}".format(ht.count))
