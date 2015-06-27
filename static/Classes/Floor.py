from Query import Query

class Floor:
    def __init__(self):
        self.id = 0
        self.building_id = ""
        self.floor_number = -1
        self.floor_map = ""
        self.in_DB = False
        
    def loadFromID(self, id):
        result = Query.getOneResult("select * from BYUDev.FLOORS where ID = " + str(id))
        if result is None:
            return
        return self.loadFromResult(result)
        
    def loadFromAll(self, building_id, floor_number, floor_map):
        self.building_id = building_id
        self.floor_number = floor_number
        self.floor_map = floor_map
        return self
        
    def loadFromResult(self, result):
        self.id = result[0]
        self.building_id = result[1]
        self.floor_number = result[2]
        self.floor_map = result[3]
        self.in_DB = True
        return self
    
    @staticmethod    
    def getAllFloors():
        floors = []
        results = Query.getAllResults("select * from BYUDev.FLOORS")
        for result in results:
            floor = Floor()
            floors.append(floor.loadFromResult(result))
        return floors
    
    @staticmethod    
    def getAllForBuilding(building_id):
        floors = []
        results = Query.getAllResults("select * from BYUDev.FLOORS where BUILDING_ID = '" + building_id + "'")
        for result in results:
            floor = Floor()
            floors.append(floor.loadFromResult(result))
        return floors
        
    def save(self):
        if self.in_DB:
            #update
            SQL = "update BYUDev.FLOORS set BUILDING_ID = '" + self.building_id + "', FLOOR_NUMBER = " + str(self.floor_number) + ", FLOOR_MAP = '" + self.floor_map + "' where ID = " + str(self.id)
            Query.execute(SQL)
        else:
            #insert
            SQL = "insert into BYUDev.FLOORS (BUILDING_ID, FLOOR_NUMBER, FLOOR_MAP) values('" + self.building_id + "', " + str(self.floor_number) + ", '" + self.floor_map + "')"
            Query.execute(SQL)
            
            #get the new ID and save it to the object
            SQL = "select * from BYUDev.FLOORS order by ID desc"
            result = Query.getOneResult(SQL)
            self.id = result[0]
            self.in_DB = True
    
    def __str__(self):
        return "ID: " + str(self.id) + "\nBUILDING_ID: " + self.building_id + "\nFLOOR NUMBER: " + str(self.floor_number) + "\nFLOOR MAP: " + self.floor_map + "\n" 
