from simulator import *
from example_nfa import *

def test_general():
    a = compile(even_0_or_1)
    b = compile(ends_in_1)
    print(b)
    assert not b.accepted("0010")
    assert not b.accepted("")
    assert not b.accepted("10")
    assert b.accepted("111")
    assert b.accepted("101")
    assert b.accepted("100001")

def test_even_0_or_1():
    strings = [
              ('10001',True),
              ('10101',True),
              ('', True),
              ('1', True),
              ('0', True),
              ('1001', True),
              ('10101',True),
            ]
    for string in strings:
        assert string[1] is compile(even_0_or_1).accepted(string[0])

def test_ends_in_1():
    traces = [
              ('110001',True),
              ('110001',True),
              ('11000',False),
              ('1100',False),
              ('1',True),
              ('0',False),
              ('110',False),
              ('1100',False),
              ('11000',False),
              ('110000',False),
              ('110000',False),
            ]
    for trace in traces:
        assert trace[1] is compile(ends_in_1).accepted(trace[0])


def test_ends_in_0():
    traces = [
              ('1100011',False),
              ('1100011',False),
              ('110001',False),
              ('1100',True),
              ('00',True),
              ('0',True),
              ('1',False),
              ('111',False),
              ('1101',False),
              ('11010',True),
              ('110100',True),
              ('110100',True),
            ]
    for trace in traces:
        assert trace[1] is compile(ends_in_0).accepted(trace[0])

def test_subtring_101():
    traces = [
              ('111111',False),
              ('00000',False),
              ('1110',False),
              ('110',False),
              ('1',False),
              ('0',False),
              ('110',False),
              ('1100',False),
              ('1101',True),
              ('11000',False),
              ('11010',True),
            ]
    for trace in traces:
        assert trace[1] is compile(substring_101).accepted(trace[0])

def test_ends_with_01():
    traces = [
            ('00101',True),
            ('0010',True),
            ('00',True),
            ('001',True),
            ('0',True),
            ('0',True),
            ('0',False),
            ('1',False),
            ('01',False),
            ('011',False),
            ('011',False),
            ('011',False),
            ]
    for trace in traces:
        assert ends_with_01.oracle(*trace)

def test_oneone():
    traces = [
              ('111111',True),
              ('1100',True),
              ('111',True),
              ('110',True),
              ('111',True),
              ('1',True),
              ('0',False),
              ('110',False),
              ('1100',False),
              ('00000',False),
              ('110000',False),
              ('110000',False),
            ]
    for trace in traces:
        assert oneone.oracle(*trace)

def test_double1_0():
    traces = [
                ('011000', True),
                ('011001', True),
                ('01100', True),
                ('1100', True),
                ('110000',True),
                ('110011',True),
                ('001000',False),
                ('010001',False),
                ('01010', False),
                ('1000', False),
                ('010000', False),
                ('100011', False),
            ]
    for trace in traces:
        assert double1_0.oracle(*trace)

# accepts strings that contain at least two 0s or exactly two 1s
def test_zero_or_one():
    traces = [
              ([('1', 5), ('0', 5), ('0', 5), ('0', 5), ('0', 5), ('1', 6)],True),
              ([('1', 5), ('0', 5), ('0', 5), ('0', 5), ('1', 6), ('0', 6)],True),
              ([(None, 2), ('0', 3), ('0', 4)],True),
              ([(None, 2), ('1', 2), ('0', 3)],True),
              ([(None, 2)],True),
              ([('1', 5)],True),
              ([('0', 2)],False),
              ([('1', 2), ('1', 3), ('0', 3)],False),
              ([('1', 2), ('1', 3), ('0', 4), ('0', 4)],False),
              ([(None, 2), ('0', 1), ('0', 1), ('0', 1), ('0', 1)],False),
              ([(None, 2), ('1', 4), ('0', 1), ('0', 1), ('0', 1), ('0', 2)],False),
              ([(None, 2), ('1', 3), ('0', 3), ('0', 3), ('0', 3), ('0', 3)],False),
            ]
    for trace in traces:
        assert zero_or_one.oracle(*trace)

def test_3rd_from_last_is_0():
    traces = [
            ([('0',1),('1',1),('0',1),('0',2),('0',3),('0',4)], True),
            ([('0',1),('1',1),('0',1),('0',2),('0',3),('1',4)], True),
            ([('0',1),('1',1),('0',1),('0',2),('1',3),('1',4)], True),
            ([('0',1),('0',1),('0',1),('0',2),('0',3),('0',4)], True),
            ([('0',1),('0',1),('0',2),('0',3),('0',4)], True),
            ([('0',1),('0',2),('0',3),('0',4)], True),
            ([('0',1),('1',1),('0',1),('0',2),('0',3),('0',1)], False),
            ([('0',3),('1',4),('0',1),('0',2),('0',3),('1',4)], False),
            ([('0',2),('1',1),('0',1),('0',2),('1',5),('1',4)], False),
            ([('0',1),('0',3),('0',1),('0',7),('0',3),('0',4)], False),
            ([('0',1),('0',1),('0',2),('0',2),('0',4)], False),
            ([('0',1),('0',2),('0',2),('0',4)], False),
            ]
    for trace in traces:
        assert third_from_last_is_0.oracle(*trace)

def test_ends_in_a():
    traces = [
            ([('a',1),('a',1),('a',1),('a',1),('a',1),('a',2),], True),
            ([('a',1),('b',1),('c',1),('b',1),('c',1),('a',2),], True),
            ([('b',1),('b',1),('b',1),('b',1),('b',1),('a',2),], True),
            ([('c',1),('b',1),('a',2),], True),
            ([('b',1),('a',2),], True),
            ([('a',2),], True),
            ([('a',1),('a',1),('a',1),('a',1),('a',1),('b',2),], False),
            ([('a',1),('b',1),('c',1),('b',1),('c',1),('c',2),], False),
            ([('b',1),('b',1),('b',1),('b',1),('b',1),('d',2),], False),
            ([('c',2),('b',1),('c',2),], False),
            ([('b',2),('a',2),], False),
            ([('a',2),], False),
            ]
    for trace in traces:
        ends_in_a.oracle(*trace)
