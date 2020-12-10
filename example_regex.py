from simulator import *

one = RE_char('1')
zero = RE_char('0')

all_one = RE_star(one)
# 111111, 1, 1111111111

all_zero = RE_star(zero)
# 00000, 0, 00, 000

zero_followed_by_ones = RE_circ(all_one,all_zero)
#01, 0011, 000001, 011111

zero_or_one = RE_circ(one,zero)
#01, 10

any_amount_0_or_1 = RE_star(zero_or_one)
#010101010101, 1011110010100000101, 0, 1, 10, 01

alternating_10 = RE_star(RE_circ(one,zero))
# 10, 1010, 101010, 10101010

alternating_10_any_amount_of_1 = RE_circ(alternating_10, RE_star(one))
#101010, 10101011111, 10111111

oneoneone = RE_circ(RE_circ(one, one), one)
#111

zero_or_one_followed_by_111 = RE_circ(zero_or_one, oneoneone)
#0111, 1111

any_0_or_1_followed_by_zero_or_one_followed_by_111 = RE_circ(any_amount_0_or_1, zero_or_one_followed_by_111)
#00111, 01111, 111,


re_list = [
        all_one,
        all_zero,
        zero_followed_by_ones,
        zero_or_one,
        any_amount_0_or_1,
        alternating_10,
        alternating_10_any_amount_of_1,
        oneoneone,
        zero_or_one_followed_by_111,
        any_0_or_1_followed_by_zero_or_one_followed_by_111
        ]
