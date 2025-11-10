"""Utilidades para el proyecto Lights Out.

Contiene funciones auxiliares usadas por `main.py` y por tests (helpers)
"""
from typing import Lis

def print_matrix(matrix: List[List[int]]) -> None:
    for row in matrix:
        print(row)

def flatten(matrix: List[List[int]]) -> List[int]:
    """Transforma una matriz en una lista de una dimensión."""
    return [v for row in matrix for v in row]

def is_all_zero(mat: List[List[int]]) -> bool:
    """Retorna True si todas las entradas de la matriz son 0."""
    return all(v == 0 for row in mat for v in row)