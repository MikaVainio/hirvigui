# AN EXAMPLE OF RUNTIME ADJUSTABLE THEME USING Qt-Material LIBRARY
# ===============================================================

# LIBRARIES AND MODULES

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from qt_material import QtStyleTools

# Class definitons

class RuntimeStylesheets(QMainWindow, QtStyleTools):
    
    def __init__(self):
        
        super().__init__()
        # Create the main window as main
        self.main = loadUi('chooseThemeExample.ui', self) # Attention this must be named main

        self.apply_stylesheet(self.main, 'dark_amber.xml') # Set the initial theme
        self.show_dock_theme(self.main) # Show the theme adjusting palette


if __name__ == "__main__":
    app = QApplication(sys.argv)
    appWindow = RuntimeStylesheets()
    appWindow.main.show()
    app.exec_()