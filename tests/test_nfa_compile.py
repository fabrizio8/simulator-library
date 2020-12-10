from simulator import *
from example_nfa import *

def test_general():
    a = compile(even_0_or_1)
    b = compile(ends_in_1)
    ends_in_1_DFA = DFA({(1,),(1,2)},
            lambda s,c: {(1): (1) if c == '0' else (1,2),
                        (1,2): (1) if c == '1' else (1,2)}[s],
                        (1,),
                        {(1,2)},
                        {'0','1'})

    even_0_or_1_DFA = DFA({(2, 4), (3, 4), (2, 5), (1, 2, 4), (3, 5)},
                    lambda s,c: {
                        (2, 4): (2, 5) if c == '1' else (3, 4),
                        (3, 4): (2, 4) if c == '0' else(3, 5),
                        (2, 5): (2, 4) if c == '1' else(3, 5),
                        (3, 5): (2, 5) if c == '0' else(3, 4),
                        (1, 2, 4): (2, 5) if c == '1' else (3, 4),
                        }[s],
                    (1, 2, 4),
                    {(2, 4), (2, 5), (1, 2, 4), (3, 4)},
                    {'1', '0'})


    assert equal(b, ends_in_1_DFA)
    assert equal(a, even_0_or_1_DFA)


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
            ('0010',False),
            ('00',False),
            ('001',True),
            ('0',False),
            ('1',False),
            ('01',True),
            ('011',False),
            ]
    for trace in traces:
        assert trace[1] is compile(ends_with_01).accepted(trace[0])

def test_oneone():
    traces = [
              ('111111',True),
              ('1100',True),
              ('111',True),
              ('110',True),
              ('111',True),
              ('1',True),
              ('0',False),
              ('00000',False),
              ('110000',True),
              ('110000',True),
            ]
    for trace in traces:
        assert trace[1] is compile(oneone).accepted(trace[0])

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
        assert trace[1] is compile(double1_0).accepted(trace[0])

# accepts strings that contain at least two 0s or exactly two 1s
def test_zero_or_one():
    traces = [
              ('100001',True),
              ('100010',True),
              ('00',True),
              ('10', False),
              ('',False),
              ('1',False),
              ('0',False),
              ('110',True),
              ('1100',True),
              ('0000',True),
              ('10000',True),
              ('10000',True),
            ]
    for trace in traces:
        assert trace[1] is compile(zero_or_one).accepted(trace[0])

def test_3rd_from_last_is_0():
    traces = [
            ('010000', True),
            ('010001', True),
            ('010011', True),
            ('000000', True),
            ('00000', True),
            ('0000', True),
            ('010000', True),
            ('010001', True),
            ('010011', True),
            ('000000', True),
            ('00000', True),
            ('0000',True),
            ]
    for trace in traces:
        assert trace[1] is compile(third_from_last_is_0).accepted(trace[0])

def test_ends_in_a():
    traces = [
            ('aaaaaa', True),
            ('abcbca', True),
            ('bbbbba', True),
            ('cba', True),
            ('ba', True),
            ('a', True),
            ('aaaaab', False),
            ('abcbcc', False),
            ('bbbbbd', False),
            ('cbc', False),
            ('ba', True),
            ]
    for trace in traces:
        assert trace[1] is compile(ends_in_a).accepted(trace[0])
