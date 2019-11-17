import imdb

hr = imdb.IMDb()

movie_name = input("Enter Movie Name : ")
movies = hr.search_movie(str(movie_name))
index = movies[0].getID()
movie = hr.get_movie(index)
title = movie['title']
year = movie['year']
cast = movie['cast']
list_of_cast = ','.join(map(str, cast))
print("Title", title)
print("Year of Release", year)
print("Full Cast", list_of_cast)
