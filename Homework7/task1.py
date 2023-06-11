"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

#>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import List, Union, Iterator
import os

def get_file_list(path: str) -> List[str]:
    file_list = []
    for file in os.listdir(path):
        file_list.append(os.path.join(path, file))
    return file_list

def merge_sorted_files(file_list: List[str]) -> Iterator:
    numbers = []
    for i in file_list:
        with open(file=i, encoding="utf-8", mode='r') as file:
            for row in file.readlines():
                numbers.append(int(row))
    return iter(sorted(numbers))