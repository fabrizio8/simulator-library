from simulator import *
from example_dfa import *

def test_union_even_and_my_name():
    dfa_u = union(even_chars, my_name)
    assert dfa_u.accepted([1,2,3,4,5,6], trace=True)
    assert dfa_u.accepted([], trace=True)
    assert dfa_u.accepted([1,2], trace=True)
    assert dfa_u.accepted("FABRIZIO", trace=True)
    assert dfa_u.accepted("FABRIZIOFABRIZIO", trace=True)
    assert dfa_u.accepted("FABRIZIOFABRIZIOFABRIZIO", trace=True)
    assert dfa_u.accepted("fabrizio", trace=True)
    assert dfa_u.accepted("FABRIZIOFABR", trace=True)
    assert not dfa_u.accepted([1], trace=True)
    assert not dfa_u.accepted("not my name", trace=True)
    assert not dfa_u.accepted("Fab", trace=True)
    assert not dfa_u.accepted("0", trace=True)
    assert not dfa_u.accepted("Dj Hi-Tek", trace=True)
    assert not dfa_u.accepted("Fabri", trace=True)

def test_even_chars_and_divisible_by_3():
    dfa_u = union(even_chars, divisible_by_3)
    assert dfa_u.accepted(['1','2','3','4','5','6'], trace=True)
    assert dfa_u.accepted([], trace=True)
    assert dfa_u.accepted(['1','2'], trace=True)
    assert dfa_u.accepted(str(654321), trace=True)
    assert dfa_u.accepted([], trace=True)
    assert dfa_u.accepted(str(543210), trace=True)
    assert not dfa_u.accepted('2', trace=True)
    assert not dfa_u.accepted('7', trace=True)
    assert not dfa_u.accepted(['1','2','3','4','7'], trace=True)
    assert not dfa_u.accepted('5', trace=True)
    assert not dfa_u.accepted(list(range(7)), trace=True)
    assert not dfa_u.accepted('1', trace=True)

def test_traffic_light_and_substring101():
    dfa_u = union(traffic_light, substring_101)
    assert dfa_u.accepted([0, 0, 0, 0, 1, 1, 1, 2, 1, 0, 0, 0] , trace=True)
    assert dfa_u.accepted([0, 0, 0, 0, 1, 1, 1, 2, 1] , trace=True)
    assert dfa_u.accepted([0, 0, 0, 0, 1, 1, 1, 2, 1, 0, 0, 0,1,2] , trace=True)
    assert not dfa_u.accepted([0, 0, 0, 0, 1, 1, 1, 2] , trace=True)
    assert not dfa_u.accepted([1, 1, 2, 2], trace=True)
    assert not dfa_u.accepted([0]*2000, trace=True)
    assert dfa_u.accepted([1, 0, 1], trace=True)
    assert dfa_u.accepted([1, 0, 1] + [1, 0]*10, trace=True)
    assert dfa_u.accepted([0] * 10 + [1, 0, 1], trace=True)
    assert not dfa_u.accepted([], trace=True)
    assert dfa_u.accepted([1, 0], trace=True)
    assert dfa_u.accepted([1, 1, 1, 0, 1], trace=True)

def test_traffic_light_and_all_1s():
    dfa_u = union(traffic_light, binary_string_all_1)
    assert dfa_u.accepted([0, 0, 0, 0, 1, 1, 1, 2, 1, 0, 0, 0] , trace=True)
    assert dfa_u.accepted([0, 0, 0, 0, 1, 1, 1, 2, 1] , trace=True)
    assert dfa_u.accepted([0, 0, 0, 0, 1, 1, 1, 2, 1, 0, 0, 0,1,2] , trace=True)
    assert dfa_u.accepted([0, 1], trace=True)
    assert not dfa_u.accepted([0, 0, 0, 0, 1, 1, 1, 2] , trace=True)
    assert not dfa_u.accepted([1, 1, 2, 2], trace=True)
    assert not dfa_u.accepted([0]*2000, trace=True)
    assert dfa_u.accepted([1,1,1,1,1,1,1,1], trace=True)
    assert dfa_u.accepted([1]*25, trace=True)
    assert dfa_u.accepted([1], trace=True)
    assert not dfa_u.accepted([], trace=True)
    assert not dfa_u.accepted([1]*5 + [0,2], trace=True)


