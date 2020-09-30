from Sorting import quicksort as qc
import config as conf
import csv
from ADT import list as lt
from DataStructures import listiterator
from time import process_time


def moviesByDirector(director,casting,details):
    """
    Función 3
    Conocer a un director
    director: nombre del director

    Como aficionado del cine Quiero
    conocer el trabajo de un director.
    """

    peliculas_dirigidas_por_x_director = lt.newList('SINGLE_LINKED', None)
    
    iter = listiterator.newIterator(casting)
    while listiterator.hasNext(iter):
        d = listiterator.next(iter)
        if d["director_name"] == director:
            lt.addFirst(peliculas_dirigidas_por_x_director, d)
        

    peliculas = lt.newList('SINGLE_LINKED', None)



    iter1 = listiterator.newIterator(peliculas_dirigidas_por_x_director)
    while listiterator.hasNext(iter1):
        ide = listiterator.next(iter1)

    iter2 = listiterator.newIterator(details)
    while listiterator.hasNext(iter2):
        p = listiterator.next(iter2)

        if ide["id"] == p["id"]:
            lt.addFirst(peliculas, p)
            print (p["original_title"])
            


    #encontrar los datos

    numero_peliculas_director = lt.size(peliculas)
    suma_promedio_voto = 0
 

    iter = listiterator.newIterator(peliculas)
    while listiterator.hasNext(iter):
        s = listiterator.next(iter)
        suma_promedio_voto += float(s["vote_average"])


    promedio_pelis = 0
    if(numero_peliculas_director > 0):
        promedio_pelis = suma_promedio_voto/numero_peliculas_director
    resultado = {}
    resultado["Numero de películas de "+ director] = numero_peliculas_director
    resultado["Promedio de calificación de las peliculas del director "] = promedio_pelis
    return resultado







#FUNCION 5









def moviesByGenre(genero,casting,details):
    """
    
    Funcion 5:
    genero: género de intéres
    casting: info del archivo csv casting
    details: info del archivo csv details cleaned

    Como aficionado del cine Quiero
    entender las características de un
    genero de películas.

    Las condicionesson:
    −El nombre del genero
    cinematográfico (genres).

    """

    peliculas_del_genero = lt.newList('SINGLE_LINKED', None)
    iter = listiterator.newIterator(details)
    while listiterator.hasNext(iter):
        d = listiterator.next(iter)
        if genero in d["genres"]:
            lt.addFirst(peliculas_del_genero, d)
            print(d["original_title"])


    numero_peliculas_genero = lt.size(peliculas_del_genero)
    suma_promedio_voto = 0
    nombres_peliculas = []

    iter = listiterator.newIterator(peliculas_del_genero)
    while listiterator.hasNext(iter):
        s = listiterator.next(iter)
        suma_promedio_voto += float(s["vote_count"])

    promedio_vote_count = 0
    if(numero_peliculas_genero > 0):
        promedio_vote_count = suma_promedio_voto/numero_peliculas_genero

    #mostrar la lista
    respuesta = {}
    respuesta['Numero de películas asociadas al género '+ genero] = numero_peliculas_genero
    respuesta["Promedio de votos de las peliculas del género "+ genero] = promedio_vote_count
    return respuesta


def compareRecordVotos (recordA, recordB):
    if int(recordA["vote_count"]) == int(recordB['vote_count']):
        return 0
    elif int(recordA['vote_count']) > int(recordB['vote_count']):
        return 1
    return -1

def compareRecordAverage (recordA, recordB):
    if float(recordA["vote_average"]) == float(recordB['vote_average']):
        return 0
    elif float(recordA['vote_average']) > float(recordB['vote_average']):
        return 1
    return -1


def crear_ranking(lst):
    votos_ranking = qc.quickSort(lst,compareRecordVotos)
    average_ranking = qc.quickSort(lst,compareRecordAverage)
    return (votos_ranking,average_ranking)

 
def crear_ranking2(details,parametro):
    if parametro == "AVERAGE":
        criterio = 'vote_average'
    elif parametro == "COUNT":
        criterio = 'vote_count'
    respuesta = {}
    lista_mejores = []
    #Mejores calificaciones 
    x = crear_ranking2_maximo(details,0,0,criterio,lista_mejores)
    respuesta[x[0]] =  x[1]
    lista_mejores.append(x[0])
    x2 = crear_ranking2_maximo(details,0,0,criterio,lista_mejores)
    respuesta[x2[0]] = x2[1]
    lista_mejores.append(x2[0])
    x3 = crear_ranking2_maximo(details,0,0,criterio,lista_mejores)
    respuesta[x3[0]] = x3[1]
    lista_mejores.append(x3[0])
    x4 = crear_ranking2_maximo(details,0,0,criterio,lista_mejores)
    respuesta[x4[0]] = x4[1]
    lista_mejores.append(x4[0])
    x5 = crear_ranking2_maximo(details,0,0,criterio,lista_mejores)
    respuesta[x5[0]] = x5[1]
    lista_mejores.append(x5[0])

    #Peores calificaciones
    lista_peores = []
    respuesta_peores = {}
    z = crear_ranking2_minimo(details,0,10000000,criterio,lista_peores)
    respuesta_peores[z[0]] =  z[1]
    lista_peores.append(z[0])
    z2 = crear_ranking2_minimo(details,0,10000000,criterio,lista_peores)
    respuesta_peores[z2[0]] = z2[1]
    lista_peores.append(z2[0])
    z3 = crear_ranking2_minimo(details,0,10000000,criterio,lista_peores)
    respuesta_peores[z3[0]] = z3[1]
    lista_peores.append(z3[0])
    z4 = crear_ranking2_minimo(details,0,10000000,criterio,lista_peores)
    respuesta_peores[z4[0]] = z4[1]
    lista_peores.append(z4[0])
    z5 = crear_ranking2_minimo(details,0,10000000,criterio,lista_peores)
    respuesta_peores[z5[0]] = z5[1]
    lista_peores.append(z5[0])
    
    return respuesta , respuesta_peores


def crear_ranking2_maximo(details,maximo,minimo,criterio,lista):

    iter = listiterator.newIterator(details)
    while listiterator.hasNext(iter):
        d = listiterator.next(iter)
        if float(d[criterio]) > maximo and d['title'] not in lista:
            maximo = float(d[criterio])
            nombre_max = d['title']
    return nombre_max,maximo


def crear_ranking2_minimo(details,maximo,minimo,criterio,lista):

    iter = listiterator.newIterator(details)
    while listiterator.hasNext(iter):
        d = listiterator.next(iter)
        if float(d[criterio]) <= minimo and d['title'] not in lista:
            minimo = float(d[criterio])
            nombre_min = d['title']
    return nombre_min , minimo

#FUNCION 6
def mejoresgenero(lista, parametro, genero):

    peliculas_del_genero = lt.newList('SINGLE_LINKED', None)

    iter = listiterator.newIterator(lista)
    while listiterator.hasNext(iter):
        d = listiterator.next(iter)
        if genero in d["genres"]:
            lt.addFirst(peliculas_del_genero, d)
    
    r = crear_ranking2(peliculas_del_genero, parametro)
    return r
        