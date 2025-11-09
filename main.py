"""
Script de ejecución separado para `consigna6`.
"""
from consigna6 import solve_lights_out
from utils import print_matrix

def main():
    examples = {
        "todo_cero_3x3": [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        "una_luz_3x3": [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ],
        "conocido_3x3": [
            [0, 0, 0],
            [1, 0, 0],
            [0, 0, 1]
        ],
        "conocido_5x5":[
            [1, 0, 1, 0, 0],
            [1, 0, 1, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1],
            [0, 1, 1, 0, 1]
        ],
        "conocido_7x7": [
            [1, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0],
            [1, 1, 0, 1, 1, 0, 1],
            [1, 1, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 1, 0],
            [1, 0, 0, 1, 1, 1, 0]
        ]
        # Agregar aquí otros tableros para ver su solución.
    }

    for name, initial_board in examples.items():
        print(f"-- Ejemplo: {name}")
        print_matrix(initial_board)
        try:
            solution = solve_lights_out(initial_board)
            print("Solución (matriz):")
            print_matrix(solution)
        except Exception as e:
            print("Error/No solución:", e)
        print()

if __name__ == "__main__":
    main()
