import math
import json
from Query import Query
from Building import Building
from Coordinate import Coordinate
from Floor import Floor
from Path import Path
from User import User

class DB:
    @staticmethod
    def getPath(start_place, end_place):
        #Get all coordinates in the database for our start_place
        start_coordinates = Coordinate.getAllForBuilding(start_place)
        if len(start_coordinates) == 0:
            raise Exception(start_place + " is not a building in our database")
            
        #Get all coordinate in the database for our end place
        end_coordinates = Coordinate.getAllForBuilding(end_place)
        if len(end_coordinates) == 0:
            raise Exception(end_place + " is not a building in our database")
            
        #Figure out the two closest coordinates
        (startCoord, endCoord) = DB.getClosestCoords(start_coordinates, end_coordinates)
        
        #Find all floor plans for our end place
        floorPlans = []
        floors = Floor.getAllForBuilding(end_place)
        for floor in floors:
            floorPlans.append(floor.floor_map)
        
        #Get building information for our end place
        building = Building()
        building.loadFromID(end_place)
        
        #Build path object to pass back
        path = Path()
        path.startCoord = startCoord.__dict__
        path.endCoord = endCoord.__dict__
        path.floorPlans = floorPlans
        path.buildingInfo = building.__dict__
        
        return path.__dict__
                  
    @staticmethod    
    def getClosestCoords(start_coords, end_coords):
        least = float("inf")
        for start_coord in start_coords:
            for end_coord in end_coords:
                x1 = float(start_coord.latitude)
                x2 = float(start_coord.longitude)
                y1 = float(end_coord.latitude)
                y2 = float(start_coord.longitude)
                
                distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                
                if distance < least:
                    least = distance
                    best_start = start_coord
                    best_end = end_coord
        return (best_start, best_end)
    
    @staticmethod    
    def getCustomPath(latitude, longitude, end_place):
        startCoord = Coordinate()
        startCoord.latitude = latitude
        startCoord.longitude = longitude
        
        #Get all coordinate in the database for our end place
        end_coordinates = Coordinate.getAllForBuilding(end_place)
        if len(end_coordinates) == 0:
            raise Exception(end_place + " is not a building in our database")
        
        #Figure out the two closest coordinates
        (startCoord, endCoord) = DB.getClosestCoords([startCoord], end_coordinates)
        
        #Find all floor plans for our end place
        floorPlans = []
        floors = Floor.getAllForBuilding(end_place)
        for floor in floors:
            floorPlans.append(floor.floor_map)
        
        #Get building information for our end place
        building = Building()
        building.loadFromID(end_place)
        
        #Build path object to pass back
        path = Path()
        path.startCoord = startCoord
        path.endCoord = endCoord
        path.floorPlans = floorPlans
        path.buildingInfo = building

        return str(path)
    
    @staticmethod
    def getSavedPaths(username, password):
        pass
        
    @staticmethod
    def loadPath(username, pathname):
        pass
        
    @staticmethod
    def loadTour(tourname):
        pass
        
    @staticmethod
    def savePath(username, pathname, points):
        pass
    
    @staticmethod
    def verifyLogin(username, password):
        user = User()
        user.loadFromID(username)
        
        if user.password == password:
            return True
        else:
            return False
    
    
        
    




        
