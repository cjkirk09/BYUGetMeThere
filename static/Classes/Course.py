from Query import Query

class Course:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.section = ""
        self.time = ""
        self.days = ""
        self.building_id = ""
        self.room = ""
        self.in_DB = False
        
    def loadFromID(self, id):
        result = Query.getOneResult("select * from BYU.COURSES where ID = " + str(id))
        if result is None:
            return
        self.loadFromResult(result)
        
    def loadFromAll(self, name, section, time, days, building_id, room):
        self.name = name
        self.section = section
        self.time = time
        self.days = days
        self.building_id = building_id
        self.room = room
        
    def loadFromResult(self, result):
        self.id = result[0]
        self.name = result[1]
        self.section = result[2]
        self.time = result[3]
        self.days = result[4]
        self.building_id = result[5]
        self.room = result[6]
        self.in_DB = True
    
    @staticmethod    
    def getAllCourses():
        courses = {}
        results = Query.getAllResults("select * from BYU.COURSES")
        for result in results:
            course = Course()
            courses.add(course.loadFromResult(result))
        return courses
    
    def save(self):
        if self.in_DB:
            #update
            SQL = "update BYU.COURSES set NAME = '" + self.name + "', SECTION = '" + self.section + "', TIME = '" + self.time + "', DAYS = '" + self.days + "', BUILDING_ID = '" + self.building_id + "', ROOM = '" + self.room + "' where ID = " + str(self.id)
            Query.execute(SQL)
        else:
            #insert
            SQL = "insert into BYU.COURSES (NAME, SECTION, TIME, DAYS, BUILDING_ID, ROOM) values('" + self.name + "', '" + self.section + "', '" + self.time + "', '" + self.days + "', '" + self.building_id + "', '" + self.room + "')"
            Query.execute(SQL)
            
            #get the new ID and save it to the object
            SQL = "select * from BYU.COURSES order by ID desc"
            result = Query.getOneResult(SQL)
            self.id = result[0]
            self.in_DB = True
        
    def __str__(self):
        return "ID: " + str(self.id) + "\nNAME: " + self.name + "\nSECTION: " + self.section + "\nTIME: " + self.time + "\nDAYS: " + self.days + "\nBUILDING_ID: " + self.building_id + "\nROOM: " + self.room + "\n" 
