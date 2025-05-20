from add_numbers import *
def test_adding_even_numbers_returns_even_number():
    number = add(2, 2)
    assert number == 4
def test_adding_two_negative_numbers_returns_negative_number():
    temp = add(-2, -2)
    assert temp == -4

def test_5_is_odd():
    assert is_odd(3)

def test_4_is_even():
    assert is_even(3) is False