"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Hemos acabado el trabajo
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import shellsort as ls

from time import process_time 


def loadCSVFile (file, cmpfunction):
    lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst
#Comparación de datos

def compareRecordIds (element1, element2):
    if int(element1["id"]) == int(element2["id"]):
        return 0
    elif int(element1["id"]) > int(element2["id"]):
        return 1
    return -1

#Ordenamiento de datos

def topMovies(element1, element2):
    if (int(element1['vote_count']) > int(element2['vote_count'])):
        return True
    return False

def lowMovies(element1, element2):
    if (int(element1['vote_count']) < int(element2['vote_count'])):
        return True
    return False

def topMoviesAve(element1, element2):
    if (float(element1['vote_average']) > float(element2['vote_average'])):
        return True
    return False

def lowMoviesAve(element1, element2):
    if (float(element1['vote_average']) < float(element2['vote_average'])):
        return True
    return False



# Cargador de Datos

def loadMovies():
    lst = loadCSVFile("Data/SmallMoviesDetailsCleaned.csv", compareRecordIds)
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def loadCasting():
    lst = loadCSVFile("Data/MoviesCastingRaw-small.csv", compareRecordIds)
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

#Consola
def printMenu():
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Ranking de películas")
    print("4- Conocer el trabajo de un director")
    print("5- Conocer el trabajo de un actor")
    print("6- Entender un género")
    print("7- Crear Ranking de un género")
    print("0- Salir")
#Función de cantidad de datos

def countElementsFilteredByColumn(criteria, column, lst):
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

# Función requerimiento 2
def topCountMovies(lstmovies):
    t1 = process_time()
    lista = []
    ls.shellSort(lstmovies, topMovies)
    for i in range(1, 11):
        dato = lt.getElement(lstmovies, i)
        gg = (dato['original_title'] + ": " + dato['vote_count'])
        lista.append(gg)
    t2 = process_time()
    print("El tiempo de procesamiento es de: ", t2 - t1)
    return lista
def lowCountMovies(lstmovies):
    t1 = process_time()
    lista = []
    ls.shellSort(lstmovies, lowMovies)
    for i in range(1, 11):
        dato = lt.getElement(lstmovies, i)
        gg = (dato['original_title'] + ": " + dato['vote_count'])
        lista.append(gg)
    t2 = process_time()
    print("El tiempo de procesamiento es de: ", t2 - t1)
    return lista
    
def topAveMovies(lstmovies):
    t1 = process_time()
    lista = []
    ls.shellSort(lstmovies, topMoviesAve)
    for i in range(1, 6):
        dato = lt.getElement(lstmovies, i)
        gg = (dato['original_title'] + ": " + dato['vote_average'])
        lista.append(gg)
    t2 = process_time()
    print("El tiempo de procesamiento es de: ", t2 - t1)
    return lista
def lowAveMovies(lstmovies):
    t1 = process_time()
    lista = []
    ls.shellSort(lstmovies, lowMoviesAve)
    for i in range(1, 6):
        dato = lt.getElement(lstmovies, i)
        gg = (dato['original_title'] + ": " + dato['vote_average'])
        lista.append(gg)
    t2 = process_time()
    print("El tiempo de procesamiento es de: ", t2 - t1)
    return lista

#Función requerimiento 3
def Conocer_un_director(lst, lst2, criteria):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    t1 = process_time()
    cont = 0
    valor = 0
    lista = []
    print("\n")
    ite = it.newIterator(lst2)
    while it.hasNext(ite):
        vote = it.next(ite)
        nom = vote["director_name"]
        ids = int(vote["id"])
        if criteria == vote["director_name"]:
            ite2 = it.newIterator(lst)
            while it.hasNext(ite2):
                vote2 = it.next(ite2)
                ids2 = int(vote2["id"])
                if int(ids) == int(ids2):
                    cont += 1
                    valor += float(vote2["vote_average"])
                    lista.append(vote2["original_title"])     
    if cont == 0:
        promedio = valor/1
    else:
        promedio = valor/cont
    t2 = process_time()
    print("El tiempo de procesamiento es de: ", t2 - t1)
    return str(lista) + "\nLa cantidad de películas es de: " + str(cont) + "\nSu promedio es de: " + str(round(promedio, 2))
    

#Función requerimiento 4

def Conocer_un_actor(lst, lst2, criteria):
    t1 = process_time()
    cont = 0
    valor = 0
    dicc = {}
    lista = []
    print("\n")
    ite = it.newIterator(lst2)
    while it.hasNext(ite):
        vote = it.next(ite)
        ids = int(vote["id"])
        if ((criteria == vote["actor1_name"]) or 
        (criteria == vote["actor2_name"]) or 
        (criteria == vote["actor3_name"]) or 
        (criteria == vote["actor4_name"]) or 
        (criteria == vote["actor5_name"])):
            ite2 = it.newIterator(lst)
            while it.hasNext(ite2):
                vote2 = it.next(ite2)
                ids2 = int(vote2["id"])
                if int(ids) == int(ids2):
                    cont += 1
                    valor += float(vote2["vote_average"])
                    lista.append(vote2["original_title"])
                    #print(vote2["original_title"])
                    if (vote["director_name"]) in dicc:
                        dicc[vote["director_name"]] += 1
                    else:
                        dicc[vote["director_name"]] = 1  
    #print("La cantidad de películas es de: " + str(cont))      
    if cont == 0:
        promedio = valor/1
    else:
        promedio = valor/cont
    #print("Su promedio es de: " + str(round(promedio, 2)))
    m = (max(dicc.values()))
    for i in dicc:
        if m == dicc[i]:
            va = "\nEl director con el que tiene más colaboraciones es: " + i
    t2 = process_time()
    print("El tiempo de procesamiento es de: ", t2 - t1)
    return str(lista) + "\nLa cantidad de películas es de: " + str(cont) + "\nSu promedio es de: " + str(round(promedio, 2)) + va

