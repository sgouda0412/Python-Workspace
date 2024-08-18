import random

films = []

film1 = input("Please enter a first film: ")
film2 = input("Please enter a second film: ")
film3 = input("Please enter a third film: ")
films.append(film1)
films.append(film2)
films.append(film3)
random.sample(films, len(films))[0]
