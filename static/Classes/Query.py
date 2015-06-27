import MySQLdb

class Query:
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost", user="root", passwd="google41", db="BYUDev")
        self.cur = self.db.cursor()

    @staticmethod
    def getAllResults(SQL):
        query = Query()
        query.cur.execute(SQL)
        return query.cur.fetchall()
        
    @staticmethod
    def getOneResult(SQL):
        query = Query()
        query.cur.execute(SQL)
        return query.cur.fetchone()
    
    @staticmethod    
    def execute(SQL):
        query = Query()
        query.cur.execute(SQL)
        query.db.commit()

