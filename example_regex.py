from simulator import *

one = RE_char('1')
zero = RE_char('0')

all_one = RE_star(one)
# 111111, 1, 1111111111
all_zero = RE_star(zero)
# 00000, 0, 00, 000
zero_followed_by_ones = RE_circ(all_one,all_zero)
#01, 0011, 000001, 011111
zero_or_one = RE_union(one,zero)
#01, 10
any_amount_0_or_1 = RE_star(zero_or_one)
#010101010101, 1011110010100000101, 0, 1, 10, 01
alternating_10 = RE_star(RE_cirq(one,zero))
# 10, 1010, 101010, 10101010
alternating_10_any_amount_of_1 = RE_cirq(alternating_10, RE_star(one))
#101010, 10101011111, 10111111
zero_or_one_followed_by_111 = RE_concat(zero_or_one, RE_concat(RE_concat(one, one), one))

re_list = [
        all_one,
        all_zero,
        zero_followed_by_ones,
        zero_or_one,
        any_amount_0_or_1,
        alternating_10,
        alternating_10_any_amount_of_1,
        zero_or_one_followed_by_111,
        ]
