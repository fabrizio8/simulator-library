import pytest
from simulator import *
from example_dfa import *


def test_basic_subset():
    assert subset(binary_string_all_1, traffic_light)
    assert subset(loooong, at_least_3)
    assert not subset(even_chars, my_name)
    assert not subset(even_chars, divisible_by_3)
    assert not subset(traffic_light, substring_101)
    assert not subset(substring_101, strictly_alternating)
    assert not subset(divisible_by_3, first_and_last_char_is_x)
    assert not subset(binary_string_all_1, strictly_alternating) 
    assert not subset(at_least_3, is_weekend)
    assert not subset(at_least_3, binary_string_all_1)
    assert not subset(capitalized_first_letter_only, loooong)
    assert not subset(capitalized_first_letter_only, my_name)

def test_more():
    for i in range(2,9,2):
        assert subset(divisible_by_n[i], divisible_by_n[2])
        assert not subset(divisible_by_n[i], divisible_by_n[7])
    for i in range(3,10,3):
        assert subset(divisible_by_n[i], divisible_by_n[3])
        assert not subset(divisible_by_n[i], divisible_by_n[7])
