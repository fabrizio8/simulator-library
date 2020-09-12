#!/usr/bin/env python

from simulator import *

# accepts only even lengthed strings
even_chars = DFA([1, 2],
                lambda s: {1: 2,
                           2: 1}[s],
                1,
                [1])

# accepts strings containing my name in uppercase letters
my_name = DFA([1,2,3,4,5,6,7,8,9,10],
              lambda s, c: {1: 2 if c=='F' else 10,
                            2: 3 if c=='A' else 10,
                            3: 4 if c=='B' else 10,
                            4: 5 if c=='R' else 10,
                            5: 6 if c=='I' else 10,
                            6: 7 if c=='Z' else 10,
                            7: 8 if c=='I' else 10,
                            8: 9 if c=='O' else 10,
                            9: 10,}[s],
              1,
              [9])

# accepts strings containing traffic light sequences that end in yellow or green
# 0 = hold color, 1 = go forward, 2 = go back
# traffic light follows the cycle R->Y->G->Y->R
traffic_light = DFA(['R','Y','G'],
                    lambda s,x: {1: 1 if x==0 else 2,
                                 2: 2 if x==0 else 3 if x==1 else 1,
                                 3: 3 if x==0 else 2}[s],
                    1,
                    [2,3])


# accepts binary strings with substrings 101
substring_101 = DFA([1,2,3,4],
                    lambda s, x: {1: 1 if x == 0 else 2,
                                  2: 1 if x == 1 else 3,
                                  3: 4 if x == 1 else 1,
                                  4: 4}[s].
                    1,
                    [4])

# accepts string of hours if the last hour was in the morning.
is_it_morning = DFA(['Morning', 'Not Morning'],
        lambda x: 'Not Morning' if x  >= 12  else 'Morning',
        'Not Morning',
        ['Morning'])

# accepts non-empty string with first same and last char being 'x'
first_and_last_char_is_x = DFA([1,2,3],
        lambda c: 2 if c == 'x' else 3,
        1,
        [2])

# accepts all binary strings containing only 1s
binary_string_all_1 = DFA([1,2,3],
        lambda s,c: {1: 2 if c == 1 else 3,
                    {2: 2 if c == 1 else 3,
                     3: 3}[s],
        1,
        [2])

# accepts all strings with only the first character capitalized
capitalized_first_letter_only = DFA([1,2,3,4],
        lambda s,c: {1: 2 if isupper(c) else 4,
                    {2: 3 if islower(c) else 4,
                     3: 3 if islower(c) else 4,
                     4: 4}[s],
        1,
        [2,3])


# accept only strings that are alternating 10
strictly_alternating = DFA([1,2,3,4],
                           lambda s,c: {1: 2 if c == 1 else 4,
                                        2: 3 if c == 0 else 4,
                                        3: 2 if c == 1 else 4,
                                        4: 4}[s],
                           1,
                           [3])

# accept all strings longer than 3 characters
at_least_3 = DFA([1,2,3,4],
    lambda s: {1: 2,
              2: 3,
              3: 4
              4: 4}[s],
    1,
    [4])

is_weekend() = DFA([1,'Weekend', 'Weekday']
                  lambda s, c: {1: 'Weekend' if c in ['Saturday', 'Sunday'] else 'Weekday',
                                2: 'Weekend' if c in ['Saturday', 'Sunday'] else 'Weekday',
                                3: 'Weekday'}[s],
                  1,
                  ['Weekend'])

# accepts l0o0oO0o0oong strings
loooong = DFA([1,2,3,4,5],
        lambda s,c: {1: 2 if c in ['l', 'L'] else 5,
                     2: 2 if c in ['o', 'O', '0'] else 3 if c == 'n' else 5,
                     3: 4 if c == 'g',
                     4: 5}[s]
        1,
        [4])