def test_substring_101_and_strictly_alternating():
    dfa_u = union(substring_101, strictly_alternating)
    assert dfa_u.accepted([1, 0, 1], trace=True)
    assert dfa_u.accepted([1, 0, 1] + [1, 0]*10, trace=True)
    assert dfa_u.accepted([0] * 10 + [1, 0, 1], trace=True)
    assert not dfa_u.accepted([], trace=True)
    assert dfa_u.accepted([1, 0], trace=True)
    assert not dfa_u.accepted([1, 1, 1, 0, 0, 0, 1], trace=True)
    assert dfa_u.accepted([1, 0] * 5, trace=True)
    assert dfa_u.accepted([1, 0, 1, 0, 1, 0, 1, 0, 1, 0], trace=True)
    assert dfa_u.accepted([1, 0], trace=True)
    assert not dfa_u.accepted([], trace=True)
    assert not dfa_u.accepted([1, 1], trace=True)
    assert dfa_u.accepted([1, 0, 1], trace=True)


def test_divisible_by_3_and_first_last_x():
    dfa_u = union(divisible_by_3, first_and_last_char_is_x)
    assert dfa_u.accepted('33', trace=True)
    assert dfa_u.accepted(['1','5'], trace=True)
    assert dfa_u.accepted(['1','2'], trace=True)
    assert dfa_u.accepted('x', trace=True)
    assert dfa_u.accepted('xx', trace=True)
    assert dfa_u.accepted([], trace=True)
    assert not dfa_u.accepted(['5', '1', '0', '1'], trace=True)
    assert not dfa_u.accepted(str(23), trace=True)
    assert not dfa_u.accepted(str(10), trace=True)
    assert not dfa_u.accepted(str(14), trace=True)
    assert not dfa_u.accepted(str(26), trace=True)
    assert not dfa_u.accepted(str(103), trace=True)

def test_string_all_1_and_strictly_alternating():
    dfa_u = union(binary_string_all_1, strictly_alternating) 
    assert dfa_u.accepted([1,1,1,1,1,1,1,1], trace=True)
    assert dfa_u.accepted([1]*25, trace=True)
    assert dfa_u.accepted([1], trace=True)
    assert not dfa_u.accepted([], trace=True)
    assert not dfa_u.accepted([0, 1], trace=True)
    assert not dfa_u.accepted([1]*5 + [0], trace=True)
    assert dfa_u.accepted([1, 0] * 5, trace=True)
    assert dfa_u.accepted([1, 0, 1, 0, 1, 0, 1, 0, 1, 0], trace=True)
    assert dfa_u.accepted([1, 0], trace=True)
    assert not dfa_u.accepted([], trace=True)
    assert not dfa_u.accepted([1, 2], trace=True)
    assert not dfa_u.accepted([1, 0, 1], trace=True)

def test_at_least_3_and_is_weekend():
    dfa_u = union(at_least_3, is_weekend)
    assert dfa_u.accepted("onetwothree", trace=True)
    assert dfa_u.accepted([1, 2, 3], trace=True)
    assert dfa_u.accepted(["hello", "my", "name", "is", "three"], trace=True)
    assert not dfa_u.accepted([], trace=True)
    assert not dfa_u.accepted([1], trace=True)
    assert not dfa_u.accepted([1, 2], trace=True)
    assert dfa_u.accepted(["Saturday"], trace=True)
    assert dfa_u.accepted(["Saturday", "Sunday"], trace=True)
    assert dfa_u.accepted(["Sunday"], trace=True)
    assert not dfa_u.accepted([], trace=True)
    assert not dfa_u.accepted(["Monday"], trace=True)
    assert dfa_u.accepted(["Monday", "Tuesday", "Wednesday"] * 3, trace=True)

