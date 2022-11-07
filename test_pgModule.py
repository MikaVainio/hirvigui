# TESTS FOR THE pgmodule.py MODULE

# LIBRARIES AND MODULES
import pgModule  # Module to be tested
import json  # for handling json based setting files
import datetime # to test result set containing dates


# TESTS

# Database connection settings

# Create a databaseOperation object for connectivity tests
databaseOperation = pgModule.DatabaseOperation()

# Read data from the settings file (test_connectionSettings.dat)


def test_readConnectionSettings():
    connectionSettings = databaseOperation.readDbSettingsFromJsonFile(
        'test_connectionSettings.dat')

    # Results should be
    expectedSettings = {'server': 'localhost', 'port': '5432',
                        'database': 'tests', 'role': 'postgres', 'pwd': 'Q2werty'}

    assert connectionSettings == expectedSettings


def test_createConnectionWithAllArguments():

    # Set all arguments
    connectionArgumentsDict = databaseOperation.createConnectionArgs(
        'tests', 'postgres', 'Q2werty', '127.0.0.1', '5433')

    # Dictionary should be
    expectedDict = {'server': '127.0.0.1', 'port': '5433',
                    'database': 'tests', 'role': 'postgres', 'pwd': 'Q2werty'}

    assert connectionArgumentsDict == expectedDict

# Create connection arguments, set host and port to default values


def test_createConnectionWithDefaultArguments():

    # Set other arguments to database is tests, role is postgres and password is Q2werty
    connectionArgumentsDict = databaseOperation.createConnectionArgs(
        'tests', 'postgres', 'Q2werty')

    # Dictionary should be
    expectedDict = {'server': 'localhost', 'port': '5432',
                    'database': 'tests', 'role': 'postgres', 'pwd': 'Q2werty'}

    assert connectionArgumentsDict == expectedDict

# Create settigs file

# Write connection settings to a file and compare the file to original connection arguments
def test_writeConnectionSettings():
    # Set all arguments
    connectionArguments = databaseOperation.createConnectionArgs(
        'tests', 'postgres', 'Q2werty', '127.0.0.1', '5433')

    # Write settings to file
    databaseOperation.saveDbSettingsToJsonFile(
        'test_connectionSettings_write.dat', connectionArguments)

    # Read the file
    settingsFile = open('test_connectionSettings_write.dat', 'r')
    storedConnectionArguments = json.load(settingsFile)
    settingsFile.close()

    assert storedConnectionArguments == connectionArguments 

# Test reading data from read_test table containing int4 and varchar columns -> integer and string
def test_readAllRowsCommonTypes():
    connectionSettings = databaseOperation.readDbSettingsFromJsonFile(
        'test_connectionSettings.dat')
    databaseOperation.connectDbGetAllRows(connectionSettings, 'read_test')
    resultSet = databaseOperation.resultset

    # Expected resultset
    expectedResultset = [(1, 'Jakke', 'Jäynä'), (2, 'Jonne', 'Janttari'), (3, 'Tuittu', 'Kiukkunen')]

    assert resultSet == expectedResultset

# Reading test data from table containing floats, booleans and dates
def test_realdAllRowsSpecialTypes():
    connectionSettings = databaseOperation.readDbSettingsFromJsonFile(
        'test_connectionSettings.dat')
    databaseOperation.connectDbGetAllRows(connectionSettings, 'read_tst2')
    resultSet = databaseOperation.resultset

    # Expected resultset
    expectedResultset = [(1, 76.5, False, datetime.date(2000, 11, 7)), (2, 80.5, True, datetime.date(1998, 3, 16))]

    assert resultSet == expectedResultset
