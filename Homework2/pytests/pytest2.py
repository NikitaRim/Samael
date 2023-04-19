import pytest
from task2 import major_and_minor_elem

@pytest.mark.parametrize(
    "list,letter",
    [
        ([3,2,3], (3, 2))
    ],
)
def test_task2_positive(list, letter):
    result = major_and_minor_elem(list)
    assert result == letter
@pytest.mark.parametrize(
    "list,letter",
    [
        ([3,2,3], (3, 3))
    ],
)
def test_task2_negative(list, letter):
    result = major_and_minor_elem(list)
    assert result != letter