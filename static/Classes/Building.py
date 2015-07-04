from Query import Query
from Floor import Floor

class Building:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.phone_number = ""
        self.hours = "N/A"
        self.in_DB = False
        self.floorPlans = []
        
    def loadFromID(self, id):
        result = Query.getOneResult("select * from " + Query.getDBName() +".BUILDINGS where ID = '" + id + "'")
        if result is None:
            return
        self.loadFromResult(result)
        #floorPlans = []
        floors = Floor.getAllForBuilding(id)
        for floor in floors:
            self.floorPlans.append(floor.floor_map)
        return self
        
#doenst appear to be used ever
    def loadFromAll(self, id, name, phone_number, hours):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.hours = hours
        return self
        
    def loadFromResult(self, result):
        self.id = result[0]
        self.name = result[1]
        self.phone_number = result[2]
        self.hours = result[3]
        self.in_DB = True
        return self
    
    @staticmethod    
    def getAllBuildings():
        buildings = []
        results = Query.getAllResults("select * from " + Query.getDBName() + ".BUILDINGS")
        for result in results:
            building = Building()
            buildings.append(building.loadFromResult(result))
        return buildings
        
    def save(self):
        if self.in_DB:
            #update
            SQL = "update " + Query.getDBName() + ".BUILDINGS set NAME = '" + self.name + "', PHONE_NUMBER = '" + self.phone_number + "', HOURS = '" + self.hours + "' where ID = '" + self.id + "'"
        else:
            #insert
            SQL = "insert into " + Query.getDBName() + ".BUILDINGS (ID, NAME, PHONE_NUMBER, HOURS) values('" + self.id + "', '" + self.name + "', '" + self.phone_number + "', '" + self.hours + "')"
        Query.execute(SQL)
        self.in_DB = True
        
    def __str__(self):
        return "ID: " + self.id + "\nNAME: " + self.name + "\nPHONE NUMBER: " + self.phone_number + "\nHOURS: " + self.hours + "\n" 
