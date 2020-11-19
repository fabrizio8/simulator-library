from simulator import *
from string import ascii_letters as letters
binary = {'0', '1'}

#even number of 0s or 1s
even_0_or_1 = NFA({1,2,3,4,5},
                  {
                    1: {None: {2,4}},
                    2: {'0': {3}, '1': {2}},
                    3: {'0': {2}, '1': {3}},
                    4: {'0': {4}, '1': {5}},
                    5: {'0': {5}, '1': {4}}
                  },
                  1,
                  {2,4},
                  binary)

ends_in_1 = NFA({1,2},
                {
                 1: {'0': {1}, '1': {1,2}},
                 2: {None: {2}},
                },
                1,
                {2},
                binary)

ends_in_0 = NFA({1,2},
                {
                 1: {'1': {1}, '0': {1,2}},
                 2: {None: {2}},
                },
                1,
                {2},
                binary)

substring_101 = NFA({1,2,3,4},
                    {
                     1: {'0': {1}, '1': {1,2}},
                     2: {'0': {3}, '1': {2}},
                     3: {'1': {4}},
                     4: {'1': {4}, '0': {4}},
                    },
                    1,
                    {4},
                    binary)


ends_with_01 = NFA({1,2,3},
                    {
                     1: {'0': {1,2}, '1': {1}},
                     2: {'1': {3}},
                     3: {},
                    },
                    1,
                    {3},
                    binary)

# Strings that begin with 11 and are followed by all 1s, all 0s, or nothing.
oneone = NFA({1,2,3,4,5},
          {
            1: {'1': {2}},
            2: {'1': {3,4}, None: {5}},
            3: {'1': {3}},
            4: {'0': {4}},
            5: {},
          },
          1,
          {3,4,5}
        )

#double 1 is followed by double 0
double1_0 = NFA({1,2,3,4,5},
          {
            1: {'0': {1},'1': {1,2}},
            2: {'1': {3}},
            3: {'0': {4}},
            4: {'0': {5}},
            5: {'0': {5}, '1': {5}},
          },
          1,
          {5}
        )

# I don't know what this is supposed to mean but it gives you strings ending in zero or one
zero_or_one = NFA({1,2,3,4,5,6},
                  {
                    1: {'0': {1}, '1': {5}, None: {2}},
                    2: {'0': {2,3}, '1': {2}},
                    3: {'0': {4}, '1': {3}},
                    4: {'0': {4}, '1': {4}},
                    5: {'0': {5}, '1': {6}},
                    6: {'0': {6}}    
                  },
                  1,
                  {4,6},
                  binary
                )


third_from_last_is_0 = NFA({1,2,3,4},
          {
            1: {'0': {1,2},'1': {1}},
            2: {'0': {3}, '1': {3}},
            3: {'0': {4}, '1': {4}},
            4: {},
          },
          1,
          {4}
        )


ends_in_a = NFA({1,2},
                {
                 1: {'a': {1,2}, 'b': {1}, 'c': {1}},
                 2: {None: {2}},
                },
                1,
                {2},
                )

is_one = NFA({1,2},
                {
                 1: {'1': {2}},
                 2: {None: {2}},
                },
                1,
                {2},
                )

is_zero_or_one = NFA({1,2},
                {
                 1: {'0': {2}, '1': {2}},
                 2: {},
                },
                1,
                {2},
                )

nfa_list  = [
        even_0_or_1,
        ends_in_1,
        ends_in_0, 
        substring_101,
        ends_with_01, 
        oneone, 
        double1_0, 
        zero_or_one, 
        third_from_last_is_0, 
        ends_in_a,
]
