# Código para resolver un Sudoku con backtracking y recursividad

# Esta función muestra el Sudoku de una manera más simple y limpia

def print_sudoku(sudoku):
    # Itera sobre cada fila del Sudoku
    for i in range(9):
        # Imprime una línea de separación cada 3 filas
        if i == 3 or i == 6:
            print("|-------+-------+-------|")
        
        # Itera sobre cada columna de la fila actual
        for j in range(9):
            # Imprime una separación cada 3 columnas
            if j % 3 == 0:
                print("| ", end="")
            
            # Muestra el número si no es cero, de lo contrario muestra un punto
            if sudoku[i][j]:
                print(str(sudoku[i][j]) + " ", end="")
            else:
                print(". ", end="")
        # Finaliza la línea actual
        print("|")

# Esta función comprueba si se puede añadir un número dada una casilla

def valido(sudoku, num, i, j):
    # Comprueba que el número no esté en la fila actual
    fila = sudoku[i]
    
    # Comprueba que el número no esté en la columna actual
    columna = [fila[j] for fila in sudoku]
    
    # Comprueba que el número no esté en el bloque 3x3 actual
    bloque = [sudoku[a][b]
              for a in range(9)
              for b in range(9)
              if i // 3 == a // 3
              and j // 3 == b // 3]
    
    # Retorna verdadero si el número no está en la fila, columna, ni en el bloque
    return num not in fila and num not in columna and num not in bloque
    
# Esta función contiene la lógica para solucionar el Sudoku

def resolver(sudoku):
    # Recorre cada fila del Sudoku
    for i in range(9):
        # Recorre cada columna de la fila actual
        for j in range(9):
            # Comprueba las casillas que están vacías (contienen 0)
            if sudoku[i][j] == 0:
                # Intenta colocar cada número del 1 al 9
                for num in range(1, 10):
                    # Comprueba si el número se puede colocar en la posición actual
                    if valido(sudoku, num, i, j):
                        # Coloca el número en la casilla
                        sudoku[i][j] = num
                        # Llama recursivamente a la función para continuar con la solución
                        if resolver(sudoku):
                            return True
                        else:
                            # Si no funciona, resetea la casilla a 0
                            sudoku[i][j] = 0
                
                # Esto es el backtracking: si me quedo atrapado, vuelvo atrás
                return False
    # Retorna verdadero si el Sudoku está solucionado
    return True
                        
# MAIN----------------------------------------------

# Creamos el Sudoku inicial con algunas casillas llenas
sudoku = [
    [0,0,0,0,0,0,0,5,7],
    [0,0,0,0,0,6,0,0,0],
    [1,0,0,7,0,0,0,9,6],
    [6,0,0,0,0,0,4,0,0],
    [0,0,0,0,2,0,0,0,0],
    [0,4,3,0,0,0,0,0,0],
    [0,0,8,0,1,0,0,0,9],
    [0,9,0,2,0,7,8,0,0],
    [0,0,5,0,8,4,0,7,0],
]

# Llamamos a la función que resuelve el Sudoku
resolver(sudoku)

# Imprimimos el Sudoku resuelto
print_sudoku(sudoku)
