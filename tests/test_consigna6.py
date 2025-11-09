import pytest

from consigna6 import solve_lights_out, apply_solution
from utils import flatten, is_all_zero

def test_all_zero_3x3():
    initial_board = [
        [0, 0, 0], 
        [0, 0, 0], 
        [0, 0, 0]
    ]
    solution = solve_lights_out(initial_board)
    assert solution == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

def test_center_one_3x3_applies_correctly():
    initial_board = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    solution = solve_lights_out(initial_board)
    x = flatten(solution)
    resolved_board = apply_solution(initial_board, x)
    assert is_all_zero(resolved_board)
    
def test_know_3x3():
    initial_board = [
        [0, 0, 0],
        [1, 0, 0],
        [0, 0, 1]
    ]
    solution = solve_lights_out(initial_board)
    x = flatten(solution)
    resolved_board = apply_solution(initial_board, x)
    assert is_all_zero(resolved_board)
    assert solution == [
        [0, 1, 0],
        [1, 1, 1],
        [1, 0, 0]
    ] # Solución conocida.

def test_know_5x5():
    initial_board = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1],
        [0, 1, 1, 0, 1]
    ]
    solution = solve_lights_out(initial_board)
    x = flatten(solution)
    resolved_board = apply_solution(initial_board, x)
    assert is_all_zero(resolved_board)
    assert solution == [
        [0, 1, 0, 0, 1],
        [0, 1, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0]
    ] # Solución conocida.
    
def test_know_7x7():
    initial_board = [
        [1, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 0],
        [1, 1, 0, 1, 1, 0, 1],
        [1, 1, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 1, 0],
        [1, 0, 0, 1, 1, 1, 0]
    ]
    solution = solve_lights_out(initial_board)
    x = flatten(solution)
    resolved_board = apply_solution(initial_board, x)
    assert is_all_zero(resolved_board)
    assert solution == [
        [1, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1],
        [1, 1, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 0, 1]
    ] # Solución conocida.