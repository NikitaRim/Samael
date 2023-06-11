import pytest
from pathlib import Path
from typing import Optional, Callable
import os
from task3 import universal_file_counter

os.mkdir("test_files")
with open("test_files/file1.txt", "w") as f:
    f.write("Hello, world!")

with open("test_files/file2.txt", "w") as f:
    f.write("Lorem ipsum dolor sit amet.")

with open("test_files/file3.txt", "w") as f:
    f.write("This is a test file.")

def test_universal_file_counter():
    dir_path = Path("test_files")
    assert universal_file_counter(dir_path, ".txt") == 3
    assert universal_file_counter(dir_path, ".txt", tokenizer=lambda x: x.split()) == 12
    assert universal_file_counter(dir_path, ".md", tokenizer=lambda x: x.split()) == 8
    assert universal_file_counter(dir_path, ".py", tokenizer=lambda x: x.split()) == 2
    assert universal_file_counter(dir_path, ".py") == 2
    assert universal_file_counter(dir_path, ".md") == 4
    assert universal_file_counter(dir_path, ".docx") == 0

if __name__ == '__main__':
    pytest.main()