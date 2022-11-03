# APPLICATION FOR READING DATA FROM A DATABASE AND SHOWING RESULTS IN A TABLE WIDGET
# ==================================================================================

# LIBRARIES AND MODULES
# ---------------------

import pgModule # A home made module to communicate with PostgreSQL server
import prepareData # An other home made module for preparing data to be shown in Qt widgets
import sys  # For possible arguments when creating the application
from PyQt5.QtWidgets import *  # Load all widgets (not willing to type all we need at the time)
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

        # Create a property for UI object tableNameLineEdit, in most cases you can't access UI objects directly
        self.tableName = self.tableNameLineEdit

        # Create a property for table widget
        self.tableW1 = self.tableWidget

        # SIGNALS (Invoked by events like mouse click or editing fields in the UI)
        # ------------------------------------------------------------------------
        
        # Call a function to populate the table widget when load button ie getDatPushButton (Hae tiedot) is pressed
        

        # Signal intermediate slot (agent) when load button is cliked
        self.getDataPushButton.clicked.connect(self.agentGetData)

        # Signal using a lambda function (often hard to read, must be single line)
        # self.getDataPushButton.clicked.connect(lambda x: self.getData2(self.tableName.text(), self.tableW1))

        # Enable the load button when tablename has been edited
        self.tableName.textEdited.connect(self.activateButton)

        # Signal when the user clicks an item on the table widget
        self.tableW1.itemClicked.connect(self.onTableItemClick)

        # ---- END OF SIGNALS ----

    # SLOTS (Methods to call when a signal is emited)
    # ---------------------------------------------

    # Activate (enable) the load button
    def activateButton(self):
        self.getDataPushButton.setEnabled(True)

    # A method to find out what item is selected in the table widget and show it on the status bar
    def onTableItemClick(self, item):
        selectedRow = item.row() # The row of the selection
        selectedColumn = item.column() # The column of the selection
        idValue = self.tableWidget.item(selectedRow, 0).text() # text value of the id field
        selectionWas = item.text() + " löytyi riviltä " + str(selectedRow) + " ja piilotettu id on " + str(idValue)
        self.statusBar.showMessage(selectionWas, 5000)

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

    # Read data from a table using our home made pgModules
    def getData(self):

        # Create a databaseOperation object to handle the connection and result sets
        databaseOperation = pgModule.DatabaseOperation() # Create the object
        connectionArgs = databaseOperation.readDbSettingsFromJsonFile('connectionSettings.dat') # Read DB settings
        tableToRead = self.tableName.text() # Read the line edit to get name of the table to read
        databaseOperation.connectDbGetAllRows(connectionArgs, tableToRead) # Execute the reading operation

        # Perapare and show results on tableWidget using prepareData
        prepareData.prepareResultsToTableWidget(databaseOperation, self.tableW1)

    def agentGetData(self):
        dbTable = self.tableName.text()
        widget = self.tableW1
        self.getData2(dbTable, widget)

    def getData2(self, dbTable, widget):
        databaseOperation = pgModule.DatabaseOperation() # Create the object
        connectionArgs = databaseOperation.readDbSettingsFromJsonFile('connectionSettings.dat') # Read DB settings
        databaseOperation.connectDbGetAllRows(connectionArgs, dbTable) # Execute operation

        # Perapare and show results on tableWidget using prepareData
        prepareData.prepareResultsToTableWidget(databaseOperation, widget)   

    

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
