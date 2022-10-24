# FOR TESTING DATA INSERTS TO TABLE BY PROCEDURE

# LIBRARIES AND MODULES
import psycopg2

# VARIABLES FROM THE UI
given_name = "Pekka"
sur_name = "Palturi"
points = 50

# DB CONNECTION PARAMETERS

# Try to establish a connection to the server
try:
    dbconnection = psycopg2.connect(database="psycotesti", user="sovellus", password="Q2werty",
                                    host="localhost", port="5432")

    # Create a cursor to execute commands on the connection
    cursor = dbconnection.cursor()

    # Execute a call to stored procedure add_person using placeholders
    cursor.execute("CALL add_person(%s, %s, %s);", (given_name, sur_name, points))
    
    # Commit the transaction
    dbconnection.commit()
   
# Handle possible errors using the psycopg2 Error class
except (Exception, psycopg2.Error) as error:
    print("Virhe muodostettaessa yhteyttä tietokantaan", error)

# Close the connection if estabilished
finally:
    
    if (dbconnection):

        # Close the cursor
        cursor.close()

        # Close the connection
        dbconnection.close()
        print("Yhteys tietokantaan suljettiin")