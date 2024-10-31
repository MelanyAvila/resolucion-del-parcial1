from funciones.generales import *
from funciones.concretas import *

depositos = ['PBA', 'CABA', 'Chubut', 'Tucumán', 'Mendoza']
productos = ['autos', 'muñecas', 'trenes', 'peluches', 'spinners', 'cartas']

ejecutar = True 
carga = True #! true para que directamente no entre al if

# matriz de ejemplo para no cargar a cada rato
matriz_ejercicio = [[3, 5, 3, 7, 3, 50000], [4, 5, 6, 7, 8, 8], [2, 55000, 2, 3, 4, 3], [2, 4, 5, 6, 7, 6], [9, 3, 2, 4, 6, 5]]

while ejecutar == True:
    print('''\nOpciones a realizar:
          1- obtener existencias.
          2- calcular juguetes por depósito.
          3- calcular juguetes que necesitan reposición.
          4- calcular en que depósito se encuentra la mayor cantidad de juguetes de cada tipo.
          5- cargar precios y luego calcular depósito con mayor recaudación
          6- depósitos con más de 50.000 unidades.
          7- calcular el porcentaje de juguetes de cada tipo sobre el total.

          10- salir \n''')

    opcion = input('ingrese la opcion que desea realizar: ')

    match opcion:
        case '1':
            if carga == False: 
                #! depositos (filas = i), juguetes (columnas = j)
                matriz_ejercicio = inicializar_matriz(len(depositos), len(productos), 0)

                for i in range(len(depositos)):
                    for j in range(len(productos)):
                        cantidad = int(input(f'Ingrese cantidad de {productos[j]} en {depositos[i]}: '))
                        matriz_ejercicio[i][j] = cantidad
                carga = True
            else:
                mostrar_matriz(matriz_ejercicio) 
        case '2':
            lista_totales = calcular_totales(matriz_ejercicio)
            for i in range(len(depositos)):
                print(f'en {depositos[i]} hay {lista_totales[i]} productos')
        case '3':
           controlar_cantidad(matriz_ejercicio, depositos, productos)
        case '4':
            '''acá cambie el codigo que el profe dio porque en mi matriz de ejemplo 
            habia depositos con las mismas cantidades en los tipos y daba cualquier cosa. 
            Ahora, si dos o más depositos tienen la misma cantidad, va a decir que el que más tiene 
            es el primero que recorra'''
            for i in range(len(productos)):
                maximo = -1 # empece con un valor menor que cualquier cantidad posible de juguetes
                deposito_maximo = 0 # bandera para el nombre del depósito con la máxima cantidad
                for j in range(len(depositos)):
                    if matriz_ejercicio[j][i] > maximo:
                        maximo = matriz_ejercicio[j][i]
                        deposito_maximo = depositos[j]
                print(f'el deposito con más {productos[i]} es {deposito_maximo}')     
        case '5':
            # matriz de ejemplo para no cargar a cada rato
            matriz_precios = [[331, 52, 36, 77, 39, 101], 
                             [466, 55, 64, 87, 968, 48], 
                             [210, 100, 201, 334, 44, 32], 
                             [233, 445, 435, 336, 347, 46], 
                             [91, 311, 200, 45, 69, 599999999999999991]]
            
            if carga == False:
                matriz_precios = inicializar_matriz(len(depositos), len(productos), 0)

                for i in range(len(depositos)):
                    for j in range(len(productos)):
                        precio = float(input(f'Ingrese el precio de {productos[j]} en {depositos[i]}: '))
                        matriz_precios[i][j] = precio
                carga = True

            recaudaciones = calcular_recaudacion(matriz_ejercicio, matriz_precios)
            bandera_r = False
            
            for i in range(len(recaudaciones)):
                if bandera_r == False:
                    maximo = recaudaciones[i]
                    deposito = depositos[i]
                    bandera_r = True
                elif recaudaciones[i] > maximo:
                    maximo = recaudaciones[i]
                    deposito = depositos[i]

            print(f'el depósito con más recaudación es {deposito}')
        case '6':
            lista_totales = calcular_totales(matriz_ejercicio)

            depositos_mas_50k = []
            
            for i in range (len(lista_totales)):
                if lista_totales[i] > 50000:
                    depositos_mas_50k += [depositos[i]]
            print(f'depositos con más de 50000 unidades: {depositos_mas_50k} (son {len(depositos_mas_50k)})')           
        case '7':
            pass
        case '8':
            pass
        case '9':
            pass
        case '10':
            print('ejercicio terminado!!')
            ejecutar = False

# 7. Porcentaje de juguetes de cada tipo sobre el total de juguetes almacenados. Realizar
# una función que muestre el porcentaje de cada uno.
# 8. Generar un informe con la recaudación de cada depósito, ordenada de mayor a menor
# usando insertion sort o quick sort. Justificar la elección del algoritmo. Para ello la
# función deberá recibir una matriz de ventas, y una lista de precios.
# 9. Generar una función que permita corregir un error de carga mediante carga aleatoria o
# distribuida de matrices.