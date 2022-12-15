# AN EXAMPLE OF LIGHT AND DARK THEMES USING PyQtDarkTheme LIBRARY
# ===============================================================

# LIBRARIES AND MODULES
import sys # For the system args
from PyQt5 import QtCore, QtWidgets # For the Qt functionality
from PyQt5.uic import loadUi # For loading the UI file
import qdarktheme # For theme adjustments

# Class for the main window
class MainWithThemes(QtWidgets.QMainWindow):
    """Creates a main window with theme menu"""

    # Constructor
    def __init__(self):
        super().__init__()

        loadUi('chooseThemeExample.ui', self)

        # Menu action for changing the theme to dark, see the UI-file
        self.actionDark.triggered.connect(self.setDarkTheme)

        # Menu action for changing the theme to light, see the UI-file
        self.actionLight.triggered.connect(self.setLightTheme)

        # A combo box containing supported themes
        self.chooseThemeCB = self.comboBox # Name is comboBox in the UI file
        self.chooseThemeCB.addItems(qdarktheme.get_themes()) # Populate combobox with themes from the library
        self.chooseThemeCB.currentTextChanged.connect(qdarktheme.setup_theme) # Signal library's setup method

        # Tallenna push button, theme overrides default icons, restore icon
        self.saveReportPB = self.pushButton # Name is pushButton in the UI file
        saveBtnPixmap = QtWidgets.QStyle.StandardPixmap.SP_DialogSaveButton # Create a pixmap for the button
        saveBtnIcon = self.style().standardIcon(saveBtnPixmap) # Define it as an icon
        self.saveReportPB.setIcon(saveBtnIcon) # Add the icon to the button

        # Kahville push button has a custom icon set in the Qt Designer. Not overridden.
        self.coffeePB = self.coffeePushButton

    def setDarkTheme(self):
        qdarktheme.setup_theme() # Default theme is the dark one

    def setLightTheme(self):
        # Set a custom style for push buttons
        customButtonStyle = """
        QPushButton {
            font: 87 10pt "Arial Black";
            border-color: rgb(85, 255, 127);
        }
        """
        
        # Apply the light theme and custom styles
        qdarktheme.setup_theme('light', additional_qss=customButtonStyle) 

if __name__ == "__main__":

    # Enable High Dots Per Inch for high quality screens. Do before creating the app
    # qdarktheme.enable_hi_dpi() # not necessary when using displays in our class A253

    # Create the application
    app = QtWidgets.QApplication(sys.argv)
    
    # Create the Main Window object from MainWithWebView Class and show it on the screen
    appWindow = MainWithThemes()
    appWindow.show()  # This can also be included in the main window's class
    sys.exit(app.exec())
    