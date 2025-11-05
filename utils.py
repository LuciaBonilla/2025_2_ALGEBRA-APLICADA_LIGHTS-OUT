"""Utilidades para el proyecto Lights Out.

Contiene funciones auxiliares usadas por `main.py` y por tests:
- print_mat(mat): imprime una matriz en filas
- random_board(n): genera una matriz n x n con 0/1 aleatorios 
"""
from typing import List
import random


def print_mat(mat: List[List[int]]) -> None:
    for row in mat:
        print(row)


def random_board(n: int) -> List[List[int]]:
    return [[random.randint(0, 1) for _ in range(n)] for __ in range(n)]


def flatten(mat: List[List[int]]) -> List[int]:
    """Flatten a 2D matrix (row-major) into a 1D list."""
    return [v for row in mat for v in row]


def is_all_zero(mat: List[List[int]]) -> bool:
    """Return True if all entries in the matrix are 0."""
    return all(v == 0 for row in mat for v in row)
