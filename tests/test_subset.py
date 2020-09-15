from simulator import *
from example_dfa import *

# def test_even_and_my_name():
#     assert not subset(even_chars, my_name)

# def test_even_chars_and_divisible_by_3():
#     assert not subset(even_chars, divisible_by_3)

# def test_traffic_light_and_substring101():
#     assert not subset(traffic_light, substring_101)

def test_traffic_light_and_all_1s():
    assert subset(binary_string_all_1, traffic_light)

# def test_substring_101_and_strictly_alternating():
#     assert not subset(substring_101, strictly_alternating)

# def test_divisible_by_3_and_first_last_x():
#     assert not subset(divisible_by_3, first_and_last_char_is_x)

# def test_string_all_1_and_strictly_alternating():
#     assert not subset(binary_string_all_1, strictly_alternating) 

# def test_at_least_3_and_is_weekend():
#     assert not subset(at_least_3, is_weekend)

def test_at_least_3_and_loooong():
    assert subset(loooong, at_least_3)

# def test_at_least_3_and_all_1():
#     assert not subset(at_least_3, binary_string_all_1)

# def test_capitalized_and_loooong():
#     assert not subset(capitalized_first_letter_only, loooong)

# def test_capitalized_and_my_name():
#     assert not subset(capitalized_first_letter_only, my_name)
