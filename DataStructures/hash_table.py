class MyHashTable(object):
    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        """
        Create a hash based on the length of the initialized data.

        :type key: string
        :rtype: str
        """
        hash = 0
        for i in range(1, len(key) - 1):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash

    def set(self, key, value):
        """
        Add a key value pair to the data property.

        Get the address from the hash function and check 
        what's there. If that 'address' is set to None, 
        insert an empty bucket. Insert the key value pair 
        into the this bucket.

        :type key: string
        :type value: any
        """
        address = self._hash(key)
        if self.data[address] is None:
            self.data[address] = []
        self.data[address].append((key, value))

    def get(self, key):
        """
        Retrieve a value from the hash.

        Use the key to find the correct bucket. 
        Search each item in the bucket for the key value pair. 
        If found, return the value. Otherwise return None.

        :type key: string
        :rtype: any or None
        """
        address = self._hash(key)
        current_bucket = self.data[address]
        if current_bucket is None:
            return None
        for item in current_bucket:
            if item[0] == key:
                return item[1]
        return None

    def keys(self):
        """
        Retrieve all the keys in the data.

        :rtype: List
        """
        keys = []
        for item in self.data:
            if item is not None:
                keys.append(item[0][0])
        return keys

    def values(self):
        """
        Retrieve all the values in the data.

        :rtype: List
        """
        values = []
        for item in self.data:
            if item is not None:
                values.append(item[0][1])
        return values


def main():
    hash = MyHashTable(50)
    hash.set('grapes', 10000)
    hash.set('apples', 54)
    hash.set('oranges', 2)
    print('hash.data', hash.data)

    grapes = hash.get('grapes')
    print('grapes:', grapes)

    print(hash.keys())
    print(hash.values())


if __name__ == '__main__':
    main()
    print('done!')
