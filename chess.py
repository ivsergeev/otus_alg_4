# -*- coding: utf-8 -*-

MAX = 0xffffffffffffffff


def pos_to_board(pos: int) -> int:
    '''Преобразование позиции в маску положения на доске'''
    if pos < 0 or pos > 63:
        raise ValueError
    return 1 << pos


def king(board: int) -> int:
    '''Король'''
    k = board
    noA = 0xfefefefefefefefe
    noH = 0x7f7f7f7f7f7f7f7f
    kA = k & noA
    kH = k & noH
    mask = kA << 7 | k << 8 | kH << 9 |\
           kA >> 1 |          kH << 1 |\
           kA >> 9 | k >> 8 | kH >> 7
    return mask & MAX


def horse(board: int) -> int:
    '''Конь'''
    k = board
    noA = 0xfefefefefefefefe
    noAB = 0xfcfcfcfcfcfcfcfc
    noH = 0x7f7f7f7f7f7f7f7f
    noGH = 0x3f3f3f3f3f3f3f3f
    kA = k & noA
    kAB = k & noAB
    kH = k & noH
    kGH = k & noGH
    mask = kAB << 6 | kA << 15 | kH << 17 | kGH << 10 |\
           kAB >> 10 | kA >> 17 | kH >> 15 | kGH >> 6
    return mask & MAX


def rook(board: int) -> int:
    '''Ладья'''
    mask = 0
    v = 0x0101010101010101
    h = 0xff
    while h < MAX:
        if h & board != 0:
            mask = mask | h
        h <<= 8
    while v < MAX:
        if v & board != 0:
            mask = mask | v
        v <<= 1
    return (mask ^ board) & MAX


def elephant(board: int) -> int:
    '''Слон'''
    lD = 0x102040810204080
    rD = 0x8040201008040201
    noA = 0xfefefefefefefefe
    noH = 0x7f7f7f7f7f7f7f7f

    mask = 0
    lK = lD
    rK = rD
    for i in range(-7, 8):
        lK = lD if i == 0\
                else (lK & noA) >> 1 if i < 0\
                else (lK & noH) << 1
        rK = rD if i == 0\
                else (rK & noA) >> 1 if i < 0\
                else (rK & noH) << 1
        if lK & board != 0:            
            mask |= lK
        if rK & board != 0:
            mask |= rK

    return (mask ^ board) & MAX


def queen(pos: int):
    '''Ферзь'''
    return rook(pos) | elephant(pos)
