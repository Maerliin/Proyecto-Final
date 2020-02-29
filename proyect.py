##Este programa donde se despliega una lista de peliculas

import random
from os import system as comando
class Movie:
    """
    Esta clase es para almacenar datos de peliculas y su calificación.
    """
    def __init__(self, titulo):
        self.titulo = titulo
        self.rank = random.randint(1,10)
        print("La pelicula %s tiene un rango de %i " %(self.titulo, self.rank))
    def like(self):
        """
        Esta metodo aumenta el rango de la pelicula en 1.
        """
        self.rank  += 1
        print("La pelicula %s aumento su rango a %i" %(self.titulo, self.rank))
    def dislike(self):
        """
        Esta metodo baja el rango de la pelicula en 1.
        """
        self.rank  -= 1
        print("La pelicula %s bajo su rango a %i" %(self.titulo, self.rank))
    def display(self):
        """
        Esta metodo indica el nombre de la pelicula en mayuscula la primer letra de cada palabra.
        """
        lista = self.titulo
        lista = list(lista.split(" "))
        peli = ""
        for palabra in lista:
            peli += (palabra.capitalize() + " ")
        print("La pelicula %s tiene el gango de: %i" %(self.titulo.capitalize(), self.rank))


    



comando ("cls")
pelicula0 = Movie("malefic")
pelicula0.like()
pelicula0.dislike()
pelicula0.display()

pelicula1 = Movie("virus")
pelicula2 = Movie("tangled")
pelicula3 = Movie("frozen")
pelicula4 = Movie("los pitufos")
pelicula5 = Movie("violet")
pelicula6 = Movie("mary shelley")
pelicula7 = Movie("shadowhunters")
pelicula8 = Movie("your name")
pelicula9 = Movie("train to busan")


