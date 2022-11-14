# APPLICATION FOR READING DATA FROM A DATABASE AND SHOWING RESULTS IN A TABLE WIDGET
# ==================================================================================

# LIBRARIES AND MODULES
# ---------------------

import pgModule  # A home made module to communicate with PostgreSQL server
import prepareData  # An other home made module for preparing data to be shown in Qt widgets
import sys  # For possible arguments when creating the application
from datetime import date  # For getting current date
# Load all widgets (not willing to type all we need at the time)
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi  # For loading the UI from a .ui file
from PyQt5.QtCore import QDate # For using date transformation tools, we need ISO dates


# ----END OF LIBRALY AND MODULE LOADING -----


# CLASS DEFINITIONS
# -----------------

# The Main Window class
class MultiPageWindow(QMainWindow):

    # Constructor method to create an instace of class -> the Window objrct to show when the app is running
    def __init__(self):
        QMainWindow.__init__(self)

        # Create the UI from the definition (.ui) file -> Where to find all elements in the Window
        loadUi("pagedUiExample.ui", self)

        # Adjust properties of the Window
        self.setWindowTitle(
            "Monisivuinen käyttöliittymä")

        # Create a status bar to show informative messages
        self.statusBar = QStatusBar()  # Create a statusbar object
        # Set it as the statusbar for the main window
        self.setStatusBar(self.statusBar)
        self.statusBar.show()  # Make it visible

        # UI ELEMENTS
        # -----------

        # The tab widget for browsing UI pages
        self.pages = self.tabWidget

        # Summary page (Yhteenveto)
        self.summaryRefreshBtn = self.refreshPushButton
        self.summaryMeatSharedTW = self.meatSharedTableWidget

        # Kills page (Kaadot)
        self.killsShotDE = self.shotDateEdit
        self.killsShotByCB = self.shotByComboBox
        self.killsAddPB = self.addShotPushButton
        self.killsShotByCB2V = self.shotByComboBox2Value
        self.killShowIdPB = self.showIdPushButton

        # Set values for elements

        # SIGNALS (Invoked by events like mouse click or editing fields in the UI)
        # ------------------------------------------------------------------------

        # Emit a signal when user changes active page
        self.pages.currentChanged.connect(self.agentPopulateChoices)

        # Signal a slot when refresh button is cliked on summary page (Yhteenveto)
        self.summaryRefreshBtn.clicked.connect(self.getSummaryData)

        # Signal when value has been changed in the Combo Box
        self.killsShotByCB.currentIndexChanged.connect(self.showShotByName)

        # Signal when add a shot button (Lisää) is pressed
        self.killsAddPB.clicked.connect(self.sendShotDataToProcedure)

        self.killShowIdPB.clicked.connect(self.showShotById)

        # ---- END OF SIGNALS ----

        # Initialize the UI with some defaults
        self.setDefaultDateToday()

    # SLOTS (Methods to call when a signal is emited)
    # ---------------------------------------------

    # Set the default date to today
    def setDefaultDateToday(self):
        currentDate = date.today()
        self.killsShotDE.setDate(currentDate)

    # This agent calls 2 methods at the same time to populate 2 combo boxes
    def agentPopulateChoices(self):
        self.populateChoises()
        self.ids = self.populateChoises2Values()
        
    # Populate UI elements with updated choises
    def populateChoises(self):
        # Clear values to avoid appending choices every time page is changed
        self.killsShotByCB.clear()
        databaseOperation = pgModule.DatabaseOperation()
        connectionArgs = databaseOperation.readDbSettingsFromJsonFile(
            'connectionSettings2.dat')  # Read DB settings
        tableToRead = 'public.kokonimet'  # View with a single column of full names
        databaseOperation.connectDbGetAllRows(
            connectionArgs, tableToRead)  # Execute the reading operation

        # Result set is a list of tuples even when there is only one column in the view
        cBItems = []  # Empty list for choises in the combobox

        for result in databaseOperation.resultset:
            # Convert first element in the tuple to string
            resultAsString = str(result[0])
            cBItems.append(resultAsString)

        self.killsShotByCB.addItems(cBItems)

    # Populate UI elements with updated choices
    def populateChoises2Values(self):
        # Clear values to avoid appending choices every time page is changed
        self.killsShotByCB2V.clear()
        databaseOperation = pgModule.DatabaseOperation()
        connectionArgs = databaseOperation.readDbSettingsFromJsonFile(
            'connectionSettings2.dat')  # Read DB settings
        tableToRead = 'public.kokonimet2'  # View with 2 columns
        databaseOperation.connectDbGetAllRows(
            connectionArgs, tableToRead)  # Execute the reading operation

        # Result set is a list of tuples even when there is only one column in the view
        cBIds = [] # Empty list for hunter ids
        cBItems = []  # Empty list for choises in the combobox

        for result in databaseOperation.resultset:
            cBId = result[0] # Hunter id is the first element in the tuple
            resultAsString = str(result[1]) # Convert 2nd element in the tuple to string
            cBItems.append(resultAsString) # Append it to the  choices list
            cBIds.append(cBId) # Append the Id to the list of Ids

        self.killsShotByCB2V.addItems(cBItems) # Populate the combo box
        return cBIds # Return the list of ids

    # Create an alert dialog for critical failures eg no database connection established
    def alert(self, alertMsg, additionalMsg, details):
        alertDialog = QMessageBox()  # Create a message box object
        alertDialog.setWindowTitle("Yhteysvirhe")
        alertDialog.setIcon(QMessageBox.Critical)  # Set icon to critical
        # Basic information about the error in finnish
        alertDialog.setText(alertMsg)
        # Additional information about the error in finnish
        alertDialog.setInformativeText(additionalMsg)
        # Tehcnical details in english (from psycopg2)
        alertDialog.setDetailedText(details)
        # Only OK is needed to close the dialog
        alertDialog.setStandardButtons(QMessageBox.Ok)
        alertDialog.exec_()  # Open the message box

    # Read data from a table using our home made pgModules
    def getSummaryData(self):

        # Create a databaseOperation object to handle the connection and result sets
        # Create the database operation object
        databaseOperation = pgModule.DatabaseOperation()
        connectionArgs = databaseOperation.readDbSettingsFromJsonFile(
            'connectionSettings2.dat')  # Read DB settings
        if databaseOperation.errorCode != 0:
            self.alert(databaseOperation.errorMessage,
                       databaseOperation.detailedMessage)

        # Read the line edit to get name of the table to read
        tableToRead = 'public.jaetut_lihat'
        databaseOperation.connectDbGetAllRows(
            connectionArgs, tableToRead)  # Execute the reading operation
        if databaseOperation.errorCode != 0:
            self.alert(databaseOperation.errorMessage,
                       databaseOperation.detailedMessage)

        # Perapare and show results on tableWidget using prepareData
        prepareData.prepareResultsToTableWidget(
            databaseOperation, self.summaryMeatSharedTW)

    # Show shooter's name on the status bar
    def showShotByName(self):
        selectionWas = self.killsShotByCB.currentText()
        self.statusBar.showMessage(selectionWas, 5000)

    def showShotById(self):
        selectionIxWas = self.killsShotByCB2V.currentIndex()
        print('Jäsennumero oli', self.ids[selectionIxWas])

    # Same as above using agent method and second method with arguments
    def agentSummaryGetData(self):
        dbTable = 'public.jaetut_lihat'
        widget = self.summaryMeatSharedTW
        self.getData2(dbTable, widget)

    def getSummaryData2(self, dbTable, widget):
        databaseOperation = pgModule.DatabaseOperation()  # Create the object
        connectionArgs = databaseOperation.readDbSettingsFromJsonFile(
            'connectionSettings2.dat')  # Read DB settings
        databaseOperation.connectDbGetAllRows(
            connectionArgs, dbTable)  # Execute operation

        # Perapare and show results on tableWidget using prepareData
        prepareData.prepareResultsToTableWidget(databaseOperation, widget)

    def sendShotDataToProcedure(self):
        dateOfShot = self.killsShotDE.date() # Get the date in QDate format
        pythonDate = QDate.toPyDate(dateOfShot) # Convert to Python format (ISO)
        shotBy = self.killsShotByCB.currentText() # Get the name of shooter
        procedureCallParameters = 'Proseduurin parametritn ovat ' + str(pythonDate) + ', ' + shotBy
        self.statusBar.showMessage(procedureCallParameters, 5000)

# CREATE AND RUN THE APPLICATION
# ------------------------------
# Check if app will be created and started directly from this file
if __name__ == "__main__":

    # Create an application object
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # Create the Main Window object from FormWithTable Class and show it on the screen
    appWindow = MultiPageWindow()
    appWindow.show()  # This can also be included in the FormWithTable class
    sys.exit(app.exec_())
