# -*- coding: utf-8 -*-
from chess import king, queen, elephant, rook, horse, pos_to_board, single_rook, single_elephant
from bits import popcnt3


def test_figure(inputs, outputs, alg):
    pos = int(inputs[0])
    count = int(outputs[0])
    mask = int(outputs[1])
    result = alg(pos_to_board(pos))
    assert result == mask
    assert popcnt3(result) == count


def test_king(inputs, outputs):
    test_figure(inputs, outputs, king)


def test_queen(inputs, outputs):
    test_figure(inputs, outputs, queen)


def test_elephant(inputs, outputs):
    test_figure(inputs, outputs, elephant)


def test_rook(inputs, outputs):
    test_figure(inputs, outputs, rook)


def test_horse(inputs, outputs):
    test_figure(inputs, outputs, horse)


def test_single_rook(inputs, outputs):
    pos = int(inputs[0])
    count = int(outputs[0])
    mask = int(outputs[1])
    result = single_rook(pos)
    assert result == mask
    assert popcnt3(result) == count


def test_single_elephant(inputs, outputs):
    pos = int(inputs[0])
    count = int(outputs[0])
    mask = int(outputs[1])
    result = single_elephant(pos)
    assert result == mask
    assert popcnt3(result) == count
