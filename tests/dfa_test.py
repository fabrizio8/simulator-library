import pytest
from simulator import *
from example_dfa import *

def test_even_chars():
    assert accepted(even_chars, [1,2,3,4,5,6], trace=True)
    assert accepted(even_chars, [], trace=True)
    assert accepted(even_chars, [1,2], trace=True)
    assert not accepted(even_chars, [1], trace=True)
    assert not accepted(even_chars, [1,2,3], trace=True)
    assert not accepted(even_chars, [1,2,3,4,5], trace=True)

def test_my_name():
    assert accepted(my_name, "FABRIZIO", trace=True)
    assert accepted(my_name, "FABRIZIOFABRIZIO", trace=True)
    assert accepted(my_name, "FABRIZIOFABRIZIOFABRIZIO", trace=True)
    assert not accepted(my_name, "fabrizio", trace=True)
    assert not accepted(my_name, "FABRIZIOFABR", trace=True)
    assert not accepted(my_name, "not my name", trace=True)

def test_traffic_light():
    assert accepted(traffic_light, [0, 0, 0, 0, 1, 1, 1, 2, 1, 0, 0, 0] , trace=True)
    assert accepted(traffic_light, [0, 0, 0, 0, 1, 1, 1, 2, 1] , trace=True)
    assert accepted(traffic_light, [0, 0, 0, 0, 1, 1, 1, 2, 1, 0, 0, 0,1,2] , trace=True)
    assert not accepted(traffic_light, [0, 0, 0, 0, 1, 1, 1, 2] , trace=True)
    assert not accepted(traffic_light, [1, 1, 2, 2], trace=True)
    assert not accepted(traffic_light, [0]*2000, trace=True)

def test_substring_101():
    assert accepted(substring_101, [1, 0, 1], trace=True)
    assert accepted(substring_101, [1, 0, 1] + [1, 0]*10, trace=True)
    assert accepted(substring_101, [0] * 10 + [1, 0, 1], trace=True)
    assert not accepted(substring_101, [], trace=True)
    assert not accepted(substring_101, [1, 0], trace=True)
    assert not accepted(substring_101, [1, 1, 1, 0, 0, 0, 1], trace=True)

def test_is_it_morning():
    assert accepted(is_it_morning, list(range(23,0,-1)), trace=True)
    assert accepted(is_it_morning, [5], trace=True)
    assert accepted(is_it_morning, list(range(10,0,-1)), trace=True)
    assert not accepted(is_it_morning, list(range(23)), trace=True)
    assert not accepted(is_it_morning, [12], trace=True)
    assert not accepted(is_it_morning, [0, 5, 10, 15], trace=True)

def test_first_and_last_char_is_x():
    assert accepted(first_and_last_char_is_x, 'x', trace=True)
    assert accepted(first_and_last_char_is_x, 'xx', trace=True)
    assert accepted(first_and_last_char_is_x, 'xasdafkshfkajdx', trace=True)
    assert not accepted(first_and_last_char_is_x, 'xa', trace=True)
    assert not accepted(first_and_last_char_is_x, 'xxxxxxxxxxa', trace=True)
    assert not accepted(first_and_last_char_is_x, '', trace=True)

def test_string_all_1():
    assert accepted(binary_string_all_1, [1,1,1,1,1,1,1,1], trace=True)
    assert accepted(binary_string_all_1, [1]*25, trace=True)
    assert accepted(binary_string_all_1, [1], trace=True)
    assert not accepted(binary_string_all_1, [], trace=True)
    assert not accepted(binary_string_all_1, [0, 1], trace=True)
    assert not accepted(binary_string_all_1, [1]*5 + [0], trace=True)

def test_capitalized_first_letter_only():
    assert accepted(capitalized_first_letter_only, "Matthew", trace=True)
    assert accepted(capitalized_first_letter_only, "Fabrizio", trace=True)
    assert accepted(capitalized_first_letter_only, "A", trace=True)
    assert not accepted(capitalized_first_letter_only, "AA", trace=True)
    assert not accepted(capitalized_first_letter_only, "aaaaaaT", trace=True)
    assert not accepted(capitalized_first_letter_only, "AmericA", trace=True)

def test_strictly_alternating():
    assert accepted(strictly_alternating, [1, 0] * 5, trace=True)
    assert accepted(strictly_alternating, [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], trace=True)
    assert accepted(strictly_alternating, [1, 0], trace=True)
    assert not accepted(strictly_alternating, [], trace=True)
    assert not accepted(strictly_alternating, [1, 1], trace=True)
    assert not accepted(strictly_alternating, [1, 0, 1], trace=True)

def test_at_least_3():
    assert accepted(at_least_3, "onetwothree", trace=True)
    assert accepted(at_least_3, [1, 2, 3], trace=True)
    assert accepted(at_least_3, ["hello", "my", "name", "is", "three"], trace=True)
    assert not accepted(at_least_3, [], trace=True)
    assert not accepted(at_least_3, [1], trace=True)
    assert not accepted(at_least_3, [1, 2], trace=True)

def test_is_weekend():
    assert accepted(is_weekend, ["Saturday"], trace=True)
    assert accepted(is_weekend, ["Saturday", "Sunday"], trace=True)
    assert accepted(is_weekend, ["Sunday"], trace=True)
    assert not accepted(is_weekend, [], trace=True)
    assert not accepted(is_weekend, ["Monday"], trace=True)
    assert not accepted(is_weekend, ["Monday", "Tuesday", "Wednesday"] * 3, trace=True)

def test_loooong():
    assert accepted(loooong, "lo0o0o0o0o0ong", trace=True)
    assert accepted(loooong, "lOOOOOOOOOO000000000o0o0o0o0o0ng", trace=True)
    assert accepted(loooong, "long", trace=True)
    assert not accepted(loooong, "short", trace=True)
    assert not accepted(loooong, "smol", trace=True)
    assert not accepted(loooong, "MINISCULE", trace=True)
