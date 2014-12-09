from Query import Query

class User:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.passkey = ""
        self.in_DB = False
        
    def loadFromID(self, username):
        result = Query.getOneResult("select * from BYU.USERS where USERNAME = '" + username + "'")
        if result is None:
            return
        self.loadFromResult(result)
        return self
        
    def loadFromAll(self, username, password, passkey):            
        self.username = username
        self.password = password
        self.passkey = passkey
        return self
        
    def loadFromResult(self, result):
        self.username = result[0]
        self.password = result[1]
        self.passkey = result[2]
        self.in_DB = True
        return self
    
    @staticmethod    
    def getAllUsers():
        users = {}
        results = Query.getAllResults("select * from BYU.USERS")
        for result in results:
            user = User()
            users.add(user.loadFromResult(result))
        return users
        
    def save(self):
        if self.in_DB:
            #update
            SQL = "update BYU.USERS set PASSWORD = '" + self.password + "', PASSKEY = '" + self.passkey + "' where USERNAME = '" + self.username + "'"
        else:
            #insert
            SQL = "insert into BYU.USERS (USERNAME, PASSWORD, PASSKEY) values('" + self.username + "', '" + self.password + "', '" + self.passkey + "')"
            self.in_DB = True
        Query.execute(SQL)
        
    def __str__(self):
        return "USERNAME: " + self.username + "\nPASSWORD: " + self.password + "\nPASSKEY: " + self.passkey + "\n" 
