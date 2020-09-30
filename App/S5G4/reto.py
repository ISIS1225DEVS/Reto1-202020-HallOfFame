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
import funcionreto

from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import config as cfdos 
import F3y5

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



def loadCSVFile (file, cmpfunction):
    lst=lt.newList("ARRAY_LIST", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(  cf.data_dir + file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst



def loadMovies ():
    lst = loadCSVFile(('themoviesdb\AllMoviesDetailsCleaned.csv'),compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def loadMovieCast ():
    lst = loadCSVFile(("themoviesdb\AllMoviesCastingRaw.csv"),compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst
1
#Cargar archivos
def crear_lista(camino):
    
    lista = lt.newList('SINGLE_LINKED', None)
    with open(camino, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            lt.addFirst(lista, row)
    return lista

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """


    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs = input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                details = loadMovies()
                casting = loadMovieCast()

            elif int(inputs[0])==2: #opcion 2

                paramet2= input("ingrese según que quiere organizar las películas: AVERAGE para calificación, y COUNT para número de votos.: ")
                if paramet2 != str("AVERAGE") and paramet2 != str("COUNT"):
                    print("no es posible cargar con ese parametro")
                else:
                    resultado = F3y5.crear_ranking2(details,paramet2)
                    print("Top-5: ", resultado[0])
                    print("Peores 5: ", resultado[1])


            elif int(inputs[0])==3: #opcion 3
                director = input("Ingrese el director\n")
                ruta_casting = "Data/themoviesdb\AllMoviesCastingRaw.csv"
                ruta_details = 'Data/themoviesdb\AllMoviesDetailsCleaned.csv'
                #ruta_casting = "Data/themoviesdb\MoviesCastingRaw-small.csv"
                #ruta_details = "Data/themoviesdb\SmallMoviesDetailsCleaned.csv"
                casting = crear_lista(ruta_casting)
                details = crear_lista(ruta_details)
                resultado = F3y5.moviesByDirector(director,casting,details)
                print(resultado)

            elif int(inputs[0])==4: #opcion 4
                ruta_casting = "Data/themoviesdb\AllMoviesCastingRaw.csv"
                ruta_details = 'Data/themoviesdb\AllMoviesDetailsCleaned.csv'
                #ruta_casting = "Data/themoviesdb\MoviesCastingRaw-small.csv"
                #ruta_details = "Data/themoviesdb\SmallMoviesDetailsCleaned.csv"
                casting = crear_lista(ruta_casting)
                details = crear_lista(ruta_details)
                funcionreto.moviesByActor(casting, details)

            elif int(inputs[0])==5: #opcion 5
                genero = input('inserte el género de su interes\n')
                resultado = F3y5.moviesByGenre(genero,casting,details)
                print(resultado)

            elif int(inputs[0])==6: #opcion 6
                parametro= input("ingrese según que quiere organizar las películas: AVERAGE para calificación, y COUNT para número de votos.: ")
                if parametro != str("AVERAGE") and parametro != str("COUNT"):
                    print("no es posible cargar con ese parametro")
                else:
                    genero = input('inserte el género de su interes\n')
                    resultado = F3y5.mejoresgenero(details, parametro, genero)
                    print("Top-5: ", resultado[0])
                    print("Peores 5: ", resultado[1])
                


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
            
            else:
                print ("resultado no vállido.")

                
if __name__ == "__main__":
    main()