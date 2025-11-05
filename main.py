"""
Script de ejecución separado para `consigna6`.
"""
from consigna6 import solve_lights_out
from utils import print_mat, random_board


def main():
    examples = {
        "todo_cero_3x3": [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        "una_luz_3x3": [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        "random_4x4": None,
    }

    # generar tablero aleatorio 
    examples["random_4x4"] = random_board(4)

    for name, board in examples.items():
        print(f"-- Ejemplo: {name}")
        print_mat(board)
        try:
            sol = solve_lights_out(board)
            print("Solución (matriz):")
            print_mat(sol)
        except Exception as e:
            print("Error/No solución:", e)
        print()


if __name__ == "__main__":
    main()
