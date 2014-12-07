import json

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
		startPlace = str(requestAsJson['startPlace'])
		endPlace = str(requestAsJson['endPlace'])
		
		try:
			toReturn = DB.getPath(startPlace,endPlace)
		except Exception, e:
			toReturn = Parser.error(str(e))

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
			if(DB.verifyLogin(requestAsJson['username'],requestAsJson['password'])):
				toReturn = "True"
			else:
				toReturn = "False"
		except Exception, e:
			toReturn = Parser.error(str(e))

		return toReturn




