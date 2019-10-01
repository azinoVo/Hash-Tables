# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Collisions should print a warning for right now
        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        # hash the key and get an integer index within storage to put the value
        hashed = self._hash_mod(key)
        # add to that particular index
        # If value already exists
        if self.storage[hashed] is not None:
            current_node = self.storage[hashed]
            # If next node has a value - this while handles updating dupe keys
            # Return when update complete - if we reach the end without updates
            # add the new LinkedPair to the end of the list
            while current_node.next:
                if current_node.key == key:
                    current_node.value = value
                    return
                else:
                    current_node = current_node.next
            # This will add a LinkedPair to the end of list if we make it out of the while loop
            current_node.next = LinkedPair(key, value)

        else:
            self.storage[hashed] = LinkedPair(key, value)
        

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hashed = self._hash_mod(key)

        if self.storage[hashed] is not None:
            self.storage[hashed] = None

        print("This key does not have a value or is None!")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hashed = self._hash_mod(key)
        
        if self.storage[hashed] is not None:
            # return self.storage[hashed].value
            current_node = self.storage[hashed]
            while current_node.next:
                if current_node.key == key:
                    return current_node.value
                else:
                    current_node = current_node.next
            # Handles the last node in the list since while loop will stop abruptly
            if current_node.key == key:
                return current_node.value
            return None

        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        
        for pair in self.storage:
            if pair is not None:
                new_index = self._hash_mod(pair.key)
                new_storage[new_index] = pair
            
        self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
