# 2 y 6
def calcular_totales(matriz: list) -> list:
    lista_retorno = [0] * len(matriz)

    for i in range(len(matriz)):
        acumulador = 0
                
        for j in range(len(matriz[i])):
            acumulador += matriz[i][j]
                
        lista_retorno[i] = acumulador
    return lista_retorno

# 3.
def controlar_cantidad(matriz:list, lista_nombres_1:list, lista_nombres_2:list, minimo:int = 500)-> None:
    '''
    Verifica la cantidad de productos en una matriz y notifica si hay que reponer.
    Recibe la matriz que contiene las cantidades, la lista de los nombres de los depositos y la de los productos.
    Imprime que productos hay que reponer y en que deposito.
    '''
    for i in range(len(matriz)):                
        for j in range(len(matriz[i])):
            if matriz[i][j] < minimo:
                print(f"Hay que reponer {lista_nombres_2[j]} en {lista_nombres_1[i]}")

# 5.
def calcular_recaudacion(matriz: list, lista_precios: list)-> list:
    '''
    Esta función calcula recaudación.
    Recibe una matriz con las ventas y una lista con precios de productos.
    Devuelve una lista con recaudación por depósito.  
    '''
    lista_return = [0] * len(matriz)
      
    for i in range(len(matriz)):
        recaudacion = 0 
        for j in range(len(matriz[i])):
            recaudacion += (matriz[i][j] * lista_precios[i][j])
            
        lista_return[i] = recaudacion
                 
    return lista_return


# Intento de 2, 6 y 7
# def calcular_totales(matriz: list, modo: str) -> list:
#     lista_return = [0] * len(matriz)
#     total_general = 0

#     for i in range(len(matriz)):
#         for j in range(len(matriz[i])):
#             total_general += matriz[i][j]

#     for i in range(len(matriz)):
#         suma_fila = 0
#         for j in range(len(matriz[i])):
#             suma_fila += matriz[i][j]
        
#         if modo == "1":
#             lista_return[i] = suma_fila
#         elif modo == "2" and total_general > 0:
#             lista_return[i] = (suma_fila / total_general) * 100 

#     return lista_return

