"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
№>>> universal_file_counter(test_dir, "txt")
6
№>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
from pathlib import Path
from typing import Optional, Callable
import os

def universal_file_counter(dir_path: Path, file_extension: str, tokenizer: Callable = None) -> int:
    count = 0
    for path in dir_path.glob('**/*'):
        if path.is_file() and path.suffix == file_extension:
            with open(path) as f:
                for line in f:
                    if tokenizer is None:
                        count += 1
                    else:
                        tokens = tokenizer(line)
                        count += len(tokens)
    return count

