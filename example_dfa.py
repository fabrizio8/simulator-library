#!/usr/bin/env python

from simulator import *
from string import ascii_letters as alphabet, digits

binary = {0,1}
# accepts only even lengthed strings
even_chars = DFA({None, 1, 2},
                lambda s,c: {
                            None: None,
                            1: 2,
                            2: 1}[s],
                1,
                {1},
                set(alphabet))

# accepts strings containing my name one or many times
my_name = DFA({None, 1,2,3,4,5,6,7,8,9,10},
                lambda s, c: {
                            None: None,
                            1: 2 if c=='F' else 10,
                            2: 3 if c=='A' else 10,
                            3: 4 if c=='B' else 10,
                            4: 5 if c=='R' else 10,
                            5: 6 if c=='I' else 10,
                            6: 7 if c=='Z' else 10,
                            7: 8 if c=='I' else 10,
                            8: 9 if c=='O' else 10,
                            9: 2 if c=='F' else 10,
                            10: 10,}[s],
                1,
                {9},
                set(alphabet))

# accepts strings containing traffic light sequences that end in yellow or green
# 0 = hold color, 1 = go forward, 2 = go back
# traffic light follows the cycle R->Y->G->Y->R
traffic_light = DFA({None, 'R','Y','G'},
                    lambda s,c: {
                                None: None,
                                'R': 'R' if c==0 else 'Y',
                                'Y': 'Y' if c==0 else 'G' if c==1 else 'R',
                                'G': 'G' if c==0 else 'Y'}[s],
                    'R',
                    {'Y','G'},
                    {0,1,2})


# accepts binary strings with substrings 101
substring_101 = DFA({None, 1,2,3,4},
                    lambda s, c: {
                                None: None,
                                1: 1 if c == 0 else 2,
                                2: 1 if c == 1 else 3,
                                3: 4 if c == 1 else 1,
                                4: 4}[s],
                    1,
                    {4},
                    binary)

# accepts string of base 10 numbers divisible by 3
divisible_by_3 = gen_DFA_base_b_divisible_by_n(10,3)

divisible_by_n = dict.fromkeys(range(1,10))
for i in range(1,10):
    divisible_by_n[i] = gen_DFA_base_b_divisible_by_n(10,i)
# accepts non-empty string with first same and last char being 'x'
first_and_last_char_is_x = DFA({None, 1,2,3,4},
                            lambda s,c: {
                                        None: None,
                                        1: 2 if c == 'x' else 4,
                                        2: 2 if c == 'x' else 3,
                                        3: 2 if c == 'x' else 3,
                                        4: 4}[s],
                            1,
                            {2},
                            set(alphabet))

# accepts all binary strings containing only 1s
binary_string_all_1 = DFA({None,1,2,3},
                    lambda s,c: {
                                None: None,
                                1: 2 if c == 1 else 3,
                                2: 2 if c == 1 else 3,
                                3: 3}[s],
                    1,
                    {2},
                    binary)

# accepts strings with only the first character capitalized
capitalized_first_letter_only = DFA({None,1,2,3,4},
                        lambda s,c: {
                                    None: None,
                                    1: 2 if c.isupper() else 4,
                                    2: 3 if c.islower() else 4,
                                    3: 3 if c.islower() else 4,
                                    4: 4}[s],
                        1,
                        {2,3},
                        set(alphabet))


# accept only strings that are alternating 10
strictly_alternating = DFA({None, 1,2,3,4},
                            lambda s,c: {
                                        None: None,
                                        1: 2 if c == 1 else 4,
                                        2: 3 if c == 0 else 4,
                                        3: 2 if c == 1 else 4,
                                        4: 4}[s],
                            1,
                            {3},
                            binary)

# accept all strings longer than 3 characters
at_least_3 = DFA({None,1,2,3,4},
            lambda s,c: {
                    None: None,
                    1: 2,
                    2: 3,
                    3: 4,
                    4: 4}[s],
            1,
            {4},
            set(alphabet)|set(digits))

is_weekend = DFA({None,1,'Weekend', 'Weekday'},
                lambda s, c: {
                            None: None,
                            1: 'Weekend' if c in ['Saturday', 'Sunday'] else 'Weekday',
                            'Weekend': 'Weekend' if c in ['Saturday', 'Sunday'] else 'Weekday',
                            'Weekday': 'Weekday'}[s],
                  1,
                {'Weekend'},
                {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"})

# accepts l0o0oO0o0oong strings
loooong = DFA({None,1,2,3,4,5,6},
            lambda s,c: {
                        None: None,
                        1: 2 if c in ['l', 'L'] else 6,
                        2: 3 if c in ['o', 'O', '0'] else 6,
                        3: 3 if c in ['o', 'O', '0'] else 4 if c == 'n' else 6,
                        4: 5 if c == 'g' else 6,
                        5: 6,
                        6: 6}[s],
            1,
            {5},
            set(alphabet)|set(digits))


dfas = [
        even_chars,my_name,traffic_light,substring_101,divisible_by_3,
        first_and_last_char_is_x,binary_string_all_1,capitalized_first_letter_only,
        strictly_alternating,at_least_3,is_weekend,loooong
        ]

