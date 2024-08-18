import random

def movie_input():
    movie1 = input("Please enter movie 1: ")
    movie2 = input("Please enter movie 2: ")
    movie3 = input("Please enter movie 3: ")    
    movie4 = input("Please enter movie 4: ")    
    return movie1, movie2, movie3, movie4

movies = list(movie_input())
    
choice_1 = random.choices(movies)
print(choice_1)
