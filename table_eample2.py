# APPLICATION FOR READING DATA FROM A DATABASE AND SHOWING RESULTS IN A TABLE WIDGET
# ==================================================================================

# LIBRARIES AND MODULES
# ---------------------

import psycopg2 # For database operations with PostgreSQL serverr
import sys # For possible arguments when creating the application
from PyQt5.QtWidgets import * # Load all widgets
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi # For loading the UI from a .ui file


# ----END OF LIBRALY AND MODULE LOADING -----


# CLASS DEFINITIONS
# -----------------

# The Main Window class
class FormWithTable(QMainWindow):

    # Constructor method to create an instace of class
    def __init__(self):
        QMainWindow.__init__(self)

        # Create the UI from definition (.ui) file
        loadUi("table_example.ui", self)

        self.alert('Virhe otettaessa yhteyttä tietokantaan', "Väärä käyttäjätunnus")

        # Adjust properties of the Window
        self.setWindowTitle("Esimerkki taulun tiedoista, jotka tulevat tietokannasta")
        
        # Create a status bar to show informative messages (replaces print function used in previous exercises)
        self.statusBar = QStatusBar() # Create a statusbar objecti
        self.setStatusBar(self.statusBar) # Set it as the statusbar for the main window
        self.statusBar.show() # Make it visible  
        
        # Call a function to populate the table
        # self.alert("Voi kettu", "Yhteys tietokantaan ei onnistunut")
        self.addTableData()
        

    # Create an alert dialog for critical failures eg no database connection established
   
        # msgBox.buttonClicked.connect(msgButtonClick)
    def alert(self, alertMsg, additionalMsg):
        alertDialog = QMessageBox() # Create a message box object
        alertDialog.setIcon(QMessageBox.Critical) # Set icon to critical
        alertDialog.setText(alertMsg)
        alertDialog.setInformativeText(additionalMsg)
        alertDialog.setStandardButtons(QMessageBox.Ok)
        alertDialog.exec_()

    # Define the populating method
    def addTableData(self):

        # Try to establish a connection to the server
        try:
            self.dbconnection = psycopg2.connect(database="psycotesti", user="sovellus", password="Q2werty",
                                            host="localhost", port="5432")

            # Create a cursor to execute commands on the connection
            cursor = self.dbconnection.cursor()

            # Execute a command to get rows from the person table row by row 
            cursor.execute("SELECT * FROM person")

            # Count amount of rows in the result set -> set the number of rows in the table widget 
            rows = cursor.rowcount

            # Create a message to inform about rows read from the db
            msg = "Luettiin tietokannasta " + str(rows) + " riviä"
            self.statusBar.showMessage(msg, 5000) # Show the message 5 seconds
                    
            # Execute a command to get all rows and columns from the person table
            cursor.execute("SELECT * FROM person")

            # Get records from the cursor expectig several rows
            records = cursor.fetchall()
            
            # Populate the table widget and do necessary settings 

            # Create a list of column headers from cursor.description, name is the first item in the description
            columnHeaders = [cname[0] for cname in cursor.description]
            self.tableWidget.setHorizontalHeaderLabels(columnHeaders)

            # Set the amount of rows in the table Widget
            self.tableWidget.setRowCount(rows + 1)          
                
            # Set the row index to start from 0
            rowIndex = 0 

            # Cycle trough the table data
            for tupleIndex in records:
                columnIndex = 0 # Set the colun index to start from 0

                # Cycle through a tuple
                for item in tupleIndex:

                    # Create data for a cell using QtableWidgetItem method
                    cellData = QTableWidgetItem(str(item)) # item must be a string to be seen in the table widget
                    
                    # Populate the table named tableWidget in the UI
                    self.tableWidget.setItem(rowIndex, columnIndex, cellData)

                    # Increase columnIndex counter
                    columnIndex += 1

                # Increase rowIndex counter
                rowIndex += 1


        # Handle possible errors using the psycopg2 Error class
        except (Exception, psycopg2.Error) as error:
            self.statusBar.showMessage(msg, 5000) # Show the message 5 seconds
            

        #Close the connection if estabilished
        finally:
            
            if self.dbconnection:

                # Close the cursor
                cursor.close()

                # Close the connection
                self.dbconnection.close()
                

                
# ---- END OF CLASS DEFINITIONS ----

# CREATE AND RUN THE APPLICATION
# ------------------------------

# Check if app will be created and started directly from this file
if __name__ == "__main__":

    # Create an application object
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # Create the Main Window object from FormWithTable Class and show it on the screen
    appWindow = FormWithTable()
    appWindow.show() # This can also be included in the FormWithTable class
    sys.exit(app.exec_())

# -----END OF APPLICATION BLOCK-----


    
