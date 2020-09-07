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
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv

from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from time import process_time 



def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Ranking de peliculas")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un genero")
    print("6- Crear ranking")
    print("0- Salir")




def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1

"""
SOLUCIÓN GRUPO 8 SECCIÓN 4
Jessica Robles, Mª Paula Gonzales y Martin Ubaque
"""
def less(element1, element2, criteria):
    if float(element1[criteria]) < float(element2[criteria]):
        return True
    return False
"""
SOLUCIÓN GRUPO 8 SECCIÓN 4
Jessica Robles, Mª Paula Gonzales y Martin Ubaque
"""
def greater (element1,element2, criteria):
    if float(element1[criteria]) > float(element2[criteria]):
        return True
    return False
"""
SOLUCIÓN GRUPO 8 SECCIÓN 4
Jessica Robles, Mª Paula Gonzales y Martin Ubaque
"""
def selectionSort (lst, lessfunction, criteria,size):    #Se utiliza selection sort para que se organicen solo las primeras posiciones del ranking, y así
    pos1 = 1                                             #gastar menos timepo con los archivos large
    while pos1 < size:
        minimum = pos1              
        pos2 = pos1 + 1
        while (pos2 <= lt.size(lst)):
            if (lessfunction (lt.getElement(lst, pos2),lt.getElement(lst, minimum),criteria)): 
                minimum = pos2      # minimum se actualiza con la posición del nuevo elemento más pequeño
            pos2 += 1
        lt.exchange (lst, pos1, minimum)  # se intercambia el elemento más pequeño hasta ese punto con el elemento en pos1
        pos1 += 1
"""
SOLUCIÓN GRUPO 8 SECCIÓN 4
Jessica Robles, Mª Paula Gonzales y Martin Ubaque
"""
def orderElementsByCriteria(function, column, lst, elements):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    if column == "1":
        column="vote_count"
    elif column == "2":
        column="vote_average"
    else:
        print("Valor no valido para criterio de busqueda")
    lista=lt.newList("ARRAY_LIST")
    if function=="1":
        selectionSort(lst,greater,column, (int(elements)+1))
    elif function=="2":
        selectionSort(lst,less,column, (int(elements)+1))
    for i in range(1,(int(elements)+1)):
        lt.addLast(lista, lt.getElement(lst, i))
    return lista

def loadCSVFile (file, cmpfunction):
    lst=lt.newList("ARRAY_LIST", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        print(cf.data_dir + file)
        with open(  cf.data_dir + file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst


def loadMovies ():
    lst = loadCSVFile("themoviesdb/SmallMoviesDetailsCleaned.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def loadCasting ():
    lst = loadCSVFile("themoviesdb/MoviesCastingRaw-small.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst
def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """

    lstmovies = lt.newList()   # se require usar lista definida
    lstcasting = lt.newList()
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                lstmovies = loadMovies()
                lstcasting = loadCasting()
            elif int(inputs[0])==2: #opcion 2
                if lstmovies==None or lstmovies['size']==0: #obtener la longitud de la lista
                    print("La lista details esta vacía")  
                elif lstcasting==None or lstcasting['size']==0: #obtener la longitud de la lista
                    print("La lista casting esta vacía")    
                else: 
                    criteria =input('Ingrese 1 si el criterio de busqueda es COUNT o ingrese 2 si es AVERAGE\n')
                    crecimiento =input("Ingrese 1 si quiere la lista de las 10 mejores películas, o 2 si quiere la lista de las 10 peores películas.\n")
                    tamaño = 10
                    lista=orderElementsByCriteria(crecimiento,criteria,lstmovies,tamaño)
                    print ("La lista solicitada es:")
                    iterator = it.newIterator(lista)
                    i=1
                    while  it.hasNext(iterator):
                        element = it.next(iterator)
                        print(str(i)+"- "+element["original_title"])
                        i += 1

            elif int(inputs[0])==3: #opcion 3
                pass

            elif int(inputs[0])==4: #opcion 4
                pass

            elif int(inputs[0])==3: #opcion 5
                pass

            elif int(inputs[0])==4: #opcion 6
                pass


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()