import pytest

from consigna6 import solve_lights_out, apply_solution
from utils import random_board, flatten, is_all_zero


def test_all_zero_3x3():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    sol = solve_lights_out(board)
    assert sol == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_center_one_3x3_applies_correctly():
    board = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    sol = solve_lights_out(board)
    x = flatten(sol)
    res = apply_solution(board, x)
    assert is_all_zero(res)


def test_random_4x4():
    board = random_board(4)
    try:
        sol = solve_lights_out(board)
    except ValueError:
        # aceptable: sistema inconsistente
        return
    x = flatten(sol)
    res = apply_solution(board, x)
    assert is_all_zero(res)
