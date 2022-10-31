# FOR TESTING UPDATES TO A TABLE

# LIBRARIES AND MODULES
import psycopg2

# DB CONNECTION PARAMETERS

# Try to establish a connection to the server
try:
    dbconnection = psycopg2.connect(database="psycotesti", user="sovellus", password="Q2werty",
                                    host="localhost", port="5432")

    # Create a cursor to execute commands on the connection
    cursor = dbconnection.cursor()

    # Execute a command to update person's data
    cursor.execute("UPDATE person SET tehopisteet = 120 WHERE id = 3")
    
    # Commit the transaction
    dbconnection.commit()

    # Let user know if a successfull transaction
    print("Tehopisteet päivitettiin")

    
   
# Handle possible errors using the psycopg2 Error class
except (Exception, psycopg2.Error) as error:
    print("Virhe muodostettaess yhteyttä tietokantaan", error)

# Close the connection if estabilished
finally:
    
    if (dbconnection):

        # Close the cursor
        cursor.close()

        # Close the connection
        dbconnection.close()
        print("Yhteys tietokantaan suljettiin")