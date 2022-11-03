# A MODULE FOR PREPARING DATA AND POPULATING QTABLEWIDGETS
# ========================================================

# LIBRARIES AND MODULES
# ---------------------
from PyQt5.QtWidgets import QTableWidgetItem # Needed when preparing cell data

# METHODS
# -------
def prepareResultsToTableWidget(resultObject, widgetToUpdate):
    """Updates an existing TableWidget using an instace of DatabaseOperation class
       defined in the pgModule

    Args:
        resultObject (DatabaseOperation): instance of DatabaseOperation class providing error data and the result set
        widgetToUpdate (QTableWidget): instance of QtableWidget to be updated from the result set
    """
    if resultObject.errorCode == 0:
        widgetToUpdate.setColumnCount(resultObject.columns)
        widgetToUpdate.setHorizontalHeaderLabels(resultObject.columnHeaders)
        widgetToUpdate.setRowCount(resultObject.rows)


        # Set the row index to start from 0
        rowIndex = 0

        # Result set to be prepared is a list of tupples so 2 loops are needed to create rows and columns  
        
        # Cycle trough the list
        for tupleIndex in resultObject.resultset:
            columnIndex = 0  # Set the colun index to start from 0

            # Cycle through a tuple in hand
            for item in tupleIndex:

                # Create data for a cell using QtableWidgetItem method
                cellData = QTableWidgetItem(str(item)) # item must be a string to be seen in the table widget

                # Populate the cell of the table widget
                widgetToUpdate.setItem(rowIndex, columnIndex, cellData)

                # Increase columnIndex counter
                columnIndex += 1

            # Increase rowIndex counter
            rowIndex += 1
