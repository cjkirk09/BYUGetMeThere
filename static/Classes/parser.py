import json
import datetime

from DB import DB


class Parser(object):
	@staticmethod
	def error(inputValue):
		tempDict = {}
		tempDict['error'] = inputValue
		return tempDict
	
	def getPathJSON(self,requestAsJson):
		# start place, end place
		#json.dumps(myJson, sort_keys=True, indent=4) #converts dict to JSON

		#myJson = requestAsJson #json.loads(request) #converts JSON to dict
		try:	
			#requestAsJson = json.loads(requestAsJson1)	
			startPlace = str(requestAsJson['startPlace'])
			endPlace = str(requestAsJson['endPlace'])
		except Exception, e:	
			toReturn = Parser.error(str(requestAsJson))
			return json.dumps(toReturn)

		f = open ("/var/www/BYUGetMeThereTest/BYUGetMeThere/static/Classes/out.txt",'w')
		#f.write(str(e))
		f.write(str(requestAsJson))			
				

		try:
			toReturn = DB.getPath(startPlace,endPlace)
		except Exception, e:
			toReturn = Parser.error(str(e))
			f.write("DBERROR" + str(e))

		f.close()
		return json.dumps(toReturn) 
		#db = fakeDB()
		
	def getCustomPathJSON(self,requestAsJson):
		try:
			startLat = requestAsJson['start_latitude']
			startLon = requestAsJson['start_longitude']
			toReturn = DB.getCustomPath(startLat,startLon,requestAsJson['endPlace'])
		except Exception, e:
			toReturn = Parser.error(str(e))

		return json.dumps(toReturn)

	def loginJSON(self,requestAsJson):
		try:
			if(DB.verifyUser(requestAsJson['username'],requestAsJson['password'])):
				toReturn = "True"
			else:
				toReturn = "False"
		except Exception, e:
			toReturn = json.dumps(Parser.error(str(e)))

		return toReturn

	def getSavedSchedules(self,requestAsJson):
		try:
			toReturn = DB.getSavedSchedules(requestAsJson['username'])
		except Exception, e:
			toReturn = Parser.error(str(e))

		return json.dumps(toReturn)

	def loadSchedule(self,requestAsJson):
		try:
			toReturn = DB.loadSchedule(requestAsJson['username'],requestAsJson['schedule_name'])
		except Exception, e:
			toReturn = Parser.error(str(e))

		return json.dumps(toReturn)

	def getBuildingInfo(self,buildingID):
		try:
			toReturn = DB.getBuildingInfo(buildingID)
		except Exception, e:
			toReturn = Parser.error(str(e))

		return json.dumps(toReturn)

	def verifyUser(self,requestAsJson):
		try:
			toReturn = DB.verifyUser(requestAsJson['username'],requestAsJson['password'])
		except Exception, e:
			toReturn = Parser.error(str(e))

		return json.dumps(toReturn)

	def createUser(self,requestAsJson):
		try:
			if(DB.createUser(requestAsJson['username'],requestAsJson['password'])):
				toReturn = "True"
			else:
				toReturn = "False"
		except Exception, e:
			toReturn = json.dumps(Parser.error(str(e)))

		return toReturn
	
	def saveSchedule(self,requestAsJson):
		try:
			if(DB.saveSchedule(requestAsJson['username'],requestAsJson['schedule_name'],requestAsJson['courses'])):
				toReturn = "True"
			else:
				toReturn = "False"
		except Exception, e:
			f = open ("/var/www/BYUGetMeThereTest/BYUGetMeThere/static/Classes/out.txt",'a')
			f.write(str(datatime.datetime.now()) + str(e))
			#f.write(str(requestAsJson))
			f.close()	
			toReturn = Parser.error(str(e))

		return toReturn

	def getAllBuildings(self):
		try:
			toReturn = DB.getAllBuildings()
		except Exception, e:
			toReturn = Parser.error(str(e))

		f = open ("/var/www/BYUGetMeThereTest/BYUGetMeThere/static/Classes/out.txt",'a')
		f.write(str(datetime.datetime.now()))
		#f.write(str(requestAsJson))
		f.close()	
		
		return json.dumps(toReturn)


