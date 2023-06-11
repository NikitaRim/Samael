import os
import pytest
from task5 import KeyValueStorage

def test_1():
    storage = KeyValueStorage('D:/Курс/Homework7/prim1.txt')
    assert storage['name'] == 'kek'

def test_2():
    storage = KeyValueStorage('D:/Курс/Homework7/prim1.txt')
    assert storage.song_name == 'shadilay'

def test_3():
    storage = KeyValueStorage('D:/Курс/Homework7/prim1.txt')
    assert storage.power == 9001

def test_4():
    storage = KeyValueStorage('D:/Курс/Homework7/prim1.txt')
    storage['city'] = 'Moscow'
    assert storage.cat_name == 'Moscow'

test_file_name = 'test.txt'
test_file_contents = 'name=John\nage=30\nheight=1.75\nweight=70.5\nsong_name=let_it_be\n'


@pytest.fixture(scope='module')
def create_test_file():
    with open(test_file_name, 'w') as f:
        f.write(test_file_contents)
    yield
    os.remove(test_file_name)


def test_key_value_storage(create_test_file):
    kvs = KeyValueStorage(test_file_name)
    assert kvs.name == 'John'
    assert kvs.age == 30
    assert kvs.height == 1.75
    assert kvs.weight == 70.5
    assert kvs.song_name == 'let_it_be'
    with pytest.raises(AttributeError):
        kvs.nonexistent_key
    assert kvs['name'] == 'John'
    assert kvs['age'] == 30
    assert kvs['height'] == 1.75
    assert kvs['weight'] == 70.5
    assert kvs['song_name'] == 'let_it_be'
    with pytest.raises(KeyError):
        kvs['nonexistent_key']