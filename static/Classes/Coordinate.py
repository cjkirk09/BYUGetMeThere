from Query import Query

class Coordinate:
    def __init__(self):
        self.id = ""
        self.building_id = ""
        self.latitude = ""
        self.longitude = ""
        self.in_DB = False
        
    def loadFromID(self, id):
        result = Query.getOneResult("select * from BYU.COORDINATES where ID = '" + id + "'")
        if result is None:
            return
        return self.loadFromResult(result)
        
    def loadFromAll(self, id, building_id, latitude, longitude):
        self.id = id
        self.building_id = building_id
        self.latitude = latitude
        self.longitude = longitude
        return self
        
    def loadFromResult(self, result):
        self.id = result[0]
        self.building_id = result[1]
        self.latitude = result[2]
        self.longitude = result[3]
        self.in_DB = True
        return self
    
    @staticmethod    
    def getAllCoordinates():
        coordinates = []
        results = Query.getAllResults("select * from BYU.COORDINATES")
        for result in results:
            coordinate = Coordinate()
            coordinates.append(coordinate.loadFromResult(result))
        return coordinates
    
    @staticmethod    
    def getAllForBuilding(building_id):
        coordinates = []
        results = Query.getAllResults("select * from BYU.COORDINATES where BUILDING_ID = '" + building_id + "'")
        for result in results:
            coordinate = Coordinate()
            coordinates.append(coordinate.loadFromResult(result))
        return coordinates
        
    def save(self):
        if self.in_DB:
            #update
            SQL = "update BYU.COORDINATES set BUILDING_ID = '" + self.building_id + "', LATITUDE = '" + self.latitude + "', LONGITUDE = '" + self.longitude + "' where ID = '" + self.id + "'"
            Query.execute(SQL)
        else:
            #insert
            SQL = "insert into BYU.COORDINATES (BUILDING_ID, LATITUDE, LONGITUDE) values('" + self.building_id + "', '" + self.latitude + "', '" + self.longitude + "')"
            Query.execute(SQL)
            
            #get the new ID and save it to the object
            SQL = "select * from BYU.COORDINATES order by ID desc"
            result = Query.getOneResult(SQL)
            self.id = result[0]
            self.in_DB = True
            
        
    def __str__(self):
        return "ID: " + str(self.id) + "\nBUILDING_ID: " + self.building_id + "\nLATITUDE: " + self.latitude + "\nLONGITUDE: " + self.longitude + "\n" 
