# FOR TESTING RESULTSET FROM A FUNCTION

# LIBRARIES AND MODULES
import psycopg2


# DB CONNECTION PARAMETERS

# Try to establish a connection to the server
try:
    dbconnection = psycopg2.connect(database="psycotesti", user="sovellus", password="Q2werty",
                                    host="localhost", port="5432")

    # Create a cursor to execute commands on the connection
    cursor = dbconnection.cursor()

    # Execute a select clause from the function with parameter
    cursor.execute("SELECT * FROM get_person_by_id(7)")

    # Get the result set (a single row)
    result = cursor.fetchone()
    print(result)
    
    
   
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