# APPLICATION FOR READING DATA FROM A DATABASE AND SHOWING RESULTS IN A TABLE WIDGET
# ==================================================================================

# LIBRARIES AND MODULES
# ---------------------

import psycopg2  # For database operations with PostgreSQL serverr
import sys  # For possible arguments when creating the application
from PyQt5.QtWidgets import *  # Load all widgets
from PyQt5.uic import loadUi  # For loading the UI from a .ui file


# ----END OF LIBRALY AND MODULE LOADING -----


# CLASS DEFINITIONS
# -----------------

# The Main Window class
class FormWithTable(QMainWindow):

    # Constructor method to create an instace of class -> the Window objrct to show when the app is running
    def __init__(self):
        QMainWindow.__init__(self)

        # Create the UI from the definition (.ui) file -> Where to find all elements in the Window
        loadUi("table_example2.ui", self)

        # Adjust properties of the Window
        self.setWindowTitle(
            "Tiedot käyttäjän määrittelemästä taulusta")

        # Create a status bar to show informative messages 
        self.statusBar = QStatusBar()  # Create a statusbar object
        self.setStatusBar(self.statusBar) # Set it as the statusbar for the main window
        self.statusBar.show()  # Make it visible

        # Disable loading button if table when the Window is created (and nothing has changed in teh UI)
        self.getDataPushButton.setEnabled(False) 

        # Define arguments for a connection string to connect the PostgreSQL Server
        self.database = "psycotesti"
        self.user = "sovellus"
        self.password = "Q2werty"
        self.host = "localhost"
        self.port = "5432"

        # Create a property for UI object tableNameLineEdit, in most cases you can't access UI objects directly
        self.tableName = self.tableNameLineEdit

        # SIGNALS (Invoked by events like mouse click or editing fields in the UI)
        # ------------------------------------------------------------------------

        # Call a function to populate the table widget when load button ie getDatPushButton (Hae tiedot) is pressed
        self.getDataPushButton.clicked.connect(self.addTableData)

        # Enable the load button when tablename has been edited
        self.tableName.textEdited.connect(self.activateButton)


        # ---- END OF SIGNALS ----

    # SLOTS (Methods to call when a signal is emited)
    # ---------------------------------------------

    # Activate (enable) the load button
    def activateButton(self):
        self.getDataPushButton.setEnabled(True)

        # Create an alert dialog for critical failures eg no database connection established
    def alert(self, alertMsg, additionalMsg, details):
        alertDialog = QMessageBox()  # Create a message box object
        alertDialog.setWindowTitle("Yhteysvirhe")
        alertDialog.setIcon(QMessageBox.Critical)  # Set icon to critical
        alertDialog.setText(alertMsg) # Basic information about the error in finnish
        alertDialog.setInformativeText(additionalMsg) # Additional information about the error in finnish
        alertDialog.setDetailedText(details) # Tehcnical details in english (from psycopg2)
        alertDialog.setStandardButtons(QMessageBox.Ok) # Only OK is needed to close the dialog
        alertDialog.exec_() # Open the message box

    # Define the populating method
    def addTableData(self, tableName):

        # Set status of the method to an error -> reset the value at the begining
        status = "Error"

        # Try to establish a connection to the server
        try:
            dbconnection = psycopg2.connect(database=self.database, user=self.user, password=self.password,
                                                 host=self.host, port=self.port)

            status = "Connected"
            # Create an automatically closing cursor to execute commands on the connection
            with dbconnection.cursor() as cursor:

                # Execute a command to get rows from the person table row by row
                nameOfTable = self.tableName.text() # Get text value of tableName property
                sqlClause = "SELECT * FROM " + nameOfTable + ";" # Build  a SQL clause accordingly
                cursor.execute(sqlClause) # Execute the clause using the cursor

                # Count amount of rows in the result set -> set the number of rows in the table widget
                rows = cursor.rowcount

                # Create a message to inform about rows read from the db
                msg = "Luettiin tietokannan " + self.database + " taulusta " + nameOfTable + " " + str(rows) + " riviä"
                self.statusBar.showMessage(msg, 5000)  # Show the message 5 seconds

                # Set status accordingly
                status = "Returned a result set"

                # Get records from the cursor expectig several rows
                records = cursor.fetchall()

                # Populate the table widget and do necessary settings

                # Create a list of column headers from cursor.description, name is the first item in the description
                columnHeaders = [cname[0] for cname in cursor.description]

                # Count number of columns in the resultset -> set number of colunms in the widget
                columns = len(columnHeaders)
                
                
            # --- End of with clause. Cursor is no more needed and will be closed automatically ---

            # Update column headers 
            self.tableWidget.setHorizontalHeaderLabels(columnHeaders)

            # Set the amount of rows in the table Widget, +1 to see empty row at the bottom
            self.tableWidget.setRowCount(rows + 1)

            # Set the amount of columns in the widget
            self.tableWidget.setColumnCount(columns)

            # Set the row index to start from 0
            rowIndex = 0
            
            # Cycle trough the table data to update table widget
            for tupleIndex in records:
                columnIndex = 0  # Set the colun index to start from 0

                # Cycle through a tuple
                for item in tupleIndex:

                    # Create data for a cell using QtableWidgetItem method
                    # item must be a string to be seen in the table widget
                    cellData = QTableWidgetItem(str(item))

                    # Populate the table named tableWidget in the UI
                    self.tableWidget.setItem(rowIndex, columnIndex, cellData)

                    # Increase columnIndex counter
                    columnIndex += 1

                # Increase rowIndex counter
                rowIndex += 1

        # Handle possible errors using the psycopg2 Error class
        except (Exception, psycopg2.Error) as error:
            virhe = "Tapahtui virhe: " + str(error)
            self.statusBar.showMessage(virhe, 5000)  # Show the message for 5 seconds in the status bar

            # Show a message box to inform user about the error
            self.alert("Tapahtui vakava virhe!", "Yhteyttä tietokantaan ei voitu muodostaa", virhe)

            # Set status to an error
            status = "Error"

            # Because of the error data might be invalid so lets clear the table widget and disable load button
            self.tableWidget.setRowCount(0)
            self.getDataPushButton.setEnabled(False)

        # Close the connection if status ik OK
        finally:

            if (status != "Error"):

                # Close the connection
                dbconnection.close()

                # Set status to disconnected
                status = "Disconnected"

    # ---- END OF SLOT DEFINITIONS ----


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
    appWindow.show()  # This can also be included in the FormWithTable class
    sys.exit(app.exec_())

# -----END OF APPLICATION BLOCK-----
