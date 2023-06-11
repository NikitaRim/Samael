import pytest
import os
from task1 import get_file_list, merge_sorted_files

@pytest.fixture
def test_files(tmp_path=''):
    file1 = os.path.join(tmp_path, "file1.txt")
    file2 = os.path.join(tmp_path, "file2.txt")
    file3 = os.path.join(tmp_path, "file3.txt")

    with open(file1, 'w') as f:
        f.write("1\n3\n5")

    with open(file2, "w") as f:
        f.write("2\n4\n6")

    with open(file3, "w") as f:
        f.write("7\n8\n9")

    return [str(file1), str(file2), str(file3)]

def test1(tmp_path="D:/Курс/Homework7/pytests/Pytest1_data"):
    test_file1 = os.path.join(tmp_path, 'testFile1.txt')
    with open(test_file1, 'w') as f:
        f.write("1\n3\n5")
    test_file2 = os.path.join(tmp_path, 'testFile2.txt')
    with open(test_file2, 'w') as f:
        f.write("2\n4\n6\n")
    assert list(merge_sorted_files([
        test_file1,
        test_file2
    ])) == [1, 2, 3, 4, 5, 6]

def test_get_file_list(test_files):
    assert get_file_list(test_files[0]) == test_files


def test_merge_sorted_files(test_files):
    expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(merge_sorted_files(test_files)) == expected_output