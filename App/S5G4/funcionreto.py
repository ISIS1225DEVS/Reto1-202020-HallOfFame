from Sorting import shellsort as shsort
from DataStructures import listiterator
from DataStructures import liststructure as lt
from ADT import list as lt
from Sorting import config as cfdos
from time import process_time 

def less(element1, element2):
    if int(element1['goodreads_book_id']) < int(element2['goodreads_book_id']):
        return True
    return False



def moviesByActor(casting, details):
    peliculas_dirigidas_por_x_director = lt.newList('SINGLE_LINKED', None)
    actor = input("Ingrese el actor:\n")

    t1_start = process_time()

    iter = listiterator.newIterator(casting)
    while listiterator.hasNext(iter):
        d = listiterator.next(iter)
        if d["actor1_name"] == actor or d["actor2_name"] == actor or d["actor3_name"] == actor or d["actor4_name"] == actor or d["actor5_name"] == actor:        
            lt.addFirst(peliculas_dirigidas_por_x_director, d)
            


    peliculas = lt.newList('SINGLE_LINKED', None)

    directores = {}

    iter1 = listiterator.newIterator(peliculas_dirigidas_por_x_director)
    while listiterator.hasNext(iter1):
        ide = listiterator.next(iter1)

        iter2 = listiterator.newIterator(details)
        while listiterator.hasNext(iter2):
            p = listiterator.next(iter2)

            if ide["id"] == p["id"]:
                lt.addFirst(peliculas, p)
                print(p["original_title"])
                if ide["director_name"] in directores:
                    directores[ide["director_name"]] += 1
                else:
                    directores[ide["director_name"]] = 1


    #encontrar directores pelis
    maximo_colab = max(directores, key=directores.get)  
    


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

    #print("Peliculas dirigidas por "+ director +": " + str(peliculas['title'])) Encontrar los nombres de las peliculas
    print("Numero de películas de "+ actor + ": " + str(numero_peliculas_director))
    print("Promedio de calificación de las peliculas del actor: " + str(promedio_pelis))
    print("el director con mayor número de colaboraciones es: " + maximo_colab)