import pytest
from task5 import custom_range

import string


@pytest.mark.parametrize(
    "string,list_args,res_list",
    [
        (string.ascii_lowercase, ['g'], ['a', 'b', 'c', 'd', 'e', 'f']),
        (string.ascii_lowercase, ['g', 'p'], ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']),
        (string.ascii_lowercase, ['p', 'g', -2], ['p', 'n', 'l', 'j', 'h']),
    ],
)
def test_custom_range(string, list_args, res_list):
    result = custom_range(string, *list_args)
    assert result == res_list