def test_at_least_3_and_loooong():
    dfa_u = union(at_least_3, loooong)
    assert dfa_u.accepted("onetwothree", trace=True)
    assert dfa_u.accepted([1, 2, 3], trace=True)
    assert not dfa_u.accepted("sm", trace=True)
    assert not dfa_u.accepted([], trace=True)
    assert not dfa_u.accepted([1], trace=True)
    assert not dfa_u.accepted([1, 2], trace=True)
    assert dfa_u.accepted("lo0o0o0o0o0ong", trace=True)
    assert dfa_u.accepted("lOOOOOOOOOO000000000o0o0o0o0o0ng", trace=True)
    assert dfa_u.accepted("long", trace=True)
    assert dfa_u.accepted("short", trace=True)
    assert dfa_u.accepted("smol", trace=True)
    assert dfa_u.accepted("MINISCULE", trace=True)

def test_at_least_3_and_all_1():
    dfa_u = union(at_least_3, binary_string_all_1)
    assert dfa_u.accepted([1,1,1,1,1,1,1,1], trace=True)
    assert dfa_u.accepted([1]*25, trace=True)
    assert dfa_u.accepted([1], trace=True)
    assert not dfa_u.accepted([], trace=True)
    assert not dfa_u.accepted([0, 1], trace=True)
    assert not dfa_u.accepted([2]*2, trace=True)
    assert dfa_u.accepted("onetwothree", trace=True)
    assert dfa_u.accepted([1, 2, 3], trace=True)
    assert dfa_u.accepted(["hello", "my", "name", "is", "three"], trace=True)
    assert not dfa_u.accepted([], trace=True)
    assert not dfa_u.accepted([3], trace=True)
    assert not dfa_u.accepted([1, 2], trace=True)


def test_capitalized_and_loooong():
    dfa_u = union(capitalized_first_letter_only, loooong)
    assert dfa_u.accepted("Long", trace=True)
    assert dfa_u.accepted("Lamb", trace=True)
    assert dfa_u.accepted("Looooongg", trace=True)
    assert not dfa_u.accepted("AA", trace=True)
    assert not dfa_u.accepted("aaaaaaT", trace=True)
    assert not dfa_u.accepted("AmericA", trace=True)
    assert dfa_u.accepted("lo0o0o0o0o0ong", trace=True)
    assert dfa_u.accepted("lOOOOOOOOOO000000000o0o0o0o0o0ng", trace=True)
    assert dfa_u.accepted("long", trace=True)
    assert not dfa_u.accepted("ShorT", trace=True)
    assert not dfa_u.accepted("smol", trace=True)
    assert not dfa_u.accepted("MINISCULE", trace=True)

def test_capitalized_and_my_name():
    dfa_u = union(capitalized_first_letter_only, my_name)
    assert dfa_u.accepted("Matthew", trace=True)
    assert dfa_u.accepted("Fabrizio", trace=True)
    assert dfa_u.accepted("A", trace=True)
    assert not dfa_u.accepted("AA", trace=True)
    assert not dfa_u.accepted("aaaaaaT", trace=True)
    assert not dfa_u.accepted("AmericA", trace=True)
    assert dfa_u.accepted("FABRIZIO", trace=True)
    assert dfa_u.accepted("FABRIZIOFABRIZIO", trace=True)
    assert dfa_u.accepted("FABRIZIOFABRIZIOFABRIZIO", trace=True)
    assert not dfa_u.accepted("fabrizio", trace=True)
    assert not dfa_u.accepted("FABRIZIOFABR", trace=True)
    assert not dfa_u.accepted("not my name", trace=True)


def test_math():
    dfa_u = divisible_by_n[1]
    for i in range(2,5):
        dfa_u = union(divisible_by_n[i], dfa_u)
    for i in range(1,500,3):
        assert dfa_u.accepted(str(i))
    dfa_u = divisible_by_n[2]
    dfa_u = union(divisible_by_n[3], dfa_u)
    should_fail = ['1', '7', '11']
    should_pass = ['8', '9', '666']
    for i in should_fail:
        assert not dfa_u.accepted(i)
    for i in should_pass:
        assert dfa_u.accepted(i)
