class HashTable:

    def __init__(self) -> None:
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def put(self, key, data):

        # Calculate the hash value, aka - index for the key in the hash
        hash_value = self.hash(key, len(self.slots))

        # If the slot is empty, insert the key and data
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        # If the slot is not empty, and the key is the same, update the data
        else:
            # If the key is the same, update the data
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            # If the key is different, rehash and insert
            else:
                nextSlot = self.rehash(hash_value, len(self.slots))
                # Loop until an empty slot is found or slot with the same key is found
                while self.slots[nextSlot] != None and self.slots[nextSlot] != key:
                    nextSlot = self.rehash(nextSlot, len(self.slots))
                
                if self.slots[nextSlot] == None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = data
                else:
                    self.data[nextSlot] = data

    def hash(self, key, size):
        # Calculate the hash using the remainder method
        return key % size
    
    def rehash(self, oldHash, size):
        return (oldHash + 1) % size
    
    def get(self, key):
        start_slot = self.hash(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        
        return data
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)

# Test the HashTable
H = HashTable()

# Store items with int keys and string dta
H[22] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"

print("data: ", H.data)
print("slots: ", H.slots)

# Modify the hash table
print(H[22])
H[22] = "duck"
print(H[22])
    
