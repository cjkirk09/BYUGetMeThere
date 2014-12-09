import math
import json
from Query import Query
from Building import Building
from Coordinate import Coordinate
from Course import Course
from Floor import Floor
from Path import Path
from Schedule import Schedule
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
                y2 = float(end_coord.longitude)
                
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
        path.startCoord = startCoord.__dict__
        path.endCoord = endCoord.__dict__
        path.floorPlans = floorPlans
        path.buildingInfo = building.__dict__

        return path.__dict__
    
    @staticmethod
    def getSavedSchedules(username):
        schedules = Schedule.getAllForUser(username)
        
        saved_schedules = []
        for schedule in schedules:
            course = Course()
            course.loadFromID(schedule.course_id)
            schedule.course = course.__dict__
            saved_schedules.append(schedule.__dict__)
        
        return saved_schedules
        
    @staticmethod
    def loadSchedule(username, schedule_name):
        schedule = Schedule()
        schedule.loadFromCombinedKey(username, schedule_name)
        course = Course()
        course.loadFromID(schedule.course_id)
        schedule.course = course.__dict__
        return schedule.__dict__
        
    @staticmethod
    def saveSchedule(username, schedule_name, courses):
        for json_course in courses:
            course = Course()
            course.loadFromAll(json_course.name, json_course.time, json_course.days, json_course.building_id, json_course.room)
            course.save()

            schedule = Schedule()
            schedule.username = username
            schedule.schedule_name = schedule_name
            schedule.course_id = course.id
            
            schedule.save()
        return True
            
    @staticmethod
    def getBuildingInfo(building_id):
        building = Building()
        building.loadFromID(building_id)
        return building.__dict__
    
    @staticmethod    
    def getAllBuildings():
        buildings = []
        for building in Building.getAllBuildings():
            buildings.append(building.__dict__)
        return buildings
    
    @staticmethod
    def verifyUser(username, password):
        user = User()
        user.loadFromID(username)
        
        if user.password == password:
            return True
        else:
            return False
    
    @staticmethod        
    def createUser(username, password):
        user = User()
        user.loadFromID(username)
        if user.in_DB:
            return False
        user.username = username
        user.password = password
        user.save()
        return True
    
    
        
    




        
