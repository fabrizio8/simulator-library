import pytest
from simulator import *
from example_dfa import *

def test_even_chars():
    assert trace(even_chars, [1,2,3,4,5,6])
    assert trace(even_chars, [])
    assert trace(even_chars, [1,2])
    assert not trace(even_chars, [1])
    assert not trace(even_chars, [1,2,3])
    assert not trace(even_chars, [1,2,3,4,5])

def test_my_name():
    assert trace(my_name, "FABRIZIO")
    assert trace(my_name, "FABRIZIOFABRIZIO")
    assert trace(my_name, "FABRIZIOFABRIZIOFABRIZIO")
    assert not trace(my_name, "fabrizio")
    assert not trace(my_name, "FABRIZIOFABR")
    assert not trace(my_name, "not my name")

def test_traffic_light():
    assert trace(traffic_light, [0, 0, 0, 0, 1, 1, 1, 2, 1, 0, 0, 0] )
    assert trace(traffic_light, [0, 0, 0, 0, 1, 1, 1, 2, 1] )
    assert trace(traffic_light, [0, 0, 0, 0, 1, 1, 1, 2, 1, 0, 0, 0,1,2] )
    assert not trace(traffic_light, [0, 0, 0, 0, 1, 1, 1, 2] )
    assert not trace(traffic_light, [1, 1, 2, 2])
    assert not trace(traffic_light, [0]*2000)

def test_substring_101():
    assert trace(substring_101, [1, 0, 1])
    assert trace(substring_101, [1, 0, 1] + [1, 0]*10)
    assert trace(substring_101, [0] * 10 + [1, 0, 1])
    assert not trace(substring_101, [])
    assert not trace(substring_101, [1, 0])
    assert not trace(substring_101, [1, 1, 1, 0, 0, 0, 1])

def test_is_it_morning():
    assert trace(is_it_morning, list(range(23,0,-1)))
    assert trace(is_it_morning, [5])
    assert trace(is_it_morning, list(range(10,0,-1)))
    assert not trace(is_it_morning, list(range(23)))
    assert not trace(is_it_morning, [12])
    assert not trace(is_it_morning, [0, 5, 10, 15])

def test_first_and_last_char_is_x():
    assert trace(first_and_last_char_is_x, 'x')
    assert trace(first_and_last_char_is_x, 'xx')
    assert trace(first_and_last_char_is_x, 'xasdafkshfkajdx')
    assert not trace(first_and_last_char_is_x, 'xa')
    assert not trace(first_and_last_char_is_x, 'xxxxxxxxxxa')
    assert not trace(first_and_last_char_is_x, '')

def test_string_all_1():
    assert trace(binary_string_all_1, [1,1,1,1,1,1,1,1])
    assert trace(binary_string_all_1, [1]*25)
    assert trace(binary_string_all_1, [1])
    assert not trace(binary_string_all_1, [])
    assert not trace(binary_string_all_1, [0, 1])
    assert not trace(binary_string_all_1, [1]*5 + [0])

def test_capitalized_first_letter_only():
    assert trace(capitalized_first_letter_only, "Matthew")
    assert trace(capitalized_first_letter_only, "Fabrizio")
    assert trace(capitalized_first_letter_only, "A")
    assert not trace(capitalized_first_letter_only, "AA")
    assert not trace(capitalized_first_letter_only, "aaaaaaT")
    assert not trace(capitalized_first_letter_only, "AmericA")

def test_strictly_alternating():
    assert trace(strictly_alternating, [1, 0] * 5)
    assert trace(strictly_alternating, [1, 0, 1, 0, 1, 0, 1, 0, 1, 0])
    assert trace(strictly_alternating, [1, 0])
    assert not trace(strictly_alternating, [])
    assert not trace(strictly_alternating, [1, 1])
    assert not trace(strictly_alternating, [1, 0, 1])

def test_at_least_3():
    assert trace(at_least_3, "onetwothree")
    assert trace(at_least_3, [1, 2, 3])
    assert trace(at_least_3, ["hello", "my", "name", "is", "three"])
    assert not trace(at_least_3, [])
    assert not trace(at_least_3, [1])
    assert not trace(at_least_3, [1, 2])

def test_is_weekend():
    assert trace(is_weekend, ["Saturday"])
    assert trace(is_weekend, ["Saturday", "Sunday"])
    assert trace(is_weekend, ["Sunday"])
    assert not trace(is_weekend, [])
    assert not trace(is_weekend, ["Monday"])
    assert not trace(is_weekend, ["Monday", "Tuesday", "Wednesday"] * 3)

def test_loooong():
    assert trace(loooong, "lo0o0o0o0o0ong")
    assert trace(loooong, "lOOOOOOOOOO000000000o0o0o0o0o0ng")
    assert trace(loooong, "long")
    assert not trace(loooong, "short")
    assert not trace(loooong, "smol")
    assert not trace(loooong, "MINISCULE")
