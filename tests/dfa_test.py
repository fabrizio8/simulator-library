import pytest
from simulator import *
from example_dfa import *

def test_even_chars():
    assert even_chars.accepted([1,2,3,4,5,6], trace=True)
    assert even_chars.accepted([], trace=True)
    assert even_chars.accepted([1,2], trace=True)
    assert not even_chars.accepted([1], trace=True)
    assert not even_chars.accepted([1,2,3], trace=True)
    assert not even_chars.accepted([1,2,3,4,5], trace=True)

def test_my_name():
    assert my_name.accepted("FABRIZIO", trace=True)
    assert my_name.accepted("FABRIZIOFABRIZIO", trace=True)
    assert my_name.accepted("FABRIZIOFABRIZIOFABRIZIO", trace=True)
    assert not my_name.accepted("fabrizio", trace=True)
    assert not my_name.accepted("FABRIZIOFABR", trace=True)
    assert not my_name.accepted("not my name", trace=True)

def test_traffic_light():
    assert traffic_light.accepted([0, 0, 0, 0, 1, 1, 1, 2, 1, 0, 0, 0] , trace=True)
    assert traffic_light.accepted([0, 0, 0, 0, 1, 1, 1, 2, 1] , trace=True)
    assert traffic_light.accepted([0, 0, 0, 0, 1, 1, 1, 2, 1, 0, 0, 0,1,2] , trace=True)
    assert not traffic_light.accepted([0, 0, 0, 0, 1, 1, 1, 2] , trace=True)
    assert not traffic_light.accepted([1, 1, 2, 2], trace=True)
    assert not traffic_light.accepted([0]*2000, trace=True)

def test_substring_101():
    assert substring_101.accepted([1, 0, 1], trace=True)
    assert substring_101.accepted([1, 0, 1] + [1, 0]*10, trace=True)
    assert substring_101.accepted([0] * 10 + [1, 0, 1], trace=True)
    assert not substring_101.accepted([], trace=True)
    assert not substring_101.accepted([1, 0], trace=True)
    assert not substring_101.accepted([1, 1, 1, 0, 0, 0, 1], trace=True)

def test_divisble_by_3():
    assert divisible_by_3.accepted('0')
    assert divisible_by_3.accepted('3')
    assert divisible_by_3.accepted('81')
    assert not divisible_by_3.accepted('2')
    assert not divisible_by_3.accepted('500')
    assert not divisible_by_3.accepted('25')


def test_first_and_last_char_is_x():
    assert first_and_last_char_is_x.accepted('x', trace=True)
    assert first_and_last_char_is_x.accepted('xx', trace=True)
    assert first_and_last_char_is_x.accepted('xasdafkshfkajdx', trace=True)
    assert not first_and_last_char_is_x.accepted('xa', trace=True)
    assert not first_and_last_char_is_x.accepted('xxxxxxxxxxa', trace=True)
    assert not first_and_last_char_is_x.accepted([], trace=True)

def test_string_all_1():
    assert binary_string_all_1.accepted([1,1,1,1,1,1,1,1], trace=True)
    assert binary_string_all_1.accepted([1]*25, trace=True)
    assert binary_string_all_1.accepted([1], trace=True)
    assert not binary_string_all_1.accepted([], trace=True)
    assert not binary_string_all_1.accepted([0, 1], trace=True)
    assert not binary_string_all_1.accepted([1]*5 + [0], trace=True)

def test_capitalized_first_letter_only():
    assert capitalized_first_letter_only.accepted("Matthew", trace=True)
    assert capitalized_first_letter_only.accepted("Fabrizio", trace=True)
    assert capitalized_first_letter_only.accepted("A", trace=True)
    assert not capitalized_first_letter_only.accepted("AA", trace=True)
    assert not capitalized_first_letter_only.accepted("aaaaaaT", trace=True)
    assert not capitalized_first_letter_only.accepted("AmericA", trace=True)

def test_strictly_alternating():
    assert strictly_alternating.accepted([1, 0] * 5, trace=True)
    assert strictly_alternating.accepted([1, 0, 1, 0, 1, 0, 1, 0, 1, 0], trace=True)
    assert strictly_alternating.accepted([1, 0], trace=True)
    assert not strictly_alternating.accepted([], trace=True)
    assert not strictly_alternating.accepted([1, 1], trace=True)
    assert not strictly_alternating.accepted([1, 0, 1], trace=True)

def test_at_least_3():
    assert at_least_3.accepted("onetwothree", trace=True)
    assert at_least_3.accepted([1, 2, 3], trace=True)
    assert at_least_3.accepted(["hello", "my", "name", "is", "three"], trace=True)
    assert not at_least_3.accepted([], trace=True)
    assert not at_least_3.accepted([1], trace=True)
    assert not at_least_3.accepted([1, 2], trace=True)

def test_is_weekend():
    assert is_weekend.accepted(["Saturday"], trace=True)
    assert is_weekend.accepted(["Saturday", "Sunday"], trace=True)
    assert is_weekend.accepted(["Sunday"], trace=True)
    assert not is_weekend.accepted([], trace=True)
    assert not is_weekend.accepted(["Monday"], trace=True)
    assert not is_weekend.accepted(["Monday", "Tuesday", "Wednesday"] * 3, trace=True)

def test_loooong():
    assert loooong.accepted("lo0o0o0o0o0ong", trace=True)
    assert loooong.accepted("lOOOOOOOOOO000000000o0o0o0o0o0ng", trace=True)
    assert loooong.accepted("long", trace=True)
    assert not loooong.accepted("short", trace=True)
    assert not loooong.accepted("smol", trace=True)
    assert not loooong.accepted("MINISCULE", trace=True)

def test_dfa_graph_gen():
    for dfa in dfas:
        assert dfa.accepted(find_accepted_string(dfa), trace=True)
