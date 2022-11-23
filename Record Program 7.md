# 7. ILLUSTRATION OF BINARY FILE PROGRAMING-I
A binary file named "movies.dat" contain certain records of certain movies
(movieID, movieName, rating).Write a menu driven python program to do the
following tasks:
1. Append a movie
2. Search for a movie based on the Movie ID
3. Read and display all movies

## Source Code
```py
import pickle

f = open("movies.dat", "a") # Ensure that the file exists
f.close()

def appendMovie():
    movieID = int(input("Enter movie ID: "))
    movieName = input("Enter movie name: ")
    rating = int(input("Enter movie rating out of 10: "))


    with open("movies.dat", "ab") as f:
        pickle.dump([movieID, movieName, rating], f)

def searchMovie():
    movies = []
    with open("movies.dat", "rb") as f:
        while True:
            try: # Using a try block to catch errors
                movie = pickle.load(f)
                movies.append(movie)
            except:
                break
    
    movieID = int(input("Enter MovieID: "))

    found = False # Using a loop to search for a values
    for item in movies:
        if item[0] == movieID:
            print("--------------------")
            print("ID    :", item[0])
            print("Name  :", item[1])
            print("Rating:", item[2])
            print("--------------------")
            found = True
            break

    if not found:
        print("Movie not found")

def showMovies():
    movies = []
    with open("movies.dat", "rb") as f:
        while True:
            try: # Using a try block to catch errors
                movie = pickle.load(f)
                movies.append(movie)
            except EOFError:
                break
    for item in movies:
        print("--------------------")
        print("ID    :", item[0])
        print("Name  :", item[1])
        print("Rating:", item[2])
        print("--------------------")



while True:
    print("=============================================")
    print("What would you like to do?")
    print("""
    [1] Append a movie
    [2] Search for a movie
    [3] Show all movies
    [4] Exit
    """)

    ch = input("Enter your choice[1/2/3/4]: ")

    if ch == "1":
        appendMovie()
    
    elif ch == "2":
        searchMovie()

    elif ch == "3":
        showMovies()

    elif ch == "4":
        print("[ Exiting ]") # Break from the loop to exit
        break

    else:
        print("[ Invalid Choice ]") # In case user inputs a choice that was not defined
```

## OUTPUT
```
=============================================
What would you like to do?  

    [1] Append a movie      
    [2] Search for a movie  
    [3] Show all movies     
    [4] Exit
    
Enter your choice[1/2/3/4]: 1
Enter movie ID: 1
Enter movie name: Movie
Enter movie rating out of 10: 7
=============================================
What would you like to do?

    [1] Append a movie
    [2] Search for a movie
    [3] Show all movies
    [4] Exit

Enter your choice[1/2/3/4]: 1
Enter movie ID: 2
Enter movie name: Movie 2
Enter movie rating out of 10: 9
=============================================
What would you like to do?

    [1] Append a movie
    [2] Search for a movie
    [3] Show all movies
    [4] Exit

Enter your choice[1/2/3/4]: 1       
Enter movie ID: 3
Enter movie name: Movie 2 Sequel
Enter movie rating out of 10: 10
=============================================
What would you like to do?

    [1] Append a movie
    [2] Search for a movie
    [3] Show all movies
    [4] Exit

Enter your choice[1/2/3/4]: 3
--------------------
ID    : 1
Name  : Movie
Rating: 7
--------------------
--------------------
ID    : 2
Name  : Movie 2
Rating: 9
--------------------
--------------------
ID    : 3
Name  : Movie 2 Sequel
Rating: 10
--------------------
=============================================
What would you like to do?

    [1] Append a movie
    [2] Search for a movie
    [3] Show all movies
    [4] Exit

Enter your choice[1/2/3/4]: 2
Enter MovieID: 2
--------------------
ID    : 2
Name  : Movie 2
Rating: 9
--------------------
=============================================
What would you like to do?

    [1] Append a movie
    [2] Search for a movie
    [3] Show all movies
    [4] Exit

Enter your choice[1/2/3/4]: 4
[ Exiting ]
```
