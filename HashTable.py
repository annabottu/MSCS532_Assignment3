import random

class HashTable:
    # This class implements a hash table with chaining and universal hashing.
    # It uses a universal hash function to distribute keys uniformly across the table.
    # The table is initialized with a specified size, which should be a prime number for better
    # distribution of keys.
    def __init__(self, table_size=101):
        # Ensure the table size is a prime number for better distribution
        if table_size < 1:
            raise ValueError("Table size must be a positive integer")
        if table_size % 2 == 0:
            raise ValueError("Table size should be an odd prime number")
        # Initialize the hash table with the specified size
        self.table_size = table_size 
        # Create a list of empty buckets for chaining
        self.table = [[] for _ in range(table_size)] 

        # Universal hashing parameters
        # p is a large prime number, a and b are random integers used in the hash
        self.p = 109345121 
        # Randomly select a and b for the universal hash function
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    # Universal hash function to compute the index for a given key
    def _hash(self, key):
       # Universal hash function to compute the index for a given key
       # It uses the formula: h(k) = ((a * hash(k) + b) % p) % table_size
       # where a and b are random integers, p is a large prime number,
       # and hash(k) is the built-in hash function for the key
        return ((self.a * hash(key) + self.b) % self.p) % self.table_size

    # Insert a key-value pair into the hash table
    def insert(self, key, value):
        # If the key already exists, update its value.
        index = self._hash(key)
        # Use chaining to handle collisions
        # Each bucket is a list that contains tuples of (key, value)
        if not self.table[index]:
            self.table[index] = []
        bucket = self.table[index]

        # Check if the key already exists in the bucket
        # If it does, update the value; if not, append a new key-value pair
        for i, (k, v) in enumerate(bucket):
            # If the key already exists, update its value
            if k == key:
                # Update the value for the existing key
                bucket[i] = (key, value)  
                return

        # If the key does not exist, append a new key-value pair
        # Append the new key-value pair to the bucket
        bucket.append((key, value))

    # Search for a key in the hash table
    def search(self, key):
        # Search for a key in the hash table and return its value if found
        index = self._hash(key)
        bucket = self.table[index]
        # Iterate through the bucket to find the key
        # If the key is found, return its value; otherwise, return None
        for k, v in bucket:
            if k == key:
                return v
        return None

    # Delete a key from the hash table
    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        # Iterate through the bucket to find the key
        # If the key is found, remove it from the bucket
        # If the key is not found, do nothing
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

    # String representation of the hash table for easy debugging
    # It returns a string that shows the contents of each bucket
    def __str__(self):
        return "\n".join(f"{i}: {bucket}" for i, bucket in enumerate(self.table) if bucket)

