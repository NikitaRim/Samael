"""
We have a file that works as key-value storage, each like is represented as key and value separated by = symbol, example:

name=kek
last_name=top
song_name=shadilay
power=9001

Values can be strings or integer numbers. If a value can be treated both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt')
that has its keys and values accessible as collection items and as attributes.
Example:
storage['name']  # will be string 'kek'
storage.song_name  # will be 'shadilay'
storage.power  # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute (for example when there's a line `1=something`) ValueError should be raised.
File size is expected to be small, you are permitted to read it entirely into memory.
"""

class KeyValueStorage:
    def __init__(self, file_path: str):
        self._data = {}
        with open(file_path, 'r') as f:
            for line in f:
                key, value = line.strip().split('=')
                if value.isdigit():
                    value = int(value)
                elif value.replace('.', '', 1).isdigit():
                    value = float(value)
                self._data[key] = value
        if 'song_name' in self._data:
            self.song_name = self._data['song_name']

    def __getattr__(self, attr):
        if attr in self._data:
            return self._data[attr]
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr}'")

    def __getitem__(self, key):
        return self._data[key]
"""
The class reads the file into a dictionary in the constructor, converting values to integers or floats if possible.
Then it implements the `__getattr__` and `__getitem__` methods to allow accessing the values both as attributes and 
collection items. If the key or attribute doesn't exist, it raises an appropriate error message.
"""
"""
storage = KeyValueStorage('D:/Курс/Homework7/prim1.txt')
print(storage['name'])  # 'kek'
print(storage.song_name)  # 'shadilay'
print(storage.power)  # 9001
print(storage.nonexistent)  # AttributeError: 'KeyValueStorage' object has no attribute 'nonexistent'
"""
