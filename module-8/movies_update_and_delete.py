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

def show_films(cursor, title):                                                                     #Define the function that'll be used to modify this database
    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre,"     #Inner Join the respective tables together to get the required columns
                   " studio_name as 'Studio Name' FROM film INNER JOIN genre ON film.genre_id"
                   " = genre.genre_id INNER JOIN studio ON film.studio_id = studio.studio_id;")
    
    films = cursor.fetchall()
    print("\n -- {} --".format(title))                                                             #Print the appropriate title based on what's passed to the function

    for film in films:                                                                             #Use a for loop to print the gathered information and associated changes
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n"
              .format(film[0], film[1], film[2], film[3]))

show_films(cursor, "DISPLAYING FILMS")                                                             #Display the Films pre-changes

cursor.execute("INSERT INTO film (film_id, film_name, film_releaseDate, film_runtime, "            #Insert the wonderful film Independence Day
               "film_director, studio_id, genre_id) VALUES('4', 'Independence Day', '1996', "
               "'145', 'Roland Emmerich', '1', '2');")

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")                                                #Show results after Insertion

cursor.execute("UPDATE film SET genre_id = '1' WHERE film_name = 'Alien';")                        #Change genre of Alien to Horror

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")                       #Show results of Genre change

cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator';")                                  #Delete Gladiator

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")                                                #Show results with Gladiator removed


input("\nPress any key to close Database...")                                                      #Wait for user input so that info can be read, then close database
db.close()