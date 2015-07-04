import json
import datetime
import urllib2

from DB import DB
from Directions import Directions


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

		f = open ("/var/www/BYUGetMeThere/BYUGetMeThere/static/Classes/out.txt",'w')
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
		try:			#   enter the curr loc from json here
			if requestAsJson.get('startLocation'):
				latidude = requestAsJson['startLocation']['latitude']
				longitude = requestAsJson['startLocation']['longitude']
				toReturn = DB.getCustomPath(latidude, longitude ,requestAsJson['endPlace'])
			else:
				toReturn = DB.getCustomPath(40.249145, -111.649238,requestAsJson['endPlace'])
		except Exception, e:
			toReturn = Parser.error(str(e))

		toReturn['building_id'] = 'currentLocation'
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

	def getSavedSchedulesJSON(self,requestAsJson):
		f = open ("/var/www/BYUGetMeThere/BYUGetMeThere/static/Classes/out.txt",'a')
		#f.write(str(datetime.datetime.now()) + str(e))
		f.write(str(requestAsJson))
		f.close()			
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
				toReturn = "True1"
			else:
				toReturn = "False"
		except Exception, e:
			toReturn = json.dumps(Parser.error(str(e)))

		return toReturn
	
	def saveSchedule(self,requestAsJson):
		try:
			if(DB.saveSchedule(requestAsJson['username'],requestAsJson['day_of_week'],requestAsJson['courses'])):
				toReturn = "True"
			else:
				toReturn = "False"
		except Exception, e:
			f = open ("/var/www/BYUGetMeThere/BYUGetMeThere/static/Classes/out.txt",'a')
			f.write(str(datetime.datetime.now()) + str(e))
			#f.write(str(requestAsJson))
			f.close()	
			toReturn = Parser.error(str(e))

		return toReturn

	def getAllBuildings(self):
		try:
			toReturn = DB.getAllBuildings()
		except Exception, e:
			toReturn = Parser.error(str(e))

		f = open ("/var/www/BYUGetMeThere/BYUGetMeThere/static/Classes/out.txt",'a')
		f.write(str(datetime.datetime.now()))
		#f.write(str(requestAsJson))
		f.close()	
		
		return json.dumps(toReturn)

	def getDirections(self, requestAsJson, api_key):
		try:	
			#requestAsJson = json.loads(requestAsJson1)	
			if requestAsJson.get('startLocation'):
				latidude = requestAsJson['startLocation']['latitude']
				longitude = requestAsJson['startLocation']['longitude']		
				dbInfo = DB.getCustomPath(latidude, longitude ,requestAsJson['endPlace'])
			else:			
				startPlace = str(requestAsJson['startPlace'])
				endPlace = str(requestAsJson['endPlace'])
				dbInfo = DB.getPath(startPlace,endPlace)
			#return json.dumps(dbInfo)
			startLat = str(dbInfo["startCoord"]["latitude"])
			startLong = str(dbInfo["startCoord"]["longitude"])
			endLat = str(dbInfo["endCoord"]["latitude"])
			endLong = str(dbInfo["endCoord"]["longitude"])
			
			google = urllib2.urlopen("https://maps.googleapis.com/maps/api/directions/json?origin="+startLat+","+startLong+"&destination="+endLat+","+endLong+"&mode=walking&key="+api_key).read()
			direction = Directions(json.loads(google),dbInfo)
			#print json.dumps(direction.__dict__)
			return json.dumps(direction.__dict__)
		except Exception, e:	
			toReturn = Parser.error(str(e))
			return json.dumps(toReturn)