#Función requerimiento 5

def Entender_un_genero(lst, criteria): 
    t1 = process_time()
    lista = []
    conta = 0
    valor = 0
    ite = it.newIterator(lst)
    while it.hasNext(ite):
        peli = it.next(ite)
        if criteria in peli["genres"]:
            conta += 1
            lista.append(peli["original_title"])
            valor += float(peli["vote_average"])
    promedio = valor/conta
    rep1 = "\nsu lista de películas es: "+ str(lista)
    rep2 = "\nLa cantidad de películas es: " + str(conta)
    rep3 = "\nEl promedio total es de: "+ str(round(promedio, 2))
    t2 = process_time()
    print("El tiempo de procesamiento es de: ", t2 - t1)
    return rep1 + rep2 + rep3

#Requerimiento 6
def Ranking_del_genero(lst, criteria, orden):
    lista = lt.newList('ARRAY_LIST')
    i = 0
    while i < lt.size(lst):
        valor = lt.getElement(lst, i)
        if criteria in valor["genres"]:
            lt.addFirst(lista, valor)
        i += 1   
    a = 0
    b = 0
    c = 0
    d = 0
    lista2 = []
    lista3 = []
    if orden == "mayor":
        ls.shellSort(lista, topMovies)
        for i in range(1, 11):
            dato = lt.getElement(lista, i)
            a += int(dato["vote_count"])
            lista2.append(dato['original_title'] + ": " + dato['vote_count'])
            #print (dato['original_title'] + ": " + dato['vote_count'])
        promedio = a/10
        count = "\nEl promedio del count es: " + str(promedio)
        ls.shellSort(lista, topMoviesAve)
        for i in range(1, 6):
            dato = lt.getElement(lista, i)
            b += float(dato["vote_average"])
            lista3.append(dato['original_title'] + ": " + dato['vote_average'])
            #print (dato['original_title'] + ": " + dato['vote_average'])
        promedio2 = b/5
        average = "\nEl promedio del average es: " + str(promedio2)
    elif orden == "menor":
        ls.shellSort(lista, lowMovies)
        for i in range(1, 11):
            dato = lt.getElement(lista, i)
            c += int(dato["vote_count"])
            lista2.append(dato['original_title'] + ": " + dato['vote_count'])
            #print (dato['original_title'] + ": " + dato['vote_count'])
        promedio3 = c/10
        count ="\nEl promedio del count es: " + str(promedio3)
        ls.shellSort(lista, lowMoviesAve)
        for i in range(1, 6):
            dato = lt.getElement(lista, i)
            d += float(dato["vote_average"])
            lista3.append(dato['original_title'] + ": " + dato['vote_average'])
            #print (dato['original_title'] + ": " + dato['vote_average'])
        promedio4 = d/5
        average = "\nEl promedio del average es: " + str(promedio4)
    return "\nSus películas por count: \n" + str(lista2) + count + "\nSus películas por average: \n" + str(lista3) + average

# Consola
def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lstmovies = loadMovies()
                lstcasting = loadCasting()
            elif int(inputs[0])==2: #opcion 2
                if lstmovies==None or lt.size(lstmovies)==0: #obtener la longitud de la lista
                    print("La lista esta vacía")   
                else: print("La lista tiene ",lstmovies['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                a = int(input("selecciones una opción: \n" + "1. 10 mejores películas votadas\n"
                + "2. 10 peores películas votadas\n" + "3. 5 mejores películas según su promedio\n"
                + "4. 5 peores películas según su promedio\n" + ": " ))
                if a == 1:
                    resp = topCountMovies(lstmovies)
                    print(resp)
                elif a == 2:
                    resp = lowCountMovies(lstmovies)
                    print(resp)
                elif a == 3:
                    resp = topAveMovies(lstmovies)
                    print(resp)
                elif a == 4:
                    resp = lowAveMovies(lstmovies)
                    print(resp)
                    
            elif int(inputs[0])==4: #opcion 4
                if lstmovies==None or lstmovies['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    print("La información de su director: \n")
                    criteria =input('Ingrese el nombre del director a buscar: \n')
                    counter= Conocer_un_director(lstmovies, lstcasting, criteria)
                    print(counter)
            elif int(inputs[0])==5: #opcion 5
                if lstmovies==None or lstmovies['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    resp = Conocer_un_actor(lstmovies, lstcasting, criteria)
                    print(resp)
            elif int(inputs[0])==6: #opcion 5
                if lstmovies==None or lstmovies['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    rep = Entender_un_genero(lstmovies, criteria)
                    print(rep)
            elif int(inputs[0])==7: #opcion 5
                if lstmovies==None or lstmovies['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input(str('Ingrese el criterio de búsqueda\n'))
                    crite = input("Si desea los mejores escriba: mayor y si desea los peores escriba: menor\n")
                    rep = Ranking_del_genero(lstmovies, criteria, crite)
                    print(rep)
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()
