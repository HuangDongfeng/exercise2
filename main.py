import sqlite3

# Read the contents of the file and save it to the list
with open('stephen_king_adaptations.txt', 'r') as file:
    stephen_king_adaptations_list = file.readlines()

# Establish database connections and create tables
connection = sqlite3.connect('stephen_king_adaptations.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table (
                    movieID INTEGER PRIMARY KEY,
                    movieName TEXT,
                    movieYear INTEGER,
                    imdbRating REAL
                )''')

# Insert the contents of the list into the database table
for movie in stephen_king_adaptations_list:
    movie_ID,movie_Name,movie_Year,imdbRating= movie.strip().split(',')
    cursor.execute('''SELECT * FROM stephen_king_adaptations_table''')
    if cursor.fetchone() is None:
        cursor.execute('''INSERT INTO stephen_king_adaptations_table ( movieID, movieName, movieYear, imdbRating)  VALUES (?, ?, ?, ?)''', (int(movie_ID[1:]), movie_Name, float(movie_Year), float(imdbRating)))

connection.commit()

# Loops that provide user options
while True:
    print('1. Search by movie name')
    print('2. Search by movie year')
    print('3. Search by movie rating')
    print('4. STOP')

    option = input('Please enter your option: ')

    if option == '1':
        movie_name = input('Enter the name of the movie: ')

        cursor.execute('''SELECT * FROM stephen_king_adaptations_table WHERE movieName = ?''', (movie_name,))
        movie_details = cursor.fetchone()

        if movie_details:
            print('Movie Name:', movie_details[1])
            print('Movie Year:', movie_details[2])
            print('IMDB Rating:', movie_details[3])
        else:
            print('No such movie exists in our database')

    elif option == '2':
        movie_year = input('Enter the year of the movie: ')

        cursor.execute('''SELECT * FROM stephen_king_adaptations_table WHERE movieYear = ?''', (int(movie_year),))
        movie_details = cursor.fetchall()

        if movie_details:
            for movie in movie_details:
                print('Movie Name:', movie[1])
                print('Movie Year:', movie[2])
                print('IMDB Rating:', movie[3])
        else:
            print('No movies were found for that year in our database')

    elif option == '3':
        movie_rating = input('Enter the minimum movie rating: ')

        cursor.execute('''SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?''', (float(movie_rating),))
        movie_details = cursor.fetchall()

        if movie_details:
            for movie in movie_details:
                print('Movie Name:', movie[1])
                print('Movie Year:', movie[2])
                print('IMDB Rating:', movie[3])
        else:
            print('No movies at or above that rating were found in the database')

    elif option == '4':
        break

# Close the database connection
connection.close()
