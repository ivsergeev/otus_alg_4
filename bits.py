# -*- coding: utf-8 -*-

def popcnt1(val: int) -> int:
    cnt = 0
    while val > 0:
        if (val & 1) == 1:
            cnt+=1
        val >> 1
    return cnt


def popcnt2(val: int) -> int:
    cnt = 0
    while val > 0:
        cnt += 1
        val &= val - 1
    return cnt


TAB = []
for i in range(256):
    TAB.append(popcnt2(i))


def popcnt3(val: int) -> int:
    cnt = 0
    while val > 0:
        cnt += TAB[val & 0xff]
        val >>= 8
    return cnt
