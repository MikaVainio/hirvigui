# FOR TESTING DATA FETCHING FROM A TABLE

# LIBRARIES AND MODULES
import psycopg2

# DB CONNECTION PARAMETERS

# Try to establish a connection to the server
try:
    dbconnection = psycopg2.connect(database="psycotesti", user="sovellus2", password="Q2werty",
                                    host="localhost", port="5432")


    # Create a cursor to execute commands on the connection
    cursor =dbconnection.cursor()

    # Execute a command to get rows from the person table row by row 
    cursor.execute("SELECT * FROM person")
    rows = cursor.rowcount
    print("Taulussa on", rows, "riviä")
    record1 = cursor.fetchone()
    print("Ensimmäinen rivi", record1)
    record2 = cursor.fetchone()
    print("Toinen rivi", record2)


    """
    # Get records from the cursor limiting number of rows to 2 at the time
    records = cursor.fetchmany(2)
    print("Ensimmäiset 2 tietuetta", records)
    records = cursor.fetchmany(2)
    print("Seuraavat 2 tietuetta", records)
    """

    """
    # Execute a command to get all rows and columns from the person table
    cursor.execute("SELECT * FROM person")

    # Get records from the cursor expectig several rows
    records = cursor.fetchall()
    print(records)
    """
    status = "OK"
# Handle possible errors using the psycopg2 Error class
except (Exception, psycopg2.Error) as error:
    status = "Errors"
    print("Virhe muodostettaess yhteyttä tietokantaan", error)

# Close the connection if estabilished
finally:
    
    if (status == "OK"):

        # Close the cursor
        cursor.close()

        # Close the connection
        dbconnection.close()
        print("Yhteys tietokantaan suljettiin")