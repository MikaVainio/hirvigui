# FOR TESTING DATA FETCHING FROM A TABLE

# LIBRARIES AND MODULES
import psycopg2

# DB CONNECTION PARAMETERS

# Try to establish a connection to the server
try:
    dbconnection = psycopg2.connect(database="psycotesti", user="sovellus", password="Q2werty",
                                    host="localhost", port="5432")


    # Create a cursor to execute commands on the connection
    cursor =dbconnection.cursor()

    # Execute a command to get rows from the person table
    cursor.execute("SELECT * FROM person")

    # Create a list of column names from cursor.description, name is the first item in the description
    colum_names = [cname[0] for cname in cursor.description]

    print("cursor.description näyttää tältä:", cursor.description)

    # Print names in a for loop
    for column_name in colum_names:
        print(column_name)
  
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