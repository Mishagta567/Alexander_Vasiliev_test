
def findNearestServer(SchemaData):
    serverName = 'ormuco506.ca'

#   1) Use synhronyzed data/library: ServerName | Schema.data | lastUsed
#   while search - should use servers Geo-locations: check them 'order by distance'

#   2) should be able to do fast calls to that Server to get confirmation what library dosn't expired.
#       - if it expired - update 'synhronyzed data' (delete this row), send updates to other servers, return to step 1.
#       - if it doesn't expired - return serverName

#   if didn't find out any server - just return nearest serverName. Update synhronyzed data/library

#   While checkin data/library for the ServerName - should also check 'black_ServerName_list' and avoid get those ServerNames

    return serverName


def singleTread(serverName, SchemaData, timeLimit):
    resultData = []

#   Call to the serverName
#   SchemaData - Schema and Data to retrive. Can be splited in 2+  paramets. F.e.: Schema_name, tables_name, query etc.

#   function on server, should be able to cancel request beyond timeLimit
    return resultData


def getData(SchemaData):
    resultData = []
    while len(resultData) == 0:
# step 1
        serverName = findNearestServer(SchemaData)
        resultData = singleTread(serverName, SchemaData, 5000)
#       if we didn't got responce in our timeLimit - cancel this request. 'Update synhronyzed data/library' - return to server
#       write Server name in 'black_ServerName_list'

