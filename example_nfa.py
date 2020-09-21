from simulator import *
from string import ascii_letters as letters
binary = {'0', '1'}

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
                 2: {None},
                },
                1,
                {2},
                binary)