import sys  # For possible arguments when creating the application
from PyQt5.QtWidgets import *  # Load all widgets
from PyQt5.uic import loadUi  # For loading the UI from a .ui file

# The Main Window class
class FormWithComboBox(QMainWindow):

    # Constructor method to create an instace of class
    def __init__(self):
        QMainWindow.__init__(self)

        # Create the UI from definition (.ui) file
        loadUi("combo_example.ui", self)

        # Adjust properties of the Window
        self.setWindowTitle(
            "Esimerkki yhdistelmäruudusta")

        # Create a reference (property) for the Combo in the UI
        self.animalCombo = self.animalTypeComboBox

        # Create a reference to a big label in the UI
        self.selection = self.selectionLabel
        self.selection.setHidden(True) # Don't show until value chosen fron the combo box

        # Create a reference to What's this check box
        self.whatsThisOn = self.whatsThisModeCheckBox

        # Populate the ComboBox with items 
        self.animalCombo.addItems(["Hirvi", "Valkohäntäpeura", "Kuusipeura"]) # Many string values as a list with addItems method
        self.animalCombo.addItem("Metsäkauris") # A single item with addItem method

        # Create a status bar to show informative messages 
        self.statusBar = QStatusBar()  # Create a statusbar object
        self.setStatusBar(self.statusBar) # Set it as the statusbar for the main window
        self.statusBar.show()  # Make it visible

        # Create a signal when something is selected, this signal sends the index of the selected item
        self.animalCombo.currentIndexChanged.connect(self.selectionChanged)

        # Create a signal to enable or disable What's This mode
        self.whatsThisOn.stateChanged.connect(self.checkWtMOde)

    # Create a slot to react to the selection change, must receive the index from signal    
    def selectionChanged(self, index):

        # Update the label to show the selected item
        self.selection.setHidden(False)
        self.selection.setText("Taas yksi " + self.animalCombo.currentText().lower() + " vähemmän")

        # Show the index of the selection on statusbar for 5 seconds
        msg = ("Valitun eläimen indeksi on " + str(index))
        self.statusBar.showMessage(msg, 5000) 

    # A Method to enter what's this mode
    def checkWtMOde(self):
        if self.whatsThisOn.isChecked() == True:
            QWhatsThis.enterWhatsThisMode()
            
            # There is only one widget with what's this message so clear the checkbox after entering to the mode
            self.whatsThisOn.setChecked(False)

        else:
            QWhatsThis.leaveWhatsThisMode()




# CREATE AND RUN THE APPLICATION
# ------------------------------
# Check if app will be created and started directly from this file
if __name__ == "__main__":

    # Create an application object
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # Create the Main Window object from FormWithTable Class and show it on the screen
    appWindow = FormWithComboBox()
    appWindow.show()  # This can also be included in the FormWithTable class
    sys.exit(app.exec_())
