# AN EXAMPLE OF LIGHT AND DARK THEMES USING Qt-Material LIBRARY
# ===============================================================

# LIBRARIES AND MODULES
import sys # For the system args
from PyQt5 import QtCore, QtWidgets # For the Qt functionality
from PyQt5.uic import loadUi # For loading the UI file
from qt_material import apply_stylesheet, QtStyleTools # For theme adjustments, QtStyleTools for runtime

extra = {
            'danger':'#ff0000',
            'success': '#00ff00',
            'font_family': 'Ink Free',
            'density_scale': '-2',
            }

# Class for the main window
class MainWithThemes(QtWidgets.QMainWindow, QtStyleTools):
    """Creates a main window with theme menu"""

    # Constructor
    def __init__(self):
        super().__init__()

        loadUi('chooseThemeExample.ui', self)

        # Menu action for changing the theme to dark, see the UI-file
        self.actionDark.triggered.connect(self.setDarkTheme)

        # Menu action for changing the theme to light, see the UI-file
        self.actionLight.triggered.connect(self.setLightTheme)

        # Tallenna push button without icon
        self.saveReportPB = self.pushButton # Name is pushButton in the UI file
        self.saveReportPB.setProperty('class', 'danger')

        # Kahville push button has a custom icon set in the Qt Designer
        self.coffeePB = self.coffeePushButton
        self.coffeePB.setProperty('class', 'success')
        self.coffeePB.clicked.connect(self.show_dock_theme(self))

    def setDarkTheme(self):
        
        # How nostalgic: 30 years ago they used to sell amber screens
        apply_stylesheet(self, theme='dark_amber.xml', extra=extra)
        

    def setLightTheme(self):
        apply_stylesheet(self, theme='light_teal.xml', invert_secondary=True)

if __name__ == "__main__":

    # Create the application
    app = QtWidgets.QApplication(sys.argv)
    
    # Create the Main Window object from MainWithWebView Class and show it on the screen
    appWindow = MainWithThemes()
    appWindow.show()  # This can also be included in the main window's class
    sys.exit(app.exec())
    