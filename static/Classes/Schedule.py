from Query import Query

class Schedule:
    def __init__(self):
        self.id = 0
        self.username = ""
        self.schedule_name = ""
        self.course_id = ""
        self.in_DB = False
        
    def loadFromID(self, id):
        result = Query.getOneResult("select * from BYU.SCHEDULES where ID = " + str(id))
        if result is None:
            return
        return self.loadFromResult(result)
        
    def loadFromCombinedKey(self, username, schedule_name)
        result = Query.getOneResult("select * from BYU.SCHEDULES where USERNAME = '" + username + "' and SCHEDULE_NAME = '" + schedule_name + "'"
        if result is None:
            return
        return self.loadFromResult(result)
        
    def loadFromAll(self, username, schedule_name, course_id):
        self.username = username
        self.schedule_name = schedule_name
        self.course_id = course_id
        return self
        
    def loadFromResult(self, result):
        self.id = result[0]
        self.username = result[1]
        self.schedule_name = result[2]
        self.course_id = result[3]
        self.in_DB = True
        return self
    
    @staticmethod    
    def getAllSchedules():
        schedules = []
        results = Query.getAllResults("select * from BYU.SCHEDULES")
        for result in results:
            schedule = Schedule()
            schedules.append(schedule.loadFromResult(result))
        return schedules
    
    @staticmethod    
    def getAllForUser(username):
        schedules = []
        results = Query.getAllResults("select * from BYU.SCHEDULES where USERNAME = '" + username + "'")
        for result in results:
            schedule = Schedule()
            schedules.append(schedule.loadFromResult(result))
        return schedules
        
    def save(self):
        if self.in_DB:
            #update
            SQL = "update BYU.SCHEDULES set USERNAME = '" + self.username + "', SCHEDULE_NAME = '" + self.schedule_name + "', COURSE_ID = '" + self.course_id + "' where ID = " + str(self.id)
            Query.execute(SQL)
        else:
            #insert
            SQL = "insert into BYU.SCHEDULES (USERNAME, SCHEDULE_NAME, COURSE_ID) values('" + self.username + "', '" + self.schedule_name + "', '" + self.course_id + "')"
            Query.execute(SQL)
            
            #get the new ID and save it to the object
            SQL = "select * from BYU.SCHEDULES order by ID desc"
            result = Query.getOneResult(SQL)
            self.id = result[0]
            self.in_DB = True
    
    def __str__(self):
        return "ID: " + str(self.id) + "\nUSERNAME: " + self.building_id + "\nSCHEDULE_NAME: " + self.schedule_name + "\nCOURSE_ID: " + self.course_id + "\n" 
