def inicializar_matriz(cant_filas: int, cant_colunmnas: int, valor_inicial: any = 0)-> list:
    '''
    Inicializa una matriz de dimensiones específicas, inicializando todos los elementos con un valor dado.
    Recibe el valor inicial y los numeros de filas y columnas.
    Retorna una matriz (lista de listas).
    '''
    matriz = []

    for _ in range(cant_filas):
        fila = [valor_inicial] * cant_colunmnas
        matriz += [fila]

    return matriz

def mostrar_matriz(matriz: list)-> None:
    '''
    Imprime una matriz en la consola de forma legible, mostrando cada fila en una línea separada.
    Recibe la matriz que se quiere imprimir.
    No retorna ningún valor, solo imprime.
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = ' ')
        print(' ')

#* hacer funcion para cargar secuncialmente para simplificar un poco el main