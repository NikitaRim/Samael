import pytest
from task3 import combinations


@pytest.mark.parametrize(
    "list,res_list",
    [
        ([[1, 2], [3, 4]], [(1, 3), (1, 4), (2, 3), (2, 4)])
    ],
)
def test_combinations(list, res_list):
    result = combinations(*list)
    assert result == res_list