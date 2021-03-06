from Query import Query

class Course:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.user_id = ""
        self.time = 0
        self.building_id = ""
        self.room = ""
        self.day = ""
        self.in_DB = False
        
    def loadFromID(self, id):
        print self.id
        result = Query.getOneResult("select * from " + Query.getDBName() + ".COURSES where ID = " + str(id))
        if result is None:
            return
        self.loadFromResult(result)
        return self
        
    def loadFromAll(self, name, user_id, time, days, building_id, room):
        self.name = name
        self.user_id = user_id
        self.time = time
        self.days = days
        self.building_id = building_id
        self.room = room
        return self
        
    def loadFromResult(self, result):
        self.id = result[0]
        self.name = result[1]
        self.user_id = result[2]
        self.time = result[3]
        self.building_id = result[4]
        self.room = result[5]
        self.day = result[6]
        self.in_DB = True
        return self
    
    @staticmethod    
    def getAllCourses():
        courses = []
        results = Query.getAllResults("select * from " + Query.getDBName() + ".COURSES")
        for result in results:
            course = Course()
            courses.append(course.loadFromResult(result))
        return courses
        
    @staticmethod
    def getAllCoursesForUserName(user_id):
        courses = []
        results = Query.getAllResults("select * from " + Query.getDBName() + ".COURSES where user_id = " + str(user_id))
        for result in results:
            course = Course()
            courses.append(course.loadFromResult(result))
        return courses
    
    def save(self):
        if self.in_DB:
            #update
            SQL = "update " + Query.getDBName() + ".COURSES set NAME = '" + self.name + "', user_id = " + str(self.user_id) + ", TIME = '" + self.time + "', DAYS = '" + self.days + "', BUILDING_ID = '" + self.building_id + "', ROOM = '" + self.room + "' where ID = " + str(self.id)
            Query.execute(SQL)
        else:
            #insert
            SQL = "insert into " + Query.getDBName() + ".COURSES (NAME, user_id, TIME, DAYS, BUILDING_ID, ROOM) values('" + self.name + "', " + str(self.user_id) + ", '" + self.time + "', '" + self.days + "', '" + self.building_id + "', '" + self.room + "')"
            Query.execute(SQL)
            
            #get the new ID and save it to the object
            SQL = "select * from " + Query.getDBName() + ".COURSES order by ID desc"
            result = Query.getOneResult(SQL)
            self.id = result[0]
            self.in_DB = True
        
    def __str__(self):
        return "ID: " + str(self.id) + "\nNAME: " + self.name + "\nuser_id: " + str(self.user_id) + "\nTIME: " + self.time + "\nDAYS: " + self.days + "\nBUILDING_ID: " + self.building_id + "\nROOM: " + self.room + "\n" 
