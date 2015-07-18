from Query import Query

class Course:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.time = 0
        self.building_id = ""
        self.room = ""
        self.day = 0000000
        self.in_DB = False
        
    def loadFromID(self, id):
        print self.id
        result = Query.getOneResult("select * from " + Query.getDBName() + ".COURSES where ID = " + str(id))
        if result is None:
            return
        self.loadFromResult(result)
        return self
        
    def loadFromAll(self, name, time, days, building_id, room, section_id):
        self.name = name
        self.time = time
        self.days = days
        self.building_id = building_id
        self.room = room
        self.section_id = section_id
        return self
        
    def loadFromResult(self, result):
        self.id = result[0]
        self.name = result[1]
        self.time = result[2]
        self.building_id = result[3]
        self.room = result[4]
        self.day = result[5]
        self.section_id = result[6]
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
        results = Query.getAllResults("select * from " + Query.getDBName() + ".COURSE_TO_USER where user_id = '" + user_id + "'")
        for result in results:
            course = Course()
            courses.append(course.loadFromID(result[0]).__dict__)
        return courses
    
    def save(self, user_id):
        if self.in_DB:
            #update
            SQL = "update " + Query.getDBName() + ".COURSES set courseNAME = " + self.name + ", TIME = " + self.time + ", DAY = " + self.days + ", BUILDING_ID = " + self.building_id + ", ROOM = " + self.room + ", section_id = " + self.section_id + " where ID = " + str(self.id)
            Query.execute(SQL)
            #update the join table
        else:
            #insert
            SQL = "insert into " + Query.getDBName() + ".COURSES (courseNAME, TIME, DAY, BUILDING_ID, ROOM,section_id) values('" + self.name + "', '" + self.time + "', " + str(self.days) + ", '" + self.building_id + "', '" + str(self.room) + "', " + str(self.section_id) + ")"
            Query.execute(SQL)
            #insert into the join table

            #get the new ID and save it to the object
            SQL = "select * from " + Query.getDBName() + ".COURSES order by ID desc"
            result = Query.getOneResult(SQL)
            self.id = result[0]
            self.in_DB = True
            SQL2 = "insert into " + Query.getDBName() + ".COURSE_TO_USER (course_id, user_id) values ('" + str(self.id) + "','" + user_id + "')"
            result = Query.execute(SQL2)
        
    def __str__(self):
        return "ID: " + str(self.id) + "\nNAME: " + self.name + "\nTIME: " + self.time + "\nDAYS: " + str(self.days) + "\nBUILDING_ID: " + self.building_id + "\nROOM: " + self.room + "\n" 
