# task_3.py


class Cache:
    def __init__(self):
        # Initialize the cache as an empty dictionary
        self.cache = {}

    def set(self, key, value):
        """
        Add or update a key-value pair in the cache.

        :param key: The key to be added or updated.
        :param value: The value to be associated with the key.
        """
        self.cache[key] = value

    def get(self, key):
        """
        Retrieve the value associated with a given key from the cache.

        :param key: The key whose value is to be retrieved.
        :return: The value associated with the key, or None if the key is not found.
        """
        return self.cache.get(key)

    def delete(self, key):
        """
        Remove a key-value pair from the cache.

        :param key: The key to be removed.
        """
        # Use pop to remove the key, and ignore KeyError if the key is not present
        self.cache.pop(key, None)

    def clear(self):
        """
        Clear all key-value pairs from the cache.
        """
        self.cache.clear()


# Example usage:
cache = Cache()
cache.set("name", "John")
print(cache.get("name"))  # Output: 'John'
cache.delete("name")
print(cache.get("name"))  # Output: None
cache.set("age", 30)
print(cache.get("age"))  # Output: 30
cache.clear()
print(cache.get("age"))  # Output: None


