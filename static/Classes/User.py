from Query import Query

class User:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.salt = ""
        self.in_DB = False
        
    def loadFromID(self, username):
        result = Query.getOneResult("select * from " + Query.getDBName() + ".USERS where USERNAME = '" + username + "'")
        if result is None:
            return User()
        self.loadFromResult(result)
        return self
        
    def loadFromAll(self, username, password):            
        self.username = username
        self.password = password
        return self
        
    def loadFromResult(self, result):
        self.username = result[0]
        self.password = result[1]
        self.salt = result[2]
        self.in_DB = True
        return self
    
    @staticmethod    
    def getAllUsers():
        users = {}
        results = Query.getAllResults("select * from " + Query.getDBName() + ".USERS")
        for result in results:
            user = User()
            users.add(user.loadFromResult(result))
        return users
        
    def save(self):
        if self.in_DB:
            #update
            SQL = "update " + Query.getDBName() + ".USERS set PASSWORD = '" + self.password + "' where USERNAME = '" + self.username + "'"
        else:
            #insert
            SQL = "insert into " + Query.getDBName() + ".USERS (USERNAME, PASSWORD, SALT) values('" + self.username + "', '" + self.password + "', '" + self.salt + "')"
            self.in_DB = True
        Query.execute(SQL)
        
    def __str__(self):
        return "USERNAME: " + self.username + "\nPASSWORD: " + self.password + "\n" 
