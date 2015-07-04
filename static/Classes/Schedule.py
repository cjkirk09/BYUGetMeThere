from Query import Query

class Schedule:
    def __init__(self):
        self.id = 0
        self.username = ""
        self.schedule_name = ""
        self.in_DB = False
        
    def loadFromID(self, id):
        result = Query.getOneResult("select * from " + Query.getDBName() + ".SCHEDULES where ID = " + str(id))
        if result is None:
            return
        return self.loadFromResult(result)
        
    def loadFromAll(self, username, schedule_name):
        SQL = "select * from " + Query.getDBName() + ".SCHEDULES where USERNAME = '" + username + "' and SCHEDULE_NAME = '" + schedule_name + "'"
        result = Query.getOneResult(SQL)
        if result is not None:
            self.loadFromResult(result)
        self.username = username
        self.schedule_name = schedule_name
        return self
        
    def loadFromResult(self, result):
        self.id = result[0]
        self.username = result[1]
        self.schedule_name = result[2]
        self.in_DB = True
        return self
    
    @staticmethod    
    def getAllSchedules():
        schedules = []
        results = Query.getAllResults("select * from " + Query.getDBName() + ".SCHEDULES")
        for result in results:
            schedule = Schedule()
            schedules.append(schedule.loadFromResult(result))
        return schedules
        
    @staticmethod    
    def getAllForUser(username):
        schedules = []
        results = Query.getAllResults("select * from " + Query.getDBName() + ".SCHEDULES where USERNAME = '" + username + "'")
        for result in results:
            schedule = Schedule()
            schedules.append(schedule.loadFromResult(result))
        return schedules  
        
    def deleteCourses(self):
        SQL = "delete from " + Query.getDBName() + ".COURSES where SCHEDULE_ID = '" + str(self.id) + "'"
        Query.execute(SQL)
        
    def save(self):
        if self.in_DB:
            #update
            SQL = "update " + Query.getDBName() + ".SCHEDULES set USERNAME = '" + self.username + "', SCHEDULE_NAME = '" + self.schedule_name + "'"
            Query.execute(SQL)
        else:
            #insert
            SQL = "insert into " + Query.getDBName() + ".SCHEDULES (USERNAME, SCHEDULE_NAME) values('" + self.username + "', '" + self.schedule_name + "')"
            Query.execute(SQL)
            
            #get the new ID and save it to the object
            SQL = "select * from " + Query.getDBName() + ".SCHEDULES order by ID desc"
            result = Query.getOneResult(SQL)
            self.id = result[0]
            self.in_DB = True
    
    def __str__(self):
        return "ID: " + str(self.id) + "\nUSERNAME: " + self.username + "\nSCHEDULE_NAME: " + self.schedule_name + "\n" 
