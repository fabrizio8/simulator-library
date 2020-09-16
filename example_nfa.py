from simulator import *
from string import ascii_letters as letters

even_chars = DFA({None, 1, 2},
                lambda s,c: {
                            None: None,
                            1: 2,
                            2: 1}[s],
                1,
                {1},
                set(alphabet))

my_name_substr = NFA(
                     {list(range(1,11))},
                    {
                        1: {lambda c: 1 if c in letters else 11}
                    }