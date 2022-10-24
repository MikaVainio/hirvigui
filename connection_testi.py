# FOR TESTING PSYCOPG2 CONNECTIONS TO LOCAL POSTGRESQL DATABASE

# LIBRARIES AND MODULES
import psycopg2

# DB CONNECTION PARAMETERS

# Try to establish a connection to the server
try:
    dbconnection = psycopg2.connect(database="psycotesti", user="sovellus", password="Q2werty",
                                    host="localhost", port="5432")

    # Get connection information, it is a dictionary containing connection parameters and some options
    conn_info = dbconnection.get_dsn_parameters()

    # Create a cursor to execute commands on the connection
    cursor =dbconnection.cursor()

    # Execute a command to get postgresql version
    cursor.execute("SELECT version();")

    # Get a record from the cursor
    record = cursor.fetchone()

    # Print the connection information
    for key in conn_info:
        print(key, conn_info[key])

    # Print the version of the PostgreSQL server   
    print("PostgreSQL versio on", record)

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






