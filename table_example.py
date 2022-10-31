# LIBRARIES AND MODULES
# ---------------------

import sys # For possible arguments when creating the application
from PyQt5.QtWidgets import * # Load all widgets
from PyQt5.uic import loadUi # For loading the UI from a .ui file

# ----END OF LIBRALY AND MODULE LOADING -----

# List of tuples as static data to demonstrate table widget
tableData = [] # An empty list
tableData.append((1, 'Herkko', 'Hyväusko', 80)) # Add a tuple to the list
tableData.append((2, 'Jakke', 'Jäynä', 50))
tableData.append((3, 'Calle', 'Keckelberg', 90))
tableData.append((4, 'Assi', 'Kalma', 70))

# CLASS DEFINITIONS
# -----------------

# The Main Window class
class FormWithTable(QMainWindow):

    # Constructor method to create an instace of class
    def __init__(self):
        QMainWindow.__init__(self)

        # Create the UI from definition (.ui) file
        loadUi("table_example.ui", self)

        # Adjust properties of the Window
        self.setWindowTitle("Esimerkki tauluobjektista")

        # Call a function to populate the table
        self.addTableData()

    # Define the populating method
    def addTableData(self):

        # Set column headers as a list of strings
        columnHeaders = ["id", "etunimi", "sukunimi", "tehopisteet"]
        self.tableWidget.setHorizontalHeaderLabels(columnHeaders)

        # Set the row index to start from 0
        rowIndex = 0 

        # Cycle trough the table data
        for tupleIndex in tableData:
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

# ---- END OF CLASS DEFINITIONS ----

# CREATE AND RUN THE APPLICATION
# ------------------------------

# Check if app will be created and started directly from this file
if __name__ == "__main__":

    # Create an application object
    app = QApplication(sys.argv)

    # Create the Main Window object from FormWithTable Class and show it on the screen
    appWindow = FormWithTable()
    appWindow.show() # This can also be included in the FormWithTable class
    sys.exit(app.exec_())

# -----END OF APPLICATION BLOCK-----


    
