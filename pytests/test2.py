import pytest
from task2 import Order, MorningDiscount, ElderDiscount

def test_morning_discount():
    order = Order(100, MorningDiscount())
    assert order.final_price() == 70

def test_elder_discount():
    order = Order(100, ElderDiscount())
    assert order.final_price() == 50

def test_no_discount():
    order = Order(100, None)
    assert order.final_price() == 100

def test_invalid_discount_strategy():
    with pytest.raises(TypeError):
        order = Order(100, "invalid_discount_strategy")
        order.final_price()