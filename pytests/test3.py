import pytest
from task3 import save_info, print_result, custom_sum

def test_save_info():
    def original_func():
        """This is the original function"""
        pass
    decorated_func = save_info(original_func)
    assert decorated_func.__name__ == 'original_func'
    assert decorated_func.__doc__ == 'This is the original function'
    assert decorated_func.__original_func == original_func

def test_print_result(capsys):
    @print_result
    def func():
        return 42
    func()
    captured = capsys.readouterr()
    assert captured.out.strip() == '42'
    assert func.__doc__ == 'Function-wrapper which print result of an original function'
    assert func.__name__ == 'func'
    assert func.__original_func.__name__ == 'func'

def test_custom_sum():
    assert custom_sum(1, 2, 3) == 6
    assert custom_sum([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
    assert custom_sum('aa', 'bb', 'cc') == 'aabbcc'

