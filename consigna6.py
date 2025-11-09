"""
Módulo con la implementación de la consigna 6 (Lights Out) - operaciones en GF(2).

Contiene las funciones necesarias para construir y resolver el sistema Ax = b
usando únicamente transformaciones Fi -> Fi + Fj (suma de filas módulo 2).
El solver devuelve una solución particular cuando existe.
"""

from typing import List, Optional, Tuple

def _index(i: int, j: int, n: int) -> int:
    """
    Mapea el índice ij a un único índice.
    """
    return i * n + j

def _build_linear_system(board: List[List[int]]) -> Tuple[List[List[int]], List[int]]:
    """
    Construye el sistema lineal a partir del tablero inicial del juego para después
    aplicarle eliminación Gaussiana en GF(2).
    """
    n = len(board)
    N = n * n
    A = [[0] * N for _ in range(N)]
    b = [0] * N

    # Itera por las luces a(i,j)
    # Forma la matriz A y b, para crear el sistema lineal [A b]
    for i in range(n):
        for j in range(n):
            idx = _index(i, j, n)
            A[idx][idx] = 1                         # incógnita asociada a luz a(i,j)
            if i > 0:
                A[idx][_index(i - 1, j, n)] = 1     # incógnita asociada a luz arriba de a(i,j)
            if i < n - 1:
                A[idx][_index(i + 1, j, n)] = 1     # incógnita asociada a luz abajo de a(i,j)
            if j > 0:
                A[idx][_index(i, j - 1, n)] = 1     # incógnita asociada a luz a la izquierda de a(i,j)
            if j < n - 1:
                A[idx][_index(i, j + 1, n)] = 1     # incógnita asociada a luz a la derecha de a(i,j)
            b[idx] = 1 if board[i][j] else 0        # valor de a(i,j)

    return A, b

def _row_xor(dest: List[int], src: List[int]) -> None:
    """
    Aplica XOR entre filas, se efectúa sobre la fila dest.
    """
    for k in range(len(dest)):
        dest[k] ^= src[k]

def gauss_elimination_gf2(A: List[List[int]], b: List[int]) -> Optional[List[int]]:
    """
    Eliminación Gaussiana en GF(2) usando exclusivamente Fi -> Fi + Fj.
    No se realizan swaps de filas (pivoting). Devuelve una solución particular
    o None si el sistema es inconsistente.
    """
    N = len(A)

    # Crear pivote con Fi = Fi + Fj si es necesario.
    for i in range(N):                  # Fila i
        if A[i][i] == 0:
            for j in range(i + 1, N):   # Fila j
                if A[j][i] == 1:
                    # Fi = Fi + Fj
                    _row_xor(A[i], A[j])
                    b[i] ^= b[j]
                    break

        if A[i][i] == 1:
            for j in range(i + 1, N):   # Fila j
                if A[j][i] == 1:
                    # Fj = Fj + Fi
                    _row_xor(A[j], A[i])
                    b[j] ^= b[i]

    # Detectar inconsistencia.
    for i in range(N):
        if all(v == 0 for v in A[i]) and b[i] == 1:
            return None

    # Variables libres (A[i][i]==0) se fijan a 0.
    x = [0] * N
    for i in range(N - 1, -1, -1):
        if A[i][i] == 0:
            x[i] = 0
            continue
        s = 0
        for j in range(i + 1, N):
            if A[i][j] == 1 and x[j] == 1:
                s ^= 1
        x[i] = (b[i] ^ s) & 1
    return x

def apply_solution(board: List[List[int]], x: List[int]) -> List[List[int]]:
    """
    Aplica la solución sobre el tablero de juego.
    Si el tablero de juego tiene solución, debería dar un tablero de todos 0s.
    """
    n = len(board)
    res = [row.copy() for row in board]
    for i in range(n):
        for j in range(n):
            if x[_index(i, j, n)] == 1:
                res[i][j] ^= 1
                if i > 0:
                    res[i - 1][j] ^= 1
                if i < n - 1:
                    res[i + 1][j] ^= 1
                if j > 0:
                    res[i][j - 1] ^= 1
                if j < n - 1:
                    res[i][j + 1] ^= 1
    return res

def solve_lights_out(board: List[List[int]]) -> List[List[int]]:
    """
    Recibe tablero n x n y devuelve la solución en forma de matriz n x n
    con 0/1. Lanza ValueError si no existe solución.
    """
    if not board:
        raise ValueError("El tablero debe existir")
    n = len(board)
    for row in board:
        if len(row) != n:
            raise ValueError("El tablero debe ser cuadrado n x n")

    A, b = _build_linear_system(board)  # Tablero de juego -> sistema lineal.
    x = gauss_elimination_gf2(A, b)     # Solución del juego
    if x is None:
        raise ValueError("El sistema no tiene solución (inconsistente)")

    final = apply_solution(board, x)
    if any(final[i][j] == 1 for i in range(n) for j in range(n)):
        raise RuntimeError("La solución calculada no apaga todas las luces")

    # Retorna la solución como una matriz de n x n
    sol_mat = [x[i * n:(i + 1) * n] for i in range(n)]
    return sol_mat
