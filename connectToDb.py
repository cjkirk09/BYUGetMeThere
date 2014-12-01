import MySQLdb

class DB (object):
	def getBuildings(self):
		db = MySQLdb.connect(host="localhost", # your host, usually localhost
		             user="root", # your username
		              passwd="google41", # your password
		              db="BYU") # name of the data base

		cur = db.cursor() 

		cur.execute("SELECT * FROM BUILDINGS")
		return cur.fetchall()[0][1]		

