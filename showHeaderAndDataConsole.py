import pgModule

dbOperation = pgModule.DatabaseOperation()
settingsDict = dbOperation.readDbSettingsFromJsonFile('test_connectionSettings.dat')

tableToInspect = 'public.read_tst3'
dbOperation.connectDbGetAllRows(settingsDict, tableToInspect)
resultSet = dbOperation.resultset
headers = dbOperation.columnHeaders
print (headers)
print(resultSet)