# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
from textwrap import indent
from turtle import color
import requests

import matplotlib.pyplot as plt
from sqlalchemy import true


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    response = requests.get("https://jsonplaceholder.typicode.com/todos")

    data = response.json()

    lista_comprimida = []

    userId_1 = 0
    userId_2 = 0
    userId_3 = 0 
    userId_4 = 0
    userId_5 = 0
    userId_6 = 0
    userId_7 = 0
    userId_8 = 0
    userId_9 = 0
    userId_10 = 0

    for i in range(len(data)):
        id = data[i]
        completed = id.get('completed')
        if completed == True:
            lista_comprimida.append(id)
            
    for i in range(len(lista_comprimida)):
        if lista_comprimida[i]['userId'] == 1:
            userId_1 += 1
        elif lista_comprimida[i]['userId'] == 2:
            userId_2 += 1
        elif lista_comprimida[i]['userId'] == 3:
            userId_3 += 1
        elif lista_comprimida[i]['userId'] == 4:
            userId_4 += 1
        elif lista_comprimida[i]['userId'] == 5:
            userId_5 += 1
        elif lista_comprimida[i]['userId'] == 6:
            userId_6 += 1
        elif lista_comprimida[i]['userId'] == 7:
            userId_7 += 1
        elif lista_comprimida[i]['userId'] == 8:
            userId_8 += 1
        elif lista_comprimida[i]['userId'] == 9:
            userId_9 += 1
        else:
            userId_10 += 1

    eje_x = ["userId 1","userId 2","userId 3","userId 4","userId 5","userId 6","userId 7","userId 8","userId 9","userId 10"]
    eje_y = [userId_1,userId_2,userId_3,userId_4,userId_5,userId_6,userId_7,userId_8,userId_9,userId_10]
        
    figura = plt.figure()
    ax = figura.add_subplot()
    ax.bar(eje_x,eje_y, label="Títulos completados")
    ax.set_facecolor('whitesmoke')
    ax.legend()
    plt.show()

    print("terminamos")