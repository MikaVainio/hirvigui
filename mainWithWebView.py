import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.uic import loadUi
import sankeyExample
import plotly

class MainWithWebView(QtWidgets.QMainWindow):
    """Creates a main window with a web view element"""

    def __init__(self):
        super().__init__()

        loadUi('mainWithWebView.ui', self)

        self.webView = self.webEngineView # Define the web view element

        self.showChart() # Call a function to build the chart

        # A method to populate web view with the chart object
    def showChart(self):
        chart = sankeyExample.testChart()

        # Use the chart object's method to convert it and read the plotly.js library from internet
        # self.webView.setHtml(chart.to_html(include_plotlyjs='cdn')) # Other variations seem not to work properly

        # Use plotly's offline method (even better create a html file in sankeyExample module)
        plotly.offline.plot(chart, filename='meatstreams.html') # Write the chart to a html file
        url = QtCore.QUrl('file:///meatstreams.html') # Create relative url to the file
        self.webView.load(url) # Load it into the web view element



if __name__ == "__main__":
    # Create an application object
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyle('Fusion')

    # Create the Main Window object from MainWithWebView Class and show it on the screen
    appWindow = MainWithWebView()
    appWindow.show()  # This can also be included in the main window's class
    sys.exit(app.exec())
    
