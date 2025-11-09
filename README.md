# Proyecto Lights Out — ÁLGEBRA APLICADA (2025)

Trabajo de curso: implementación y análisis del juego "Lights Out" usando álgebra lineal sobre GF(2).

Descripción breve
------------------
Este repositorio contiene una implementación en Python que modela el juego Lights Out como un sistema lineal sobre el cuerpo finito de dos elementos 1 y 0 (GF(2)). La idea central es transformar el problema de apagar todas las luces en resolver un sistema Ax = b donde A es la matriz de interacción (cada pulsación afecta a una celda y sus vecinos ortogonales), x es el vector de pulsaciones y b es el estado inicial (1 = luz encendida, 0 = apagada).

Estructura del repositorio
--------------------------
- `consigna6.py`: módulo principal que construye el sistema lineal, ejecuta la eliminación gaussiana en GF(2) (usando solamente operaciones de la forma Fi <- Fi + Fj, es decir suma/XOR de filas) y devuelve una solución particular cuando existe.
- `main.py`: script de ejemplo que muestra cómo usar el solver con tableros de ejemplo.
- `utils.py`: utilidades pequeñas (impresión de matrices, helpers para tests).
- `tests/test_consigna6.py`: pruebas unitarias con `pytest` que validan casos simples y la aplicabilidad de la solución calculada.
- `README.md`: este archivo.

Algoritmo (explicado de forma sencilla)
--------------------------------------
1. Modelado:
	 - Sea el tablero de tamaño n x n. Se asocia a cada celda (i,j) una incógnita x_k indicando si se pulsa esa celda (1) o no (0). Se ordenan las celdas en orden fila-major para formar el vector x de longitud N = n*n.
	 - Se construye la matriz A (N x N) tal que la fila k contiene unos en las posiciones correspondientes a la celda k y sus vecinos (arriba/abajo/izquierda/derecha). El vector b es el tablero inicial aplanado (1 para luces encendidas).

2. Resolución en GF(2):
	 - Todo se hace en aritmética binaria (0/1) con suma XOR (sin multiplicaciones reales).
	 - Se aplica una eliminación gaussiana adaptada para GF(2). La consigna exige que la única operación elemental permitida sea Fi <- Fi + Fj (XOR de filas). No se usan swaps de filas. Para crear un pivote cuando la diagonal es 0, se suma la fila actual con alguna fila que tenga un 1 en esa columna(operación autorizada).
	 - Después de la eliminación hacia adelante, se detectan filas inconsistentes (todas las entradas 0 y término independiente 1). Si aparece una fila así, el sistema no tiene solución.
	 - En la sustitución hacia atrás se fijan las variables libres (si las hay) a 0 para obtener una solución particular.

3. Verificación:
	 - El código incluye `apply_solution(board, x)` que aplica el vector de pulsaciones resultante y comprueba que todas las luces quedan apagadas. Las pruebas usan esta comprobación en lugar de comparar una única solución posible, porque el espacio de soluciones puede no ser único.

Cómo ejecutar (requisitos mínimos)
----------------------------------
- Python 3.8+ (se probó con Python 3.11/3.13)
- pytest (opcional, para correr tests)

Comandos útiles
---------------
Para ejecutar los ejemplos en `main.py`:
```powershell
python main.py
```

Para ejecutar las pruebas unitarias:
```powershell
python -m pytest -q
```

Comentarios finales
-------------------------------------
Este proyecto fue implementado como trabajo práctico del curso. Tratamos de mantener el código claro y comentado. Las funciones públicas principales del módulo son `solve_lights_out(board)` (devuelve la matriz de pulsaciones n x n) y `apply_solution(board, x)` (aplica un vector de pulsaciones y devuelve el tablero resultante).


Autores
-------
- Grupo: Matías Anselmo, Lucía Bonilla, Paulina Vidal (2025)