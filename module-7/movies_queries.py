import mysql.connector
from mysql.connector import errorcode

try:
    db = mysql.connector.connect(user = 'movies_user', password = 'popcorn', host = '127.0.0.1', database = 'movies', auth_plugin = 'mysql_native_password', raise_on_warnings = True)

    print("\n Database user {} connected to MySQL on host {} with database {}".format('movies_user', '127.0.0.1', 'movies'))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)


cursor = db.cursor()
cursor.execute("USE movies;")                                                           #Connect to movies database

cursor = db.cursor()
cursor.execute("SELECT studio_id, studio_name FROM studio;")                            #Select only records from Studio ID and Name
studios = cursor.fetchall()
print("-- DISPLAYING Studio RECORDS --")                                                #Display results using a for loop to print each row of results
for studio in studios:
    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

cursor = db.cursor()
cursor.execute("SELECT genre_id, genre_name FROM genre;")                               #Select only records from Genre ID and Name
genres = cursor.fetchall()
print("-- DISPLAYING Genre RECORDS --")                                                 #Display results using a for loop to print each row of results
for genre in genres:
    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

cursor = db.cursor()
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;")    #Select only records with Film Name and Runtime with the condition that runtime is greater than 2 hours
films = cursor.fetchall()
print("-- DISPLAYING Short Film RECORDS --")                                            #Display results using a for loop to print each row of results
for film in films:
    print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))

cursor = db.cursor()
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director;")     #Select only records from Film Name and Directior displayed in order of Director
films = cursor.fetchall()
print("-- DISPLAYING Director RECORDS in Order --")                                     #Display results using a for loop to print each row of results
for film in films:
    print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))

input("\nPress any key to close Database...")                                              #Wait for user input so that info can be read, then close database
db.close